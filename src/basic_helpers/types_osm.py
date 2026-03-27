from __future__ import annotations
import numpy as np
from shapely.geometry.base import BaseGeometry
from typing import Literal, Union, Dict, Tuple, List, TypedDict, Any, TypeAlias
from .config_pbf import FnamesValid
from .types_base import FlexNumeric, BBoxInt, TagVal
from .types_base import OsmNodeId, OsmWayId, OsmRelatId, OsmAreaId
#from .config_reg_code import BBoxInt, BBox
#from osmium import Node, Way, Relation, Area


OsmNodesList: TypeAlias = List[List[Union[float, np.floating]]]

OsmHighway: TypeAlias = Literal['bridleway', 'bus_stop', 'construction', 'corridor', 'crossing', 'cycleway', 'elevator', 
                      'emergency_bay', 'escape', 'ferry', 'footway', 'ladder', 'living_street', 'motorway', 
                      'motorway_link', 'path', 'pedestrian', 'platform', 'primary', 'primary_link', 'proposed', 
                      'raceway', 'razed', 'residential', 'rest_area', 'road', 'secondary', 'secondary_link', 'service', 
                      'services', 'shuttle_bus', 'shuttle_train', 'steps', 'tertiary', 'tertiary_link', 'track', 'trail', 
                      'trunk', 'trunk_link', 'unclassified', 'via_ferrata', 'parking_aisle', 'driveway']

OsmAccess: TypeAlias = Literal['Yes', 'bwd', 'construction', 'customers', 'customers;private', 'customer', 'delivery', 'designated', 
                    'destination', 'discouraged', 'emergency', 'employees', 'forestry', 'fwd', 'impassable', 
                    'limited', 'military', 'no', 'official', 'passable', 'permissive', 'private', 'private;customers', 
                    'students', 'use_sidepath', 'yes', 'allowed']

OsmMtbScale: TypeAlias = Literal['0', '0+', '0-', '1', '1+', '1-', '2', '2+', '2-', '3', '3+', '3-', 
                      '4', '4+', '4-', '5', '5+', '5-', '6', '6+', '6-', 0, 1, 2, 3, 4, 5, 6
                      ]
OsmMtbScaleSVal: TypeAlias = Literal['s0', 's1', 's2', 's3', 's4', 's5', 's6']

OsmLocalityTag: TypeAlias = Literal['allotment', 'archipelago', 'borough', 'city', 'city_block', 'farm', 
                         'hamlet', 'island', 'islet', 'isolated_dwelling', 'locality', 'municipality', 
                         'neighbourhood', 'plot', 'quarter', 'square', 'suburb', 'town', 'village']

OsmSmoothness: TypeAlias = Literal['average', 'bad', 'bon', 'catastrophic', 'excelent', 'excellent', 'fair', 'fine', 
                        'good', 'grass', 'high_clearance', 'horrible', 'impassable', 'intermediate', 'mediocre', 
                        'medium', 'moderate', 'moyen', 'off_road_wheels', 'ok', 'p', 'perfect', 'poor', 'reasonable', 
                        'robust_wheels', 'rough', 'smooth', 'specialized_off_road_wheels', 'terrible', 'thin_rollers', 
                        'thin_wheels', 'uneven', 'unpaved', 'very_bad', 'very bad', 'very_good', 'very_horrible', 
                        'very horrible', 'yes']

OsmTrailVisibility: TypeAlias = Literal['bad', 'check', 'excellent', 'excellent/good', 'exellent', 'fair', 'good', 'gut', 
                          'horrible', 'intermediate', 'intermittant', 'intermittent', 'medium', 'moderate', 
                          'no', 'none', 'ok', 'terrible', 'very_bad', 'very_good', 'very_horrible', 'y', 'yes']



OsmBridgeLayers: TypeAlias = Literal[1,2,3,4,5,'1','2','3','4','5','+1','+2','+3','+4','+5']

BicycleRestrictions: TypeAlias = Literal['dismount', 'separate', 'use_sidepath', 'share_sidewalk']
ExtraAccess: TypeAlias = Literal['agriforest']
ExtraHighways: TypeAlias = Literal['ftwy', 'crossing', 'train', 'bus']
LiftHighways: TypeAlias = Literal['gondola', 'funicular', 'chair_lift', 'zip_line', 'mixed_lift', 'cable_car']

