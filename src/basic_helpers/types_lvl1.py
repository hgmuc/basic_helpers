import queue
import multiprocessing.queues as mpq
from typing import Literal, Any
from .config_pbf import FnamesValid
from .types_osm import OsmWayId, OsmRelatId, OsmNodeId, WaysTuple, CellDataDict

MapDictType = dict[str, dict[str, str | int | None]]

SuperRouteType = dict[OsmRelatId, dict[str, str | int | None]]
SRDictType = dict[OsmRelatId, dict[str, str | None | dict[OsmRelatId, tuple[int, str | None]]]]
RouteDictType = dict  # bleibt leer
RouteNodesType = dict[OsmNodeId, list[dict[str, str | OsmRelatId | None]]]
RouteWaysType = dict[FnamesValid, dict[OsmWayId, dict[str, str | int | OsmRelatId | None]]]
RDWaysSet = set[OsmWayId]
RteWaysTuple = tuple[RouteWaysType, RDWaysSet, RouteWaysType | None, RouteWaysType | None, dict | None]

RelatRelWaysType = dict[OsmRelatId | Literal[-1], Any] | None
RegionDataType = dict[Literal['c', 'names', 'w'], dict[int | FnamesValid, Any]] | None
CoastalWaterType = dict[Literal['c', 'names', 'w'], dict[int | FnamesValid, Any]] | None

Lvl1RelatTypes = Literal['waterway', 'highway', 'railway', 'route', 'superroute', 'region',
                         'hiking_route', 'hiking_superroute', 'mtb_route', 'mtb_superroute']

Lvl1WayTypes = Literal['railway', 'road', 'waterway', 'cycling', 'tourism', 'treerow', 'region', 'coastline']
Lvl1NodeTypes = Literal['locality', 'tourism']

QDictData = dict[OsmWayId, WaysTuple]
QDictType = dict[FnamesValid, QDictData]
WaysDataDictType = dict[FnamesValid, CellDataDict]


LocalQueueDefDict = dict[Lvl1WayTypes | Lvl1NodeTypes, queue.Queue]
SharedQueueDefDict = dict[str, mpq.Queue]
