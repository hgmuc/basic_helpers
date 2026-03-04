import numpy as np
from typing import TypeAlias

FlexNumeric: TypeAlias = int | float | np.floating
CoordVal: TypeAlias = float | int | np.floating
Coordinate: TypeAlias =  tuple[CoordVal, CoordVal] | list[CoordVal]
CoordinateInt: TypeAlias = tuple[int, int] | list[int]
BBox: TypeAlias = tuple[CoordVal, CoordVal, CoordVal, CoordVal] | list[CoordVal]
BBoxInt: TypeAlias = tuple[int, int, int, int] | list[int]

OsmNodeId: TypeAlias = int
OsmWayId: TypeAlias = int
OsmRelatId: TypeAlias = int
OsmAreaId: TypeAlias = int

TagVal: TypeAlias = str | int | None
TagsDict: TypeAlias = dict[str, TagVal]