HikeSurface: TypeAlias = Literal['asphalt', 'forest_soil', 'grass', 'gravel/sand', 'ground/dirt', 'ground/dirt/grass', 'ground/grass', 
                      'ground/gravel', 'ground/rocks', 'ground/roots', 'metal', 'paved/concrete', 'plastic/rubber', 'rocks', 
                      'rubble', 'salt', 'scrub', 'snow/ice', 'stone/cobblestone', 'timber', 'wood', 'rock', 'other/unknown']

RoadSurface: TypeAlias = Literal['asphalt', 'gravel/sand', 'ground/dirt/grass', 'metal', 'paved/concrete', 'plastic/rubber', 'rocks', 
                      'rubble', 'scrub', 'stone/cobblestone', 'timber', 'wood', 'rock', 'other/unknown']
Quality: TypeAlias = Literal[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 28, 29, 
                  30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 44, 45, 46, 49, 50, 51, 52, 55, 56, 59, 
                  60, 66, 69, 70, 80, 90, 91, 92, 95, 96, 97, 
                  100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 
                  110, 112, 115, 118, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 
                  130, 131, 132, 135, 136, 140, 141, 142, 143, 150, 155, 156, 157, 158, 159,
                  190, 197, 198, 199, 999 
                  ]

ValidSmoothness: TypeAlias = Literal['bad', 'excellent', 'good', 'horrible', 'impassable', 'intermediate', 'very_bad', 'very_good', 'very_horrible']

CellOsmWayId: TypeAlias = str
CellOsmAreaId: TypeAlias = str
CellOsmRelatId: TypeAlias = str

SubcellKey: TypeAlias = Literal['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', 
                     '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', 
                     '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', 
                     '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', 
                     '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', 
                     '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', 
                     '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', 
                     '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', 
                     '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', 
                     '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']

SpecialKey: TypeAlias = Literal["cells", "bbox", "ids", -1]
CellKey: TypeAlias = str

SurfaceDictType: TypeAlias = dict[str, RoadSurface | HikeSurface]

tagset_id: TypeAlias = int
name: TypeAlias = str | None
name_de: TypeAlias = str | None
name_en: TypeAlias = str | None
code: TypeAlias = str | None
lat: TypeAlias = int | float | np.floating
lon: TypeAlias = int | float | np.floating
addr_city: TypeAlias = str | None
wikipedia: TypeAlias = str | None
website: TypeAlias = str | None
description: TypeAlias = str | None
heritage: TypeAlias = str | None
radius: TypeAlias = float | None


Role: TypeAlias = str | None

railway_type: TypeAlias = str
waterway_type: TypeAlias = str
highway_type: TypeAlias = str
is_tunnel: TypeAlias = bool
is_bridge: TypeAlias = bool
is_intermittent: TypeAlias = bool

WaterwayRelatType: TypeAlias = tuple[waterway_type, name, name_de, OsmRelatId] | tuple[waterway_type, name, name_de, OsmRelatId, Role]

lanes: TypeAlias = int | str | None
maxspeed: TypeAlias = int | str | None
oneway: TypeAlias = str | None
scenic: TypeAlias = str | None
scenic_road_ids: TypeAlias = list[int]


WghtFct: TypeAlias = float | np.floating
#AreaTagsDict = Dict[str, Union[OsmAreaId | TagVal | BBox | int | tuple[int, int] | BaseGeometry | MultiPolygon]]

PeakTS: TypeAlias = tuple[Literal['peak']] | tuple[Literal['peak'], str, str]
LocPlaceTS: TypeAlias = tuple[Literal['locality'], Literal['place'], str]
VolcanoTS: TypeAlias = tuple[Literal['volcano'], str | None, str | None]
MtnPassTS: TypeAlias = tuple[Literal['mountain_pass'], Literal['mountain_pass'], Literal['mountain_pass']]
BarrierTS: TypeAlias = tuple[Literal['barrier_node'], Literal['barrier'], str | None, int, int]

