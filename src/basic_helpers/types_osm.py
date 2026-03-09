from __future__ import annotations
import numpy as np
from shapely.geometry.base import BaseGeometry
from typing import Literal, Union, Dict, Tuple, List, TypedDict, Any, TypeAlias
from .config_pbf import FnamesValid
from .types_base import FlexNumeric, BBoxInt, TagVal
from .types_base import OsmNodeId, OsmWayId, OsmRelatId, OsmAreaId
#from .config_reg_code import BBoxInt, BBox
#from osmium import Node, Way, Relation, Area


OsmNodesList = List[List[Union[float, np.floating]]]

OsmHighway = Literal['bridleway', 'bus_stop', 'construction', 'corridor', 'crossing', 'cycleway', 'elevator', 
                      'emergency_bay', 'escape', 'ferry', 'footway', 'ladder', 'living_street', 'motorway', 
                      'motorway_link', 'path', 'pedestrian', 'platform', 'primary', 'primary_link', 'proposed', 
                      'raceway', 'razed', 'residential', 'rest_area', 'road', 'secondary', 'secondary_link', 'service', 
                      'services', 'shuttle_bus', 'shuttle_train', 'steps', 'tertiary', 'tertiary_link', 'track', 'trail', 
                      'trunk', 'trunk_link', 'unclassified', 'via_ferrata', 'parking_aisle', 'driveway']

OsmAccess = Literal['Yes', 'bwd', 'construction', 'customers', 'customers;private', 'customer', 'delivery', 'designated', 
                    'destination', 'discouraged', 'emergency', 'employees', 'forestry', 'fwd', 'impassable', 
                    'limited', 'military', 'no', 'official', 'passable', 'permissive', 'private', 'private;customers', 
                    'students', 'use_sidepath', 'yes', 'allowed']

OsmMtbScale = Literal['0', '0+', '0-', '1', '1+', '1-', '2', '2+', '2-', '3', '3+', '3-', 
                      '4', '4+', '4-', '5', '5+', '5-', '6', '6+', '6-', 0, 1, 2, 3, 4, 5, 6
                      ]
OsmMtbScaleSVal = Literal['s0', 's1', 's2', 's3', 's4', 's5', 's6']

OsmLocalityTag = Literal['allotment', 'archipelago', 'borough', 'city', 'city_block', 'farm', 
                         'hamlet', 'island', 'islet', 'isolated_dwelling', 'locality', 'municipality', 
                         'neighbourhood', 'plot', 'quarter', 'square', 'suburb', 'town', 'village']

OsmSmoothness = Literal['average', 'bad', 'bon', 'catastrophic', 'excelent', 'excellent', 'fair', 'fine', 
                        'good', 'grass', 'high_clearance', 'horrible', 'impassable', 'intermediate', 'mediocre', 
                        'medium', 'moderate', 'moyen', 'off_road_wheels', 'ok', 'p', 'perfect', 'poor', 'reasonable', 
                        'robust_wheels', 'rough', 'smooth', 'specialized_off_road_wheels', 'terrible', 'thin_rollers', 
                        'thin_wheels', 'uneven', 'unpaved', 'very_bad', 'very bad', 'very_good', 'very_horrible', 
                        'very horrible', 'yes']

OsmTrailVisibility = Literal['bad', 'check', 'excellent', 'excellent/good', 'exellent', 'fair', 'good', 'gut', 
                          'horrible', 'intermediate', 'intermittant', 'intermittent', 'medium', 'moderate', 
                          'no', 'none', 'ok', 'terrible', 'very_bad', 'very_good', 'very_horrible', 'y', 'yes']



OsmBridgeLayers = Literal[1,2,3,4,5,'1','2','3','4','5','+1','+2','+3','+4','+5']

BicycleRestrictions = Literal['dismount', 'separate', 'use_sidepath', 'share_sidewalk']
ExtraAccess = Literal['agriforest']
ExtraHighways = Literal['ftwy', 'crossing', 'train', 'bus']
LiftHighways = Literal['gondola', 'funicular', 'chair_lift', 'zip_line', 'mixed_lift', 'cable_car']

HikeSurface = Literal['asphalt', 'forest_soil', 'grass', 'gravel/sand', 'ground/dirt', 'ground/dirt/grass', 'ground/grass', 
                      'ground/gravel', 'ground/rocks', 'ground/roots', 'metal', 'paved/concrete', 'plastic/rubber', 'rocks', 
                      'rubble', 'salt', 'scrub', 'snow/ice', 'stone/cobblestone', 'timber', 'wood', 'rock', 'other/unknown']

RoadSurface = Literal['asphalt', 'gravel/sand', 'ground/dirt/grass', 'metal', 'paved/concrete', 'plastic/rubber', 'rocks', 
                      'rubble', 'scrub', 'stone/cobblestone', 'timber', 'wood', 'rock', 'other/unknown']
