import numpy as np
import numpy.typing as npt
import pandas as pd
from typing import NamedTuple, TypeAlias

from basic_helpers.config_reg_code import RegCodePart, RC
from basic_helpers.types_lvl1 import DestsDict

CellmapDict: TypeAlias = dict[RegCodePart, int]
RCMapDict: TypeAlias = dict[RC, int]



class REV_TC_FIXT_CLS(NamedTuple):
    rev_tc_dict: dict
    rev_tc_df: pd.DataFrame

class REV_HIKE_TAG_FIXT_CLS(NamedTuple):
    rev_hike_tags_dict: dict
    rev_hike_tags_df: pd.DataFrame

class QmapsTuple(NamedTuple):
    qmap: dict
    htc_q_map0: dict
    htc_q_map1: dict

class ClusterArrTuple(NamedTuple):
    cell_arr: npt.NDArray[np.integer]
    cellmap: CellmapDict
    rc_arr: npt.NDArray[np.floating]
    rc_map: RCMapDict

class FeatTagsetTuple(NamedTuple):
    tagset_id: dict[int, int]
    tagset_id_3D: dict[int, npt.NDArray[np.int64]]

class GuidepostTuple(NamedTuple):
    df: pd.DataFrame
    dests_dict: DestsDict

