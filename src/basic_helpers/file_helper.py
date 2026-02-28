import pickle, gzip, os, zipfile  
from pathlib import Path
from typing import Any  # , TypeVar 

# TypeVar => would allow to specify the expected data type returned by e.g. do_unpickle
# it would be also possible to define specific data classes / TypedDicts for specific dictionaries

type FilePath = str | Path
type FilePathOrNone = str | Path | None

def do_pickle(obj: Any, fname: FilePath) -> None:
    with open(fname, "wb") as f:
        pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)

def do_unpickle(fname: FilePath) -> Any | None:
    try:
        with open(fname, "rb") as f:
            obj = pickle.load(f)
            
        return obj
    except Exception as e:
        print(e, fname)
        return None

def do_gzip_pkl(obj: Any, fname: FilePath) -> None:
    with gzip.open(fname, "wb") as f:
        pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
        #f.write(pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL))  => wrong, leads to RAM spike

def do_ungzip_pkl(fname: FilePath) -> Any | None:
    try:
        with gzip.open(fname, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print(e, fname)
        return None


def do_gzip_txt(txt: Any, fname: FilePath) -> None:
    with gzip.open(fname, "wt", encoding="utf-8") as f:
        f.write(txt)

def do_ungzip_txt(fname: FilePath) -> str | None:
    try:
        with gzip.open(fname, "rt", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(e, fname)
        return None

def do_zip_extract(zip_fname: FilePath, dest_path: FilePathOrNone = None, 
                   fname_filter: FilePathOrNone = None) -> list[str]:
    extracted_files: list[str] = []
    with zipfile.ZipFile(zip_fname, "r") as zipf:
        for fname in zipf.namelist():
            if fname_filter and fname not in fname_filter:
                continue
            zipf.extract(fname, path=dest_path)
            extracted_files.append(f"{dest_path}/{fname}" if dest_path else fname)
    
    return extracted_files

def get_c01_from_cell(cell: str) -> tuple[str, str]:
    # Splits 'AB' into 'A' and 'B, and 'cA' into '_c' and 'A'
    c0 = cell[0] if cell[0] < 'a' else f"_{cell[0]}"
    c1 = cell[1] if cell[1] < 'a' else f"_{cell[1]}"
    return c0, c1

### TAG analyzer - determine next version filename
def get_tagcnt_dict_fnames(kw: str, data_base_path: FilePath) -> list[FilePath]:
    # Filter files in specified direcory by keyword (kw) in file name
    return sorted([f for f in os.listdir(os.path.join(data_base_path, "lvl1")) if f.startswith(kw)])

def extract_tagcnt_version_num(fname: FilePath) -> int:
    # return a version number from a file name like "COND_TAGCNT_DICT_v0003.gzip" -> returns 3
    #print(fname)
    try:
        v_str = fname.split(".")[0].split("_")[-1]
        v_num = int(v_str[1:])
    except Exception as e:
        print(e)
        return 0
    
    return v_num

def get_next_version_fname(kw: str, data_base_path: FilePath) -> str:
    # Bumps the version number of a file name by 1, e.g. "COND_TAGCNT_DICT_v0003.gzip" => "COND_TAGCNT_DICT_v0004.gzip"
    fnames = get_tagcnt_dict_fnames(kw, data_base_path)

    if not fnames:
            return f"{kw}_v0001.gzip"
    
    curr_version_num = extract_tagcnt_version_num(fnames[-1])
    return f"{kw}_v{curr_version_num + 1:04d}.gzip" 

# Check subfolders in Level directories
def get_act_dir_list(d: str, lvl: str | int, data_base_path: str) -> bool:
    return os.path.exists(os.path.join(data_base_path, lvl, d))
    # Alt solution with Path
    # return (data_base_path / str(lvl) / d).exists()

