#import os
#import pickle
#import gzip
import zipfile
import pytest
from pathlib import Path
#from unittest.mock import patch

# Assuming the source functions are in basic_helpers.file_helper
from basic_helpers.file_helper import (
    do_pickle, do_unpickle, do_gzip_pkl, do_ungzip_pkl,
    do_gzip_txt, do_ungzip_txt, do_zip_extract, get_c01_from_cell,
    get_tagcnt_dict_fnames, extract_tagcnt_version_num, 
    get_next_version_fname, get_act_dir_list
)

@pytest.fixture
def sample_dict():
    return {"key": "value", "number": 42}

## Serialization Tests
def test_pickle_roundtrip(tmp_path, sample_dict):
    fname = tmp_path / "test.pkl"
    do_pickle(sample_dict, fname)
    assert fname.exists()
    
    loaded = do_unpickle(fname)
    assert loaded == sample_dict

def test_do_unpickle_success(tmp_path: Path):
    """Verify that a valid pickle file is loaded correctly."""
    data = {"key": "value"}
    fname = tmp_path / "test_data.pkl"
    do_pickle(data, str(fname))
        
    result = do_unpickle(str(fname))
    assert result == data

def test_unpickle_file_not_found_raises(tmp_path: Path):
    """
    Verify that a non-existent file raises an exception.
    Updated to reflect the new fatal error behavior.
    """
    fname = tmp_path / "non_existent.pkl"
    
    # We use pytest.raises to assert that an Exception (specifically FileNotFoundError) occurs
    with pytest.raises(FileNotFoundError):
        do_unpickle(str(fname))

def test_unpickle_corrupt_file_raises(tmp_path: Path):
    """Verify that a corrupted file raises a pickle-related exception."""
    fname = tmp_path / "corrupt.pkl"
    fname.write_text("this is not a pickle file")
    
    with pytest.raises(Exception):
        do_unpickle(str(fname))

def test_gzip_pickle_roundtrip(tmp_path, sample_dict):
    fname = tmp_path / "test.pkl.gz"
    do_gzip_pkl(sample_dict, fname)
    
    # Verify it's actually gzipped
    with open(fname, "rb") as f:
        assert f.read(2) == b'\x1f\x8b' # Gzip magic number
        
    loaded = do_ungzip_pkl(fname)
    assert loaded == sample_dict

def test_gzip_pickle_roundtrip_filenotfoun(tmp_path, sample_dict):
    fname = tmp_path / "test.pkl.gz"
    fname_wrong = tmp_path / "wrong_test.pkl.gz"
    do_gzip_pkl(sample_dict, fname)
    
    # Verify it's actually gzipped
    with open(fname, "rb") as f:
        assert f.read(2) == b'\x1f\x8b' # Gzip magic number

    # We use pytest.raises to assert that an Exception (specifically FileNotFoundError) occurs
    with pytest.raises(FileNotFoundError):
        do_ungzip_pkl(fname_wrong)

def test_gzip_text_roundtrip(tmp_path):
    fname = tmp_path / "test.txt.gz"
    content = "Hello World"
    do_gzip_txt(content, fname)
    
    loaded = do_ungzip_txt(fname)
    assert loaded == content

## Zip Extraction Tests
def test_do_zip_extract(tmp_path):
    # Create a dummy zip file
    zip_path = tmp_path / "test.zip"
    extract_dir = tmp_path / "extracted"
    extract_dir.mkdir()
    
    with zipfile.ZipFile(zip_path, 'w') as zf:
        zf.writestr("file1.txt", "content1")
        zf.writestr("file2.txt", "content2")

    # Test full extraction
    files = do_zip_extract(zip_path, dest_path=extract_dir)
    assert len(files) == 2
    assert (extract_dir / "file1.txt").exists()

    # Test filtered extraction
    files_filtered = do_zip_extract(zip_path, dest_path=extract_dir, fname_filter=["file1.txt"])
    assert len(files_filtered) == 1
    assert "file1.txt" in files_filtered[0]

## String Processing Tests
@pytest.mark.parametrize("input_cell, expected", [
    ("AB", ("A", "B")),
    ("cA", ("_c", "A")),
    ("aa", ("_a", "_a")),
    ("Zz", ("Z", "_z")),
])
def test_get_c01_from_cell(input_cell, expected):
    assert get_c01_from_cell(input_cell) == expected

## Versioning and Tag Analysis Tests
def test_extract_tagcnt_version_num():
    assert extract_tagcnt_version_num("COND_TAGCNT_DICT_v0003.gzip") == 3
    assert extract_tagcnt_version_num("INVALID_NAME.gzip") == 0

def test_get_tagcnt_dict_fnames(tmp_path):
    # Setup lvl1 directory
    lvl1 = tmp_path / "lvl1"
    lvl1.mkdir()
    (lvl1 / "TEST_v0001.gzip").touch()
    (lvl1 / "TEST_v0002.gzip").touch()
    (lvl1 / "OTHER_v0001.gzip").touch()

    fnames = get_tagcnt_dict_fnames("TEST", tmp_path)
    assert len(fnames) == 2
    assert all(f.startswith("TEST") for f in fnames)
    assert fnames == sorted(fnames) # Verify sorting

def test_get_next_version_fname_empty(tmp_path):
    lvl1 = tmp_path / "lvl1"
    lvl1.mkdir()
    next_f = get_next_version_fname("NEW", tmp_path)
    assert next_f == "NEW_v0001.gzip"

def test_get_next_version_fname_increment(tmp_path):
    lvl1 = tmp_path / "lvl1"
    lvl1.mkdir()
    (lvl1 / "DATA_v0010.gzip").touch()
    
    next_f = get_next_version_fname("DATA", tmp_path)
    assert next_f == "DATA_v0011.gzip"

## Directory Check Tests
def test_get_act_dir_list(tmp_path):
    lvl = "lvl1"
    d_name = "active_dir"
    (tmp_path / lvl / d_name).mkdir(parents=True)
    
    assert get_act_dir_list(d_name, lvl, str(tmp_path)) is True
    assert get_act_dir_list("wrong_dir", lvl, str(tmp_path)) is False