#LocFerryTS = tuple[Literal['locality'], Literal['ferry'], str | None, str | None, str | None, str | None]
LocFerryTS: TypeAlias = tuple[Literal['locality'], Literal['ferry'], Literal['ferry_terminal'], TagVal, TagVal, TagVal]
#LocRailwayTS = tuple[Literal['locality'], Literal['railway'], str | None, str | None, str | None, str | None]
LocRailwayTS: TypeAlias = tuple[Literal['locality'], Literal['railway'], TagVal, Literal['yes', 'no'], TagVal, TagVal]

TourismTypeTS: TypeAlias = tuple[Literal['tourism'], Literal['tourism_type'], str | None, str | None, str | None, str | None]
TourismBuildingTS: TypeAlias = tuple[Literal['tourism'], Literal['building_type'], str | None, str | None, str | None, str | None]
TourismHistoricTS: TypeAlias = tuple[Literal['tourism'], Literal['historic_type'], str | None, str | None, str | None, str | None]
TourismAmenityTS: TypeAlias = tuple[Literal['tourism'], Literal['amenity_type'], str | None, str | None, str | None, str | None, str | None]
TourismParkingTS: TypeAlias = tuple[Literal['tourism'], Literal['parking'], str | None, str | None, str | None, str | None, str | None]
TourismBikeCharTS: TypeAlias = tuple[Literal['tourism'], Literal['bicycle_charging'], str | None, str | None, str | None, str | None, str | None]
TourismBikeRentTS: TypeAlias = tuple[Literal['tourism'], Literal['bicycle_rental'], str | None, str | None, str | None, str | None, str | None]
TourismSwimmingTS: TypeAlias = tuple[Literal['tourism'], Literal['swimming'], str | None, str | None, str | None, str | None, str | None, str | None]


GuidepostTS: TypeAlias = tuple[Literal['guidepost_node'], Literal['guidepost'], str | None, str | None, str | None, str | None, str | None, str | None]

TourismTagset: TypeAlias = TourismTypeTS | TourismBuildingTS | TourismAmenityTS | TourismHistoricTS | TourismParkingTS | TourismBikeCharTS | TourismBikeRentTS | TourismSwimmingTS
NodesTagset: TypeAlias = PeakTS | VolcanoTS | MtnPassTS | BarrierTS | LocPlaceTS | LocFerryTS | LocRailwayTS | GuidepostTS | TourismTagset
NodesTagsetId: TypeAlias = int
WayTagset: TypeAlias = tuple[Quality, OsmHighway, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, 
                  TagVal, TagVal, TagVal, TagVal, OsmAccess, TagVal, RoadSurface, TagVal, ValidSmoothness, TagVal, 
                  TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal]
WayTagsetId: TypeAlias = int
CWTagset: TypeAlias = tuple[TagVal, TagVal, TagVal, RoadSurface, ValidSmoothness, TagVal, TagVal, TagVal, TagVal, RoadSurface, 
                 ValidSmoothness, TagVal, TagVal, TagVal, TagVal, RoadSurface, ValidSmoothness, TagVal, TagVal, TagVal, 
                 TagVal, TagVal, TagVal, TagVal]
CWTagsetId: TypeAlias = int
HikeTagset: TypeAlias = tuple[Quality, Quality, TagVal, HikeSurface, ValidSmoothness, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, 
                   TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal]
HikeTagsetId: TypeAlias = int

FeatTagset: TypeAlias = tuple[TagVal, ...]
FeatTagsetId: TypeAlias = int

TagsetId: TypeAlias = WayTagsetId | CWTagsetId | HikeTagsetId | NodesTagsetId | FeatTagsetId | int
TagsetKey: TypeAlias = NodesTagset | WayTagset | CWTagset | HikeTagset | FeatTagset | Literal[-1]
# Generic code example with definition of TypeVars
TagsetDict: TypeAlias = dict[TagsetKey, TagsetId]

RevTagsetDict: TypeAlias = dict[TagsetId, TagsetKey]
RevHikeTagsetVals: TypeAlias = tuple[
    Quality, Quality, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, TagVal, HikeSurface, ValidSmoothness, TagVal,
    TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal]


