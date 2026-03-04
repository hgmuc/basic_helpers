from typing import TypedDict
from basic_helpers.typed_dict_helper import convert_to_typed_dict

# Define TypedDicts for testing
class SimpleDict(TypedDict):
    name: str
    id: int

class NestedDict(TypedDict):
    key: str
    flag: bool

def test_convert_to_typed_dict_filters_extra_keys():
    """Verify that keys not in TypedDict annotations are removed."""
    raw_garbage = {"name": "Test", "id": 1, "extra": "delete_me", "unwanted": 42}
    
    clean_simple = convert_to_typed_dict(SimpleDict, raw_garbage)
    
    # Assertions
    assert clean_simple == {"name": "Test", "id": 1}
    assert "extra" not in clean_simple
    assert "unwanted" not in clean_simple
    # Verify it is still a dictionary at runtime
    assert isinstance(clean_simple, dict)

def test_convert_to_typed_dict_missing_keys():
    """
    Verify behavior when raw data is missing keys defined in TypedDict.
    Note: TypedDict doesn't enforce presence at runtime via this helper 
    unless explicitly coded, it just filters what's there.
    """
    raw_data = {"name": "Partial"}  # 'id' is missing
    clean = convert_to_typed_dict(SimpleDict, raw_data)
    
    assert clean == {"name": "Partial"}
    assert "id" not in clean

def test_convert_to_typed_dict_empty_input():
    """Verify behavior with empty dictionary input."""
    clean = convert_to_typed_dict(SimpleDict, {})
    assert clean == {}

def test_convert_to_typed_dict_non_typed_dict_class():
    """Verify behavior when a standard class or empty object is passed."""
    class NotATypedDict:
        pass
        
    raw_data = {"any_key": "value"}
    # Should return empty dict because NotATypedDict has no __annotations__
    clean = convert_to_typed_dict(NotATypedDict, raw_data)
    assert clean == {}

def test_convert_to_typed_dict_identity_with_correct_keys():
    """Verify that a dictionary with exactly the right keys remains unchanged."""
    valid_data = {"name": "Perfect", "id": 100}
    clean = convert_to_typed_dict(SimpleDict, valid_data)
    assert clean == valid_data