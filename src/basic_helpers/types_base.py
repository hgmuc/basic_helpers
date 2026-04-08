import numpy as np
import numpy.typing as npt
from typing import TypeAlias, Any

OsmAdminId: TypeAlias = int
OsmAdminIdStr: TypeAlias = str


FlexNumeric: TypeAlias = int | float | np.floating
CoordVal: TypeAlias = float | int | np.floating
MVal: TypeAlias = FlexNumeric
Coordinate: TypeAlias =  tuple[CoordVal, CoordVal] | list[CoordVal]
CoordinateInt: TypeAlias = tuple[int, int] | list[int]
CoordinateM: TypeAlias =  tuple[FlexNumeric, FlexNumeric] | list[FlexNumeric]
BBox: TypeAlias = tuple[CoordVal, CoordVal, CoordVal, CoordVal] | list[CoordVal]
BBoxInt: TypeAlias = tuple[int, int, int, int] | list[int]
BBoxM: TypeAlias = tuple[MVal, MVal, MVal, MVal] | list[MVal]
ElevInt: TypeAlias = int
Elev: TypeAlias = int | float | np.floating

Url: TypeAlias = str

ElevArr: TypeAlias = npt.NDArray[np.integer[Any] | np.floating[Any]]

OsmNodeId: TypeAlias = int
OsmWayId: TypeAlias = int
OsmRelatId: TypeAlias = int
OsmAreaId: TypeAlias = int

TagVal: TypeAlias = str | int | None
TagsDict: TypeAlias = dict[str, TagVal]
