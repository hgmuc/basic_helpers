import pytest
from basic_helpers.config_pbf import (
    fnames, 
    fname_list, 
    fname_admin_list, 
    fnames_cyr, 
    fnames_el, 
    upd_packages, 
    ext_fnames, 
    ext_fnames2,
    ext_fnames3,
    excl_fnames,
    ext_fnames_admin, 
    fnames_translit
)

def test_fnames_structure():
    """Verify fnames contains expected keys and valid file extensions."""
    assert isinstance(fnames, dict)
    assert len(fnames) == 173
    assert "DE-BW" in fnames
    assert fnames["DE-BW"] == "baden-wuerttemberg-latest.osm.pbf"
    
    # All values should be strings ending in .pbf, .osm, or .bz2
    for val in fnames.values():
        assert isinstance(val, str)
        assert val.endswith((".pbf", ".osm", ".bz2", ".osm.pbf"))

def test_fname_list_filtering():
    """Verify fname_list correctly excludes items defined in exclusion lists."""
    # Based on the logic: if n not in ext_fnames + ext_fnames2 + ... + excl_fnames
    for key in excl_fnames:
        assert key not in fname_list, f"{key} should have been excluded from fname_list"
    
    for key in ext_fnames:
        assert key not in fname_list, f"{key} (external) should have been excluded from fname_list"

    for key in ext_fnames2:
        assert key not in fname_list, f"{key} (external) should have been excluded from fname_list"

    for key in ext_fnames3:
        assert key not in fname_list, f"{key} (external) should have been excluded from fname_list"

    for key in ext_fnames_admin:
        assert key not in fname_list, f"{key} (external) should have been excluded from fname_list"

    assert len(fname_list) == 105
    assert len(excl_fnames) == 32
    assert len(ext_fnames) == 20
    assert len(ext_fnames2) == 5
    assert len(ext_fnames3) == 7
    assert len(ext_fnames_admin) == 20

def test_fname_admin_list_content():
    """Verify specific required keys are in the admin list."""
    assert len(fname_admin_list) == 172
    assert "HR" in fname_admin_list
    assert "RS" in fname_admin_list
    # OBB and BAY are explicitly excluded in the list comprehension logic
    assert "OBB" not in fname_admin_list
    assert "BAY" not in fname_admin_list

def test_upd_packages_type_integrity():
    """Verify the structure of UpdatePkgs type alias."""
    assert len(upd_packages) == 6
    for idx, pkg in upd_packages.items():
        assert len(pkg) > 10

    assert isinstance(upd_packages, dict)
    for group_id, pkg_map in upd_packages.items():
        assert isinstance(group_id, int)
        assert isinstance(pkg_map, dict)
        for key, value in pkg_map.items():
            assert isinstance(key, str)
            assert isinstance(value, str)

def test_translit_consistency():
    """Ensure Greek and Cyrillic keys are bundled in translit."""
    assert len(fnames_cyr) == 16
    assert len(fnames_el) == 4
    assert len(fnames_translit) == 24
    assert "GR" in fnames_translit  # From fnames_el
    assert "RU" in fnames_translit  # From fnames_cyr
    assert "ARM" in fnames_translit # Manually added

    for c in fnames_cyr:
        assert c in fnames_translit

    for c in fnames_el:
        assert c in fnames_translit

@pytest.mark.parametrize("key", ["DE-BW", "AT", "CH", "NL-ZH"])
def test_rel_keys_presence(key):
    """Check that specific neighboring regions are in REL_KEYS."""
    from basic_helpers.config_pbf import REL_KEYS
    assert key in REL_KEYS

def test_no_empty_values():
    """Ensure no keys in fnames have empty string values."""
    for key, path in fnames.items():
        assert path.strip() != "", f"Empty path for key: {key}"

