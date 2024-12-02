from functools import wraps


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for i, (arg_name, arg_value) in enumerate(zip(annotations.keys(), args)):
            expected_type = annotations[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(f"Argument '{arg_name}' must be of type {expected_type.__name__}, "
                                f"but got type {type(arg_value).__name__}.")

        for kwarg_name, kwarg_value in kwargs.items():
            if kwarg_name in annotations:
                expected_type = annotations[kwarg_name]
                if not isinstance(kwarg_value, expected_type):
                    raise TypeError(f"Argument '{kwarg_name}' must be of type {expected_type.__name__}, "
                                    f"but got type {type(kwarg_value).__name__}.")

        return func(*args, **kwargs)

    return wrapper
