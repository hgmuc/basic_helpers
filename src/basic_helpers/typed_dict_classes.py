from typing import TypedDict, TypeAlias
from shapely.geometry.base import BaseGeometry

from basic_helpers.types_base import OsmAdminId, OsmAreaId, BBox
from basic_helpers.types_osm import name, name_de, name_en, code
from basic_helpers.config_reg_code import RegCode

# Create a TypeAlias for the repetitive tuple to keep the Dict clean
AdminTuple: TypeAlias = tuple[name, name_de, name_en, code, set[RegCode]]

class Code2AdminIdsDict(TypedDict):
    adm4: dict[OsmAdminId, AdminTuple]
    adm5: dict[OsmAdminId, AdminTuple]
    adm6: dict[OsmAdminId, AdminTuple]
    adm7: dict[OsmAdminId, AdminTuple]
    adm8: dict[OsmAdminId, AdminTuple]
    adm9: dict[OsmAdminId, AdminTuple]
    adm10: dict[OsmAdminId, AdminTuple]


TourismAreaTagsDict = TypedDict('TourismAreaTagsDict', {
    "id": OsmAreaId,   
    "ntype": str,
    "tourism": str,
    "amenity": str,
    "historic": str,
    "building": str,
    "ref": str,
    "name": str,
    "name:de": str,
    "name:en": str,
    "addr:city": str,
    "wikipedia": str,
    "website": str,
    "description": str,
    "access": str,
    "bicycle": str,
    "bicycle_rental": str,
    "is_bicycle_charging_station": bool, # <= amenity == 'charging_station' && bicycle = yes or designated
    "drinking_water": str,
    "landuse": str,
    "natural": str,
    "surface": str,
    "leisure": str,
    "sport": str,
    "information": str,
    "map_type": str,
    "man_made": str,
    "this_historic": str,  # <= man_made + building + historic
    "heritage_operator": str,    # "heritage:operator"
    "heritage_cls": str,
    "fee": str,
    "heritage": str,    # heritage_cls = heritage => heritage = heritage:operator + heritage_cls
    "heritage:operator": str,  # This is now perfectly legal!
    "bbox": BBox,
    "geom": BaseGeometry,
    "wh": tuple[int, int]
}, total=False)


class TourismAreaTagsDictOLD(TypedDict, total=False):
    # With this syntax we cannot use OSM tag key names by default, because some contain colons ":"
    # The Functional Syntax above suppors key names with colons (and some other special characters)
    ntype: str   # tourism_type, historic_type, amenity_type, bicycle_charging, swimming, parking, ...
    tourism: str
    amenity: str
    historic: str
    building: str
    ref: str
    name: str
    name_de: str
    name_en: str
    addr_city: str
    wikipedia: str
    website: str
    description: str
    access: str
    bicycle: str
    bicycle_rental: str
    is_bicycle_charging_station: bool # <= amenity == 'charging_station' && bicycle = yes or designated
    drinking_water: str
    landuse: str
    natural: str
    surface: str
    leisure: str
    sport: str
    information: str
    map_type: str
    man_made: str
    this_historic: str  # <= man_made + building + historic
    heritage_operator: str    # "heritage:operator"
    heritage_cls: str
    fee: str
    heritage: str    # heritage_cls = heritage => heritage = heritage:operator + heritage_cls
    id: OsmAreaId
    bbox: BBox
    wh: tuple[int, int]
    w: int
    h: int
    geom: BaseGeometry


class UrbIdxAreaTracker(TypedDict, total=False):
    total_area: float
    area_ids: set[OsmAreaId]


# 1 [('peak',)]
# 3 [('locality', 'place'), ('mountain_pass', 'mountain_pass'), ('volcano', 'dormant'), ('volcano', 'active'), ('volcano', None), ('volcano', 'extinct')]
# 5 [('barrier_node', 'barrier')]
# 6 [('locality', 'ferry'), ('locality', 'railway'), ('tourism', 'historic_type'), ('tourism', 'tourism_type'), ('tourism', 'building_type')]
# 7 [('tourism', 'bicycle_charging'), ('tourism', 'parking'), ('tourism', 'amenity_type')]
# 8 [('guidepost_node', 'guidepost'), ('tourism', 'swimming')]

