from typing import Callable, Any


def cache(func: Callable) -> Callable:
    check_dict = {}
    def wrapper(*args, **kwargs) -> Any:
        if args in check_dict or kwargs.values() in check_dict:
            print("Getting from cache")
            return check_dict[args]
        elif args not in check_dict:
            print("Calculating new result")
            result = func(*args, **kwargs)
            check_dict[args] = result
            return result
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            check_dict[kwargs.values()] = result
            return result
    return wrapper
