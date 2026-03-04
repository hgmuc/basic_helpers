from typing import TypeVar, cast, Any, Callable

T = TypeVar("T")

def convert_to_typed_dict(cls: Callable[..., T], raw_data: dict[str, Any]) -> T:
    """
    Filters a raw dictionary to only include keys defined in the 
    provided TypedDict class.
    """
    # At runtime, cls is the TypedDict class. 
    # We access its __annotations__ to see the allowed keys.
    annotations: dict[str, Any] = getattr(cls, "__annotations__", {})
    allowed_keys = annotations.keys()
    
    filtered = {
        k: v for k, v in raw_data.items() 
        if k in allowed_keys
    }
    
    # We cast the result to T so the return type is correct
    return cast(T, filtered)

