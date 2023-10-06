def get_variable_name(var):
    for name, value in globals().items():
        if value is var:
            return name
    for name, value in locals().items():
        if value is var:
            return name
    return None

def check_none(var, error_message = "Value is none"):
    if var is None:
        raise ValueError(error_message)


def check_type(var, data_type, error_message = None):
    if not isinstance(var, data_type):
        raise ValueError(error_message if error_message else f"{get_variable_name(var)} must be {data_type.__name__}")
    
def check_length(var, length, error_message = None):
    if len(var) != length:
        raise ValueError(f"Invalid length. {get_variable_name(var)} must be {length}")