Quality = Literal[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 28, 29, 
                  30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 44, 45, 46, 49, 50, 51, 52, 55, 56, 59, 
                  60, 66, 69, 70, 80, 90, 91, 92, 95, 96, 97, 
                  100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 
                  110, 112, 115, 118, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 
                  130, 131, 132, 135, 136, 140, 141, 142, 143, 150, 155, 156, 157, 158, 159,
                  190, 197, 198, 199, 999 
                  ]

ValidSmoothness = Literal['bad', 'excellent', 'good', 'horrible', 'impassable', 'intermediate', 'very_bad', 'very_good', 'very_horrible']

CellOsmWayId = str
CellOsmAreaId = str
CellOsmRelatId = str

SubcellKey = Literal['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', 
                     '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', 
                     '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', 
                     '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', 
                     '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', 
                     '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', 
                     '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', 
                     '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', 
                     '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', 
                     '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']

SpecialKey = Literal["cells", "bbox", -1]
CellKey = str

SurfaceDictType = dict[str, RoadSurface | HikeSurface]

tagset_id = int
name = str | None
name_de = str | None
name_en = str | None
lat: TypeAlias = int | float | np.floating
lon: TypeAlias = int | float | np.floating
addr_city = str | None
wikipedia = str | None
website = str | None
description = str | None
heritage = str | None
radius = float | None


Role = str | None

railway_type = str
waterway_type = str
highway_type = str
is_tunnel = bool
is_bridge = bool
is_intermittent = bool

WaterwayRelatType = tuple[waterway_type, name, name_de, OsmRelatId] | tuple[waterway_type, name, name_de, OsmRelatId, Role]

lanes = int | str | None
maxspeed = int | str | None
oneway = str | None
scenic = str | None
scenic_road_ids = list[int]


WghtFct: TypeAlias = float | np.floating
#AreaTagsDict = Dict[str, Union[OsmAreaId | TagVal | BBox | int | tuple[int, int] | BaseGeometry | MultiPolygon]]

PeakTS = tuple[Literal['peak']] | tuple[Literal['peak'], str, str]
LocPlaceTS = tuple[Literal['locality'], Literal['place'], str]
VolcanoTS = tuple[Literal['volcano'], str | None, str | None]
MtnPassTS = tuple[Literal['mountain_pass'], Literal['mountain_pass'], Literal['mountain_pass']]
BarrierTS = tuple[Literal['barrier_node'], Literal['barrier'], str | None, int, int]

#LocFerryTS = tuple[Literal['locality'], Literal['ferry'], str | None, str | None, str | None, str | None]
LocFerryTS = tuple[Literal['locality'], Literal['ferry'], Literal['ferry_terminal'], TagVal, TagVal, TagVal]
#LocRailwayTS = tuple[Literal['locality'], Literal['railway'], str | None, str | None, str | None, str | None]
LocRailwayTS = tuple[Literal['locality'], Literal['railway'], TagVal, Literal['yes', 'no'], TagVal, TagVal]

TourismTypeTS = tuple[Literal['tourism'], Literal['tourism_type'], str | None, str | None, str | None, str | None]
TourismBuildingTS = tuple[Literal['tourism'], Literal['building_type'], str | None, str | None, str | None, str | None]
TourismHistoricTS = tuple[Literal['tourism'], Literal['historic_type'], str | None, str | None, str | None, str | None]
TourismAmenityTS = tuple[Literal['tourism'], Literal['amenity_type'], str | None, str | None, str | None, str | None, str | None]
TourismParkingTS = tuple[Literal['tourism'], Literal['parking'], str | None, str | None, str | None, str | None, str | None]
TourismBikeCharTS = tuple[Literal['tourism'], Literal['bicycle_charging'], str | None, str | None, str | None, str | None, str | None]
TourismBikeRentTS = tuple[Literal['tourism'], Literal['bicycle_rental'], str | None, str | None, str | None, str | None, str | None]
TourismSwimmingTS = tuple[Literal['tourism'], Literal['swimming'], str | None, str | None, str | None, str | None, str | None, str | None]


GuidepostTS = tuple[Literal['guidepost_node'], Literal['guidepost'], str | None, str | None, str | None, str | None, str | None, str | None]

TourismTagset = TourismTypeTS | TourismBuildingTS | TourismAmenityTS | TourismHistoricTS | TourismParkingTS | TourismBikeCharTS | TourismBikeRentTS | TourismSwimmingTS
NodesTagset = PeakTS | VolcanoTS | MtnPassTS | BarrierTS | LocPlaceTS | LocFerryTS | LocRailwayTS | GuidepostTS | TourismTagset
NodesTagsetId = int
WayTagset = tuple[Quality, OsmHighway, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, 
                  TagVal, TagVal, TagVal, TagVal, OsmAccess, TagVal, RoadSurface, TagVal, ValidSmoothness, TagVal, 
                  TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal]
