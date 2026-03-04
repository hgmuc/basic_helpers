from typing import get_type_hints
from shapely.geometry import Point
from basic_helpers.typed_dict_classes import TourismAreaTagsDict

# Note: We import BaseGeometry to verify the 'geom' field type
from shapely.geometry.base import BaseGeometry

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