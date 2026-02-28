import pytest
from basic_helpers.config_reg_keys import REG_KEYS, REV_REG_KEYS

def test_reg_keys_structure():
    """Verify that REG_KEYS contains the expected regions and required keys."""
    expected_regions = {'DACH', 'SUD', 'IBERIA', 'WNW', 'SCAN', 'OST', 'SUDEST'}
    assert set(REG_KEYS.keys()) == expected_regions
    
    for region, params in REG_KEYS.items():
        assert 'rows' in params
        assert 'cols' in params
        assert 'testrows' in params
        assert 'testcols' in params
        assert isinstance(params['rows'], str)
        assert isinstance(params['cols'], str)
        if region == 'SUDEST':
            assert 'extra' in params
            assert len(params['extra']) == 3

def test_rev_reg_keys_mapping():
    """Verify specific known mappings in the reverse lookup dictionary."""
    # Test a standard mapping from DACH (9D)
    assert REV_REG_KEYS['9D'] == 'DACH'
    
    # Test a mapping from IBERIA (00)
    assert REV_REG_KEYS['00'] == 'IBERIA'
    
    # Test the last character mapping of SCAN
    # rows: ...XYZ, cols: ...g
    assert REV_REG_KEYS['Zg'] == 'SCAN'

def test_extra_coordinates_mapping():
    """Verify that 'extra' coordinates (like in SUDEST) are correctly mapped."""
    # SUDEST has extra: [('6', 'i'), ('6', 'j'), ('6', 'k')]
    assert REV_REG_KEYS['6i'] == 'SUDEST'
    assert REV_REG_KEYS['6j'] == 'SUDEST'
    assert REV_REG_KEYS['6k'] == 'SUDEST'

def test_rev_reg_keys_completeness():
    """Verify the total count of REV_REG_KEYS matches the cross-product of REG_KEYS."""
    total_expected = 0
    for vals in REG_KEYS.values():
        product_size = len(vals['rows']) * len(vals['cols'])
        extra_size = len(vals.get('extra', []))
        total_expected += (product_size + extra_size)
    
    # Note: This check assumes no overlapping coordinates between regions
    assert len(REV_REG_KEYS) == total_expected

@pytest.mark.parametrize("coord,expected_region", [
    ("9D", "DACH"), ("01", "IBERIA"), ("00", "IBERIA"),
    ("10", "IBERIA"), ("20", "IBERIA"), ("30", "IBERIA"),
    ("S2", "WNW"), ("T1", "WNW"), ("6i", "SUDEST"),
    ("zt", "SUDEST"), ("zT", "SUD"), 
    ("yT", "SUD"), # Testing 'y' from rows and 'z' from cols? 
                   # Wait, SUD rows has 'yz' as string, so 'y' and 'z' are individual rows.
])
def test_specific_coordinates(coord, expected_region):
    """Data-driven check for specific coordinate lookups."""
    assert REV_REG_KEYS.get(coord) == expected_region

def test_invalid_coordinate():
    """Ensure a non-existent coordinate returns None from the dictionary."""
    assert REV_REG_KEYS.get("ZZZZ") is None
    assert REV_REG_KEYS.get("Zz") is None
    assert REV_REG_KEYS.get("yy") is None
