import queue
import multiprocessing.queues as mpq
from typing import Literal, Any, TypeAlias
from basic_helpers.config_pbf import FnamesValid
from basic_helpers.config_reg_code import RegCode
from basic_helpers.types_osm import OsmWayId, OsmRelatId, OsmNodeId, WaysTuple, CellDataDict, SpecialKey, CellKey, Lvl1AreaTypes
from basic_helpers.types_base import OsmAdminId
from basic_helpers.typed_dict_classes import Code2AdminIdsDict, UrbIdxAreaTracker

MapDictType: TypeAlias = dict[str, dict[str, str | int | None]]

SuperRouteType: TypeAlias = dict[OsmRelatId, dict[str, str | int | None]]
SRDictType: TypeAlias = dict[OsmRelatId, dict[str, str | None | dict[OsmRelatId, tuple[int, str | None]]]]
RouteDictType: TypeAlias = dict  # bleibt leer
RouteNodesType: TypeAlias = dict[OsmNodeId, list[dict[str, str | OsmRelatId | None]]]
RouteWaysType: TypeAlias = dict[FnamesValid, dict[OsmWayId, list[dict[str, str | int | OsmRelatId | None]]]]
RDWaysSet: TypeAlias = set[OsmWayId]
RteWaysTuple: TypeAlias = tuple[RouteWaysType, RDWaysSet, RouteWaysType | None, RouteWaysType | None, dict | None]

RelatRelWaysType: TypeAlias = dict[OsmRelatId | Literal[-1], Any] | None
RegionDataType: TypeAlias = dict[Literal['c', 'names', 'w'], dict[int | FnamesValid, Any]] | None
CoastalWaterType: TypeAlias = dict[Literal['c', 'names', 'w'], dict[int | FnamesValid, Any]] | None

Lvl1RelatTypes: TypeAlias = Literal['waterway', 'highway', 'railway', 'route', 'superroute', 'region',
                         'hiking_route', 'hiking_superroute', 'mtb_route', 'mtb_superroute']

Lvl1WayTypes: TypeAlias = Literal['railway', 'road', 'waterway', 'cycling', 'tourism', 'treerow', 'region', 'coastline']
Lvl1NodeTypes: TypeAlias = Literal['locality', 'tourism']

AdminLvlKeys: TypeAlias = Literal['adm4', 'adm5', 'adm6', 'adm7', 'adm8', 'adm9', 'adm10']

UrbanityIdxDict: TypeAlias = dict[CellKey | RegCode, dict[Lvl1AreaTypes, UrbIdxAreaTracker]]

DestsDict: TypeAlias = dict[int, dict[str, tuple[int, str]]]


Code2AdminRegCodeData: TypeAlias = dict[AdminLvlKeys, list[OsmAdminId]]
Code2AdminDict: TypeAlias = dict[SpecialKey | RegCode, 
                                 Code2AdminIdsDict | Code2AdminRegCodeData]

QDictData: TypeAlias = dict[OsmWayId, WaysTuple]
QDictType: TypeAlias = dict[FnamesValid, QDictData]
WaysDataDictType: TypeAlias = dict[FnamesValid, CellDataDict]

LocalQueueDefDict: TypeAlias = dict[Lvl1WayTypes | Lvl1NodeTypes, queue.Queue]
SharedQueueDefDict: TypeAlias = dict[str, mpq.Queue]
