import pytest
import numpy as np
from shapely.geometry import Polygon, GeometryCollection
from basic_helpers.config_reg_code import (
    az_bbox, base_bbox, mapped_region, 
    TOTAL_CELLS, BASE_CELLS, LATLON_CELL_PARAMS,
    CellParams
)

def test_bbox_coordinates_logic():
    """Verify that all bounding boxes follow (min_lon, min_lat, max_lon, max_lat)."""
    bboxes = [az_bbox, base_bbox] # Add others as needed
    for bbox in bboxes:
        assert bbox[0] < bbox[2], f"min_lon {bbox[0]} should be less than max_lon {bbox[2]}"
        assert bbox[1] < bbox[3], f"min_lat {bbox[1]} should be less than max_lat {bbox[3]}"

def test_mapped_region_composition():
    """Ensure the mapped_region is a GeometryCollection containing Polygons."""
    assert isinstance(mapped_region, GeometryCollection)
    assert len(mapped_region.geoms) > 0
    for geom in mapped_region.geoms:
        assert isinstance(geom, Polygon)
        assert not geom.is_empty

def test_cell_sets_integrity():
    """Verify that cell sets are populated and the total set is a union of parts."""
    assert len(BASE_CELLS) > 0
    assert len(TOTAL_CELLS) >= len(BASE_CELLS)
    
    # Check a known coordinate in the base area
    # base_bbox: (-11, 36, 45, 72) -> (lat, lon)
    assert (36, -11) in BASE_CELLS
    assert (36, -11) in TOTAL_CELLS

def test_latlon_cell_params_structure():
    """Verify that LATLON_CELL_PARAMS strictly adheres to the CellParams TypedDict."""
    required_keys = {
        'x1', 'x2', 'x3', 'y1', 'y2', 'y3', 
        'extent_lon', 'extent_lat', 'n_lttr1', 'n_lttr2', 'off1', 'off2'
    }
    
    for region, params in LATLON_CELL_PARAMS.items():
        # Check all keys exist
        assert set(params.keys()) == required_keys, f"Missing or extra keys in {region}"
        
        # Check specific types for x1/y1 (allowing int, float, or np.float32)
        assert isinstance(params['x1'], (int, float, np.float32))
        assert isinstance(params['y1'], (int, float, np.float32))
        
        # Check integer fields
        int_fields = ['x2', 'x3', 'y2', 'y3', 'extent_lon', 'extent_lat', 'n_lttr1', 'n_lttr2']
        for field in int_fields:
            assert isinstance(params[field], int), f"Field {field} in {region} must be int"

@pytest.mark.parametrize("region_name", ["base", "azores", "canary"])
def test_specific_region_config_exists(region_name):
    """Ensure critical regions are defined in the config dictionary."""
    assert region_name in LATLON_CELL_PARAMS

