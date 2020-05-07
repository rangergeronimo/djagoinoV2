import os
from django.core.exceptions import ImproperlyConfigured


def get_var_value(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Set the {var_name} enviroment variable "
        raise ImproperlyConfigured(error_msg)
