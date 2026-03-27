from typing import get_type_hints, get_args, cast
from shapely.geometry import Point
from basic_helpers.typed_dict_classes import TourismAreaTagsDict, Code2AdminIdsDict
from basic_helpers.types_lvl1 import Code2AdminRegCodeData, Code2AdminDict
from basic_helpers.types_osm import SpecialKey
from basic_helpers.types_base import OsmAdminId

# Note: We import BaseGeometry to verify the 'geom' field type
from shapely.geometry.base import BaseGeometry


def test_code2_admin_ids_dict_structure():
    """Verify the TypedDict has the expected keys and required types."""
    hints = get_type_hints(Code2AdminIdsDict)
    
    # Check all ADM levels from 4 to 10 are present
    expected_levels = [f"adm{i}" for i in range(4, 11)]
    for level in expected_levels:
        assert level in hints
        # Verify the hint is a dict (or mapping)
        assert "dict" in str(hints[level]).lower()

def test_code2_admin_ids_dict_instantiation():
    """Test valid instantiation of the TypedDict with sample data."""
    # Sample data conforming to: tuple[name, name_de, name_en, code, set[RegCode]]
    sample_entry = (
        "Yerevan",      # name
        "Jerewan",      # name_de
        "Yerevan",      # name_en
        "AM-ER",        # code
        {"AM31", "AM3"} # RegCode set
    )
    
    data: Code2AdminIdsDict = {
        "adm4": {123456: sample_entry},
        "adm5": {},
        "adm6": {},
        "adm7": {},
        "adm8": {},
        "adm9": {},
        "adm10": {}
    }
    
    assert isinstance(data, dict)
    assert data["adm4"][123456][0] == "Yerevan"
    assert "AM31" in data["adm4"][123456][4]

def test_typed_dict_completeness():
    """Ensure that a dict missing a key would fail if checked by a type checker."""
    # In Python 3.10, TypedDict keys are required by default unless 'total=False' is set.
    # We verify here that our logic expects all keys.
    data = {
        "adm4": {},
        "adm5": {},
        "adm6": {},
        "adm7": {},
        "adm8": {},
        "adm9": {}
        # missing adm10
    }
    
    # Note: Runtime Python doesn't throw an error on instantiation, 
    # but we can check the set of keys against the class definition.
    required_keys = set(Code2AdminIdsDict.__annotations__.keys())
    provided_keys = set(data.keys())
    
    assert "adm10" in required_keys
    assert "adm10" not in provided_keys

def test_code2admin_dict_composition():
    """Verify Code2AdminDict can hold both Admin ID metadata and RegCode mappings."""
    
    # 1. Setup the "ids" content (Code2AdminIdsDict)
    admin_metadata: Code2AdminIdsDict = {
        "adm4": {100: ("Region A", None, None, "A1", {"AM31"})},
        "adm5": {}, "adm6": {}, "adm7": {}, "adm8": {}, "adm9": {}, "adm10": {}
    }
    
    # 2. Setup a RegCode entry (Code2AdminRegCodeData)
    # This maps a RegCode back to specific OsmAdminIds per level
    reg_code_mapping: Code2AdminRegCodeData = {
        "adm4": [100],
        "adm5": []
    }
    
    # 3. Create the main dictionary
    # "ids" is a SpecialKey; "AM31" is a RegCode
    combined_data: Code2AdminDict = {
        "ids": admin_metadata,
        "AM31": reg_code_mapping
    }
    
    ids_data = cast(Code2AdminIdsDict, combined_data["ids"])

    assert "ids" in combined_data
    assert "AM31" in combined_data
    assert ids_data["adm4"][100][0] == "Region A"
    assert 100 in combined_data["AM31"]["adm4"]

def test_special_keys_literals():
    """Ensure all defined SpecialKeys are valid keys in the structure."""
    
    allowed_keys = get_args(SpecialKey)
    assert "ids" in allowed_keys
    assert "cells" in allowed_keys
    assert "bbox" in allowed_keys
    assert -1 in allowed_keys

def test_cross_reference_integrity():
    """
    Logic test: Ensure IDs found in a RegCode entry actually 
    exist in the 'ids' metadata storage.
    """
    sample_id: OsmAdminId = 555
    reg_code = "AM3"
    
    data: Code2AdminDict = {
        "ids": {
            "adm4": {sample_id: ("Test", None, None, None, {reg_code})},
            "adm5": {}, "adm6": {}, "adm7": {}, "adm8": {}, "adm9": {}, "adm10": {}
        },
        reg_code: {
            "adm4": [sample_id]
        }
    }
    
    # 2. Alternatively, use an assertion to narrow the type
    ids_branch = data["ids"]
    assert isinstance(ids_branch, dict)

    # Verify the ID in the RegCode lookup exists in the 'ids' metadata
    ids_data = cast(Code2AdminIdsDict, ids_branch)
    lookup_id = cast(Code2AdminRegCodeData, data[reg_code])["adm4"][0]
    metadata_tuple = ids_data["adm4"][lookup_id]

    assert lookup_id in data["ids"]["adm4"]
    # Verify the RegCode is listed in that ID's metadata set
    assert reg_code in metadata_tuple[4]


def test_tourism_area_tags_dict_structure():
    """
    Test that the TypedDict has the expected keys and that the 
    runtime type hints match our definition.
    """
    hints = get_type_hints(TourismAreaTagsDict)
    
    # Test specific key existence
    assert "id" in hints
    assert "is_bicycle_charging_station" in hints
    assert "geom" in hints
    assert "wh" in hints
    assert "heritage:operator" in hints

    # Test type assignments
    assert hints["is_bicycle_charging_station"] is bool
    assert hints["wh"] == tuple[int, int]
    assert hints["ntype"] is str
    # Check if geom is a subclass/type of BaseGeometry
    assert hints["geom"] is BaseGeometry

def test_tourism_area_tags_dict_instantiation():
    """
    Test that a dictionary following the TypedDict structure can be 
    instantiated without errors.
    """
    # Mocking external types for the sake of the test data
    sample_bbox = (10.0, 20.0, 11.0, 21.0) # Assuming BBox is a tuple or similar
    sample_geom = Point(0, 0)
    
    data: TourismAreaTagsDict = {
        "id": 123456,
        "ntype": "way",
        "tourism": "museum",
        "is_bicycle_charging_station": True,
        "name": "Old Town Museum",
        "heritage:operator": "UNESCO",
        "bbox": sample_bbox,
        "geom": sample_geom,
        "wh": (1024, 768)
    }
    
    assert data["name"] == "Old Town Museum"
    assert data["is_bicycle_charging_station"] is True
    assert isinstance(data["wh"], tuple)
    assert isinstance(data["geom"], BaseGeometry)
    assert data["wh"][0] == 1024

def test_optional_keys():
    """
    Since total=False, verify we can create an empty or partial dict.
    """
    data: TourismAreaTagsDict = {"id": 999}
    assert "id" in data
    assert "name" not in data