WayTagsetId = int
CWTagset = tuple[TagVal, TagVal, TagVal, RoadSurface, ValidSmoothness, TagVal, TagVal, TagVal, TagVal, RoadSurface, 
                 ValidSmoothness, TagVal, TagVal, TagVal, TagVal, RoadSurface, ValidSmoothness, TagVal, TagVal, TagVal, 
                 TagVal, TagVal, TagVal, TagVal]
CWTagsetId = int
HikeTagset = tuple[Quality, Quality, TagVal, HikeSurface, ValidSmoothness, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, 
                   TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal]
HikeTagsetId = int
TagsetId = WayTagsetId | CWTagsetId | HikeTagsetId | NodesTagsetId | int
TagsetKey = NodesTagset | WayTagset | CWTagset | HikeTagset | Literal[-1]
# Generic code example with definition of TypeVars
TagsetDict = dict[TagsetKey, TagsetId]

RevTagsetDict = dict[TagsetId, TagsetKey]
RevHikeTagsetVals = tuple[
    Quality, Quality, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, TagVal, HikeSurface, ValidSmoothness, TagVal,
    TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal]


TagsetCombiId = int
TagsetCombiDict = dict[tuple[WayTagsetId, CWTagsetId] | Literal[-1], TagsetCombiId]
RevTagsetCombiVals = tuple[
    WayTagsetId, CWTagsetId, 
    WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct,
    Quality, OsmHighway, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal]
RevTagsetCombiDict = dict[TagsetCombiId, RevTagsetCombiVals]

EmptyCellStructDict = Dict[SpecialKey, Dict[CellKey, Dict[SubcellKey, set[int]]]]


WaysTuple = tuple[OsmNodeId, OsmNodeId, TagsetCombiId, HikeTagsetId, name, OsmNodesList]

class InnerData(TypedDict):
    """The innermost schema containing c, w, and n."""
    c: dict[FnamesValid, set[OsmWayId]]
    w: dict[OsmWayId, WaysTuple]
    n: dict[str, Any]  # Keep as Any or specific if n grows

#SubcellCDict = dict[Literal['c'], dict[FnamesValid, set[OsmWayId]]]
#SubcellWDict = dict[Literal['w'], dict[OsmWayId, WaysTuple]]
#SubcellNDict = dict[Literal['n'], dict]
#SubcellDataDict = dict[SubcellKey, dict[Literal['c', 'w', 'n'], dict[FnamesValid, set[OsmWayId]] | dict[OsmWayId, WaysTuple]]]
SubcellDataDict = dict[SubcellKey, InnerData]
CellDataDict = dict[CellKey, SubcellDataDict]

TourismNodesTuple = tuple[tagset_id, name, name_de, name_en, lat, lon, addr_city, wikipedia, website, description, heritage, radius]
TourismNodesDict = Dict[SpecialKey | int, Dict[CellKey, Dict[SubcellKey, set[int]]] | TourismNodesTuple]
TourismNodesObj = Union[TourismNodesDict, EmptyCellStructDict]

#         tourism_area_dict[id] = (name, name_de, name_en, addr_city, wikipedia, website, heritage, *tagset, poly)
TourismAreasTuple = tuple[name, name_de, name_en, addr_city, wikipedia, website, heritage, BaseGeometry]
TourismAreasDict = Dict[SpecialKey | int, 
                        list[set[tuple[OsmAreaId, FlexNumeric, FlexNumeric, 
                                       FlexNumeric, BBoxInt]]] | TourismAreasTuple]
#         tourism_area_dict[-1].append((id, w, h, poly_area_m2, bbox))



HighwaysTuple = tuple[highway_type, name, lanes, maxspeed, oneway, is_tunnel, scenic, scenic_road_ids, OsmNodesList]
HighwaysDict = Dict[SpecialKey | int, Dict[CellKey, Dict[SubcellKey, set[int]]] | HighwaysTuple]
HighwaysObj = Union[HighwaysDict, EmptyCellStructDict]

RailwaysTuple = tuple[railway_type, name, is_tunnel, is_bridge, OsmNodesList]
RailwaysDict = Dict[SpecialKey | int, Dict[CellKey, Dict[SubcellKey, set[int]]] | RailwaysTuple]
RailwaysObj = Union[RailwaysDict, EmptyCellStructDict]

WaterwaysTuple = tuple[waterway_type, name, name_de, is_tunnel, is_intermittent, OsmNodesList]
WaterwaysDict = Dict[SpecialKey | int, Dict[CellKey, Dict[SubcellKey, set[int]]] | WaterwaysTuple]
WaterwaysObj = Union[WaterwaysDict, EmptyCellStructDict]




CoastlineTuple = Tuple[name, OsmNodesList]


