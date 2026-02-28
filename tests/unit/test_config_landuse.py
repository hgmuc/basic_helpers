# tests/unit/test_config_landuse.py

import pytest
from basic_helpers import config_landuse

#class TestLanduseConfig:
#    """Test suite for landuse configuration constants."""

def test_landuse_water_types():
    """Verify WATER_TYPES set contents and type."""
    assert isinstance(config_landuse.LANDUSE_WATER_TYPES, set)
    assert "reservoir" in config_landuse.LANDUSE_WATER_TYPES
    assert len(config_landuse.LANDUSE_WATER_TYPES) == 4

def test_industrial_types():
    """Verify INDUSTRIAL_TYPES set contents and type."""
    assert isinstance(config_landuse.INDUSTRIAL_TYPES, set)
    assert "quarry" in config_landuse.INDUSTRIAL_TYPES
    assert "wastewater_plant" in config_landuse.INDUSTRIAL_TYPES
    assert len(config_landuse.INDUSTRIAL_TYPES) == 20

def test_plantation_and_farmland():
    """Verify agricultural related types."""
    assert "vineyard" in config_landuse.PLANTATION_TYPES
    assert len(config_landuse.PLANTATION_TYPES) == 6
    
    assert "paddy" in config_landuse.FARMLAND_TYPES
    assert len(config_landuse.FARMLAND_TYPES) == 8

def test_meadows_types():
    """Verify MEADOWS_TYPES and check for the specific 'natural␣reserve' typo/string."""
    assert "meadow" in config_landuse.MEADOWS_TYPES
    # Testing for the specific string with the visible space character provided in snippet
    assert "natural␣reserve" in config_landuse.MEADOWS_TYPES
    assert len(config_landuse.MEADOWS_TYPES) == 14

def test_forest_and_geology():
    """Verify forest and geological features."""
    assert "timber" in config_landuse.FOREST_TYPES
    assert len(config_landuse.FOREST_TYPES) == 5
    
    assert "volcano" in config_landuse.GEOLOGY_TYPES
    assert "glacier" in config_landuse.GEOLOGY_TYPES
    assert len(config_landuse.GEOLOGY_TYPES) == 27

def test_public_infrastructure():
    """Verify public buildings and infrastructure sets."""
    assert "religious" in config_landuse.PUBLIC_BUILDINGS
    assert len(config_landuse.PUBLIC_BUILDINGS) == 11
    
    assert "traffic_island" in config_landuse.PUBL_INFRASTRUCTURE
    assert len(config_landuse.PUBL_INFRASTRUCTURE) == 5

def test_park_lists_and_sets():
    """Verify park related lists and sets."""
    assert isinstance(config_landuse.PARK_TYPES, set)
    assert "golf_course" in config_landuse.PARK_TYPES
    
    assert isinstance(config_landuse.NATIONAL_PARK_TYPES, list)
    assert "national_park" in config_landuse.NATIONAL_PARK_TYPES
    
    assert "recreation_ground" in config_landuse.LANDUSE_TOURISM_TYPES

    assert len(config_landuse.PARK_TYPES) == 5
    assert len(config_landuse.NATIONAL_PARK_TYPES) == 2
    assert len(config_landuse.LANDUSE_TOURISM_TYPES) == 1

def test_natural_mapping():
    """Verify the dictionary mapping logic."""
    mapping = config_landuse.NATURAL_MAPPING
    assert isinstance(mapping, dict)
    
    # Check specific mappings
    assert mapping['scrub'] == 'forest'
    assert mapping['beach'] == 'water'
    assert mapping['tundra'] == 'forest'
    assert mapping['grassland'] == 'meadows'
    
    # Check total count (7 initial + 2 added later in module)
    assert len(mapping) == 9

@pytest.mark.parametrize("const_name", [
    "LANDUSE_WATER_TYPES", "INDUSTRIAL_TYPES", "PLANTATION_TYPES",
    "FARMLAND_TYPES", "MEADOWS_TYPES", "FOREST_TYPES", "GEOLOGY_TYPES",
    "PUBLIC_BUILDINGS", "PUBL_INFRASTRUCTURE", "PARK_TYPES"
])
def test_constants_are_not_empty(const_name):
    """Generic check to ensure no set was accidentally cleared."""
    const_value = getattr(config_landuse, const_name)
    assert len(const_value) > 0


