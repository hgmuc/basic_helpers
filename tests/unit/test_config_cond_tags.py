import pytest
from basic_helpers.config_cond_tags import (
    COND_TAGS, MONTH_LS, MONTH_CORR, WEEKDAY_VALS, 
    WEEKDAY_MAP_DICT, ACTION_KW, FIX_ACTION_KW, 
    CLEAN_CONDS, RND_TIME_COND_REF_DATES
)

def test_cond_tags_integrity():
    """Verify COND_TAGS is a set of strings and contains expected core tags."""
    assert isinstance(COND_TAGS, set)
    assert "access:conditional" in COND_TAGS
    assert len(COND_TAGS) == 8

def test_month_constants():
    """Verify month list and correction mapping."""
    assert len(MONTH_LS) == 12
    assert MONTH_LS[0] == "Jan"
    
    # Check specific mappings
    assert MONTH_CORR["Januar"] == "Jan"
    assert MONTH_CORR["Mär"] == "Mar"
    assert MONTH_CORR["Dez"] == "Dec"
    # Ensure all values in MONTH_CORR are in MONTH_LS
    for short_month in MONTH_CORR.values():
        assert short_month in MONTH_LS

def test_weekday_constants():
    """Verify weekday values and mapping dictionary."""
    assert len(WEEKDAY_VALS) == 9  # Mo-Su + PH, SH
    assert "PH" in WEEKDAY_VALS
    
    # Check specific mappings
    assert WEEKDAY_MAP_DICT["Sunday"] == "Su"
    assert WEEKDAY_MAP_DICT["Di"] == "Tu"
    assert WEEKDAY_MAP_DICT["lu"] == "Mo"
    assert WEEKDAY_MAP_DICT["ph"] == "PH"

    assert len(WEEKDAY_MAP_DICT) == 59

def test_action_keywords_structure():
    """Verify ACTION_KW dictionary structure and value types."""
    assert isinstance(ACTION_KW, dict)
    for key, value in ACTION_KW.items():
        assert isinstance(value, tuple)
        assert len(value) == 2
        assert isinstance(value[0], str)
        assert value[1] is None or isinstance(value[1], str)

    assert ACTION_KW["destination"] == ("yes", "destination")
    assert ACTION_KW["no"] == ("no", None)
    assert len(ACTION_KW) == 22

def test_fix_action_keywords():
    """Verify fix mappings for common tagging errors."""
    assert FIX_ACTION_KW["-1"] == "yes_opposite"
    assert FIX_ACTION_KW["none"] == "no"
    assert "winter" in FIX_ACTION_KW

    assert len(FIX_ACTION_KW) == 7

def test_clean_conds_integrity():
    """Verify CLEAN_CONDS contains the expected sample size for processing."""
    assert isinstance(CLEAN_CONDS, set)
    # Testing the specific length of the set provided in the snippet
    assert len(CLEAN_CONDS) == 41

def test_reference_dates_format():
    """Verify RND_TIME_COND_REF_DATES are valid 5-tuples of integers."""
    assert isinstance(RND_TIME_COND_REF_DATES, set)
    assert len(RND_TIME_COND_REF_DATES) == 500
    
    for date_tuple in RND_TIME_COND_REF_DATES:
        assert isinstance(date_tuple, tuple)
        assert len(date_tuple) == 5
        assert all(isinstance(i, int) for i in date_tuple)
        # Basic date validation
        year, month, day, hour, minute = date_tuple
        assert 2020 <= year <= 2026
        assert 1 <= month <= 12
        assert 1 <= day <= 31
        assert 0 <= hour <= 23
        assert 0 <= minute <= 59

@pytest.mark.parametrize("key", ["Januar", "February", "Mär", "Aprile"])
def test_month_corr_keys(key):
    """Ensure specific expected keys exist in MONTH_CORR."""
    assert key in MONTH_CORR
    assert len(MONTH_CORR) == 59