TagsetCombiId: TypeAlias = int
TagsetCombiDict: TypeAlias = dict[tuple[WayTagsetId, CWTagsetId] | Literal[-1], TagsetCombiId]
RevTagsetCombiVals: TypeAlias = tuple[
    WayTagsetId, CWTagsetId, 
    WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct, WghtFct,
    Quality, OsmHighway, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal, TagVal]
RevTagsetCombiDict: TypeAlias = dict[TagsetCombiId, RevTagsetCombiVals]

EmptyCellStructDict: TypeAlias = Dict[SpecialKey, Dict[CellKey, Dict[SubcellKey, set[int]]]]


WaysTuple: TypeAlias = tuple[OsmNodeId, OsmNodeId, TagsetCombiId, HikeTagsetId, name, OsmNodesList]

class InnerData(TypedDict):
    """The innermost schema containing c, w, and n."""
    c: dict[FnamesValid, set[OsmWayId]]
    w: dict[OsmWayId, WaysTuple]
    n: dict[OsmNodeId, Any]  # Keep as Any or specific if n grows

#SubcellCDict = dict[Literal['c'], dict[FnamesValid, set[OsmWayId]]]
#SubcellWDict = dict[Literal['w'], dict[OsmWayId, WaysTuple]]
#SubcellNDict = dict[Literal['n'], dict]
#SubcellDataDict = dict[SubcellKey, dict[Literal['c', 'w', 'n'], dict[FnamesValid, set[OsmWayId]] | dict[OsmWayId, WaysTuple]]]
SubcellDataDict: TypeAlias = dict[SubcellKey, InnerData]
CellDataDict: TypeAlias = dict[CellKey, SubcellDataDict]

TourismNodesTuple: TypeAlias = tuple[tagset_id, name, name_de, name_en, lat, lon, addr_city, wikipedia, website, description, heritage, radius]
TourismNodesDict: TypeAlias = Dict[SpecialKey | int, Dict[CellKey, Dict[SubcellKey, set[int]]] | TourismNodesTuple]
TourismNodesObj: TypeAlias = Union[TourismNodesDict, EmptyCellStructDict]

#         tourism_area_dict[id] = (name, name_de, name_en, addr_city, wikipedia, website, heritage, *tagset, poly)
TourismAreasTuple: TypeAlias = tuple[name, name_de, name_en, addr_city, wikipedia, website, heritage, BaseGeometry]
TourismAreasBBoxList: TypeAlias = list[set[tuple[OsmAreaId, FlexNumeric, FlexNumeric, 
                                       FlexNumeric, BBoxInt]]]
TourismAreasDict: TypeAlias = Dict[SpecialKey | int, TourismAreasBBoxList | TourismAreasTuple]
#         tourism_area_dict[-1].append((id, w, h, poly_area_m2, bbox))
TourismAreasObj: TypeAlias = Union[TourismAreasDict, EmptyCellStructDict]


HighwaysTuple: TypeAlias = tuple[highway_type, name, lanes, maxspeed, oneway, is_tunnel, scenic, scenic_road_ids, OsmNodesList]
HighwaysDict: TypeAlias = Dict[SpecialKey | int, Dict[CellKey, Dict[SubcellKey, set[int]]] | HighwaysTuple]
HighwaysObj: TypeAlias = Union[HighwaysDict, EmptyCellStructDict]

RailwaysTuple: TypeAlias = tuple[railway_type, name, is_tunnel, is_bridge, OsmNodesList]
RailwaysDict: TypeAlias = Dict[SpecialKey | int, Dict[CellKey, Dict[SubcellKey, set[int]]] | RailwaysTuple]
RailwaysObj: TypeAlias = Union[RailwaysDict, EmptyCellStructDict]

WaterwaysTuple: TypeAlias = tuple[waterway_type, name, name_de, is_tunnel, is_intermittent, OsmNodesList]
WaterwaysDict: TypeAlias = Dict[SpecialKey | int, Dict[CellKey, Dict[SubcellKey, set[int]]] | WaterwaysTuple]
WaterwaysObj: TypeAlias = Union[WaterwaysDict, EmptyCellStructDict]


CoastlineTuple: TypeAlias = Tuple[name, OsmNodesList]


