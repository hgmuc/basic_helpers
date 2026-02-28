import pytest
import os
from unittest.mock import patch, MagicMock

# We mock the dependency BEFORE importing config because config.py 
# executes do_gzip_pkl at the top level upon import.
with patch('basic_helpers.file_helper.do_gzip_pkl') as mock_gzip:
    import basic_helpers.config as config
    import basic_helpers.config_obs as config_obs
    import basic_helpers.config_elev as config_elev

def test_data_paths_are_strings():
    """Verify that path configurations are correctly typed."""
    assert isinstance(config.data_base_path, str) and len(config.data_base_path) > 0
    assert isinstance(config.BIKESITE_CSV_PATH, str) and len(config.BIKESITE_CSV_PATH) > 0

def test_binnen_regions_not_empty():
    """Ensure the regions list is populated and contains expected keys."""
    assert len(config.BINNEN_REGIONS) > 0
    assert 'DE-BY' in config.BINNEN_REGIONS
    assert 'AT' in config.BINNEN_REGIONS

def test_country_map_integrity():
    """Validate the mapping logic for country codes."""
    # Check if critical mappings exist
    assert config.FNAME_ADMIN_CTRY_MAP['DE-BY'] == 'DE'
    assert config.FNAME_ADMIN_CTRY_MAP['SW'] == 'SE'
    
    # Logic check: No empty keys or values
    for key, value in config.FNAME_ADMIN_CTRY_MAP.items():
        assert len(key) >= 2, f"Key {key} is too short"
        assert len(value) == 2, f"Value {value} must be a 2-letter ISO code"

def test_included_ftwys_is_set_of_ints():
    """Verify the footway ID collection is properly formatted."""
    assert isinstance(config.INCLUDED_FTWYS, set)
    assert all(isinstance(i, int) for i in config.INCLUDED_FTWYS)
    # Check a specific known ID from the list
    assert 31512448 in config.INCLUDED_FTWYS

@patch('basic_helpers.file_helper.do_gzip_pkl')
def test_config_execution_logic(mock_do_gzip):
    """
    Since we can't easily 're-import' the module to trigger the try-except,
    we verify how it would handle the gzip call if called manually 
    or check the state of the initial mock.
    """
    # Verify that the module attempted to save the PKL file on load
    # Note: This checks the mock created in the global scope of this file
    assert mock_gzip.called
    args, _ = mock_gzip.call_args
    assert args[0] == config.INCLUDED_FTWYS
    assert "INCLUDED_FTWYS.gzip" in args[1]

def test_config_obs_params():
    assert config_obs.PIPELINE_VERSION >= 1
    assert config_obs.OBS_MODE == 'db'

def test_config_elev_params():
    assert isinstance(config_elev.ELEV_DATA_PATH, str) and len(config_elev.ELEV_DATA_PATH) >= 10
    assert isinstance(config_elev.SRTM_DATA_PATH, str) and len(config_elev.SRTM_DATA_PATH) >= 8
    assert isinstance(config_elev.ASTER_DATA_PATH, str) and len(config_elev.ASTER_DATA_PATH) >= 10

