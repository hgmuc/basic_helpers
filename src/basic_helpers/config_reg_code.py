import numpy as np
from itertools import product
from shapely.geometry import box, GeometryCollection, Polygon
from typing import Sequence, Union, List, Tuple, TypedDict, Dict, Set

BBox = Tuple[int, int, int, int]
Coordinate = Tuple[int, int]

# Define the structure of the inner dictionary
class CellParams(TypedDict):
    x1: Union[int, float, np.float32]
    x2: int
    x3: int
    y1: Union[int, float, np.float32]
    y2: int
    y3: int
    extent_lon: int
    extent_lat: int
    n_lttr1: int
    n_lttr2: int
    off1: int
    off2: int


# min_lon, min_lat, max_lon, max_lat
az_bbox: BBox = (-32, 36, -24, 40)
base_bbox: BBox = (-11, 36, 45, 72)
isl_bbox: BBox = (-26, 63, -12, 68)
mad_bbox: BBox = (-18, 32, -16, 34)
can_bbox: BBox = (-19, 26, -12, 31)
cpv_bbox: BBox = (-27, 14, -21, 19)
med_bbox: BBox = (-7, 34, 45, 36)

az: Polygon = box(*az_bbox)
base: Polygon = box(*base_bbox)
isl: Polygon = box(*isl_bbox)
mad: Polygon = box(*mad_bbox)
can: Polygon = box(*can_bbox)
cpv: Polygon = box(*cpv_bbox)
med: Polygon = box(*med_bbox)
mapped_region: GeometryCollection = GeometryCollection([az, cpv, mad, isl, med, can, base])


BASE_CELLS_LIST: List[Coordinate] = [(lat, lon) for lat, lon in 
                                         product(range(base_bbox[1], base_bbox[3]), 
                                                 range(base_bbox[0], base_bbox[2]+1), repeat=1)]
AZOR_CELLS_LIST: List[Coordinate] = [(lat, lon) for lat, lon in 
                                         product(range(az_bbox[1], az_bbox[3]), 
                                                 range(az_bbox[0], az_bbox[2]+1), repeat=1)]
MADE_CELLS_LIST: List[Coordinate] = [(lat, lon) for lat, lon in 
                                         product(range(mad_bbox[1], mad_bbox[3]), 
                                                 range(mad_bbox[0], mad_bbox[2]+1), repeat=1)]
CANA_CELLS_LIST: List[Coordinate] = [(lat, lon) for lat, lon in 
                                         product(range(can_bbox[1], can_bbox[3]), 
                                                 range(can_bbox[0], can_bbox[2]+1), repeat=1)]
CABO_CELLS_LIST: List[Coordinate] = [(lat, lon) for lat, lon in 
                                         product(range(cpv_bbox[1], cpv_bbox[3]), 
                                                 range(cpv_bbox[0], cpv_bbox[2]+1), repeat=1)]
ICEL_CELLS_LIST: List[Coordinate] = [(lat, lon) for lat, lon in 
                                         product(range(isl_bbox[1], isl_bbox[3]), 
                                                 range(isl_bbox[0], isl_bbox[2]+1), repeat=1)]
MEDI_CELLS_LIST: List[Coordinate] = [(lat, lon) for lat, lon in 
                                         product(range(med_bbox[1], med_bbox[3]), 
                                                 range(med_bbox[0], med_bbox[2]+1), repeat=1)]

TOTAL_CELLS: Set[Coordinate] = set(BASE_CELLS_LIST + AZOR_CELLS_LIST + MADE_CELLS_LIST + CANA_CELLS_LIST + 
                                   CABO_CELLS_LIST+ ICEL_CELLS_LIST + MEDI_CELLS_LIST)
BASE_CELLS: Set[Coordinate] = set(BASE_CELLS_LIST)
AZOR_CELLS: Set[Coordinate] = set(AZOR_CELLS_LIST)
MADE_CELLS: Set[Coordinate] = set(MADE_CELLS_LIST)
CANA_CELLS: Set[Coordinate] = set(CANA_CELLS_LIST)
CABO_CELLS: Set[Coordinate] = set(CABO_CELLS_LIST)
ICEL_CELLS: Set[Coordinate] = set(ICEL_CELLS_LIST)
MEDI_CELLS: Set[Coordinate] = set(MEDI_CELLS_LIST)

LATLON_CELL_PARAMS: Dict[str, CellParams] = {
    'base': {'x1': 2, 'x2': 3, 'x3': 9, 'y1': 3, 'y2': 3, 'y3': 9, 
                'extent_lon': 1, 'extent_lat': 1, 
                'n_lttr1': 2, 'n_lttr2': 3, 'off1': 1, 'off2': 1},
    'madeira': {'x1': 3, 'x2': 3, 'x3': 9, 'y1': 3, 'y2': 3, 'y3': 9, 
                'extent_lon': mad_bbox[2]-mad_bbox[0], 'extent_lat': mad_bbox[3]-mad_bbox[1], 
                'n_lttr1': 6, 'n_lttr2': 3, 'off1': 0, 'off2': 0},
    'canary': {'x1': 1, 'x2': 7, 'x3': 9, 'y1': 1, 'y2': 8, 'y3': 9, 
                'extent_lon': can_bbox[2]-can_bbox[0], 'extent_lat': can_bbox[3]-can_bbox[1], 
                'n_lttr1': 7, 'n_lttr2': 7, 'off1': 0, 'off2': 0},
    'caboverde': {'x1': np.float32(8/6), 'x2': 6, 'x3': 9, 'y1': np.float32(7/5), 'y2': 6, 'y3': 9, 
                'extent_lon': cpv_bbox[2]-cpv_bbox[0], 'extent_lat': cpv_bbox[3]-cpv_bbox[1], 
                'n_lttr1': 8, 'n_lttr2': 6, 'off1': 0, 'off2': 0},
    'iceland': {'x1': np.float32(1.5), 'x2': 3, 'x3': 9, 'y1': 3, 'y2': 3, 'y3': 9, 
                'extent_lon': 4, 'extent_lat': 1, 
                'n_lttr1': 6, 'n_lttr2': 3, 'off1': 0, 'off2': 0},
    'azores': {'x1': 1, 'x2': 6, 'x3': 9, 'y1': np.float32(1.5), 'y2': 6, 'y3': 9, 
                'extent_lon': az_bbox[2]-az_bbox[0], 'extent_lat': az_bbox[3]-az_bbox[1], 
                'n_lttr1': 8, 'n_lttr2': 6, 'off1': 0, 'off2': 0},
}
