#!/usr/bin/python3
"""
This initialization module contains object defitions that are common to
all modules in this package
"""
from pydantic import ValidationError
from server.setup import LoadEnv


try:
    env_vars = LoadEnv()  # type: ignore
except ValidationError as v:
    err_obj = v.errors()
    err_var = err_obj[0]["loc"][0]
    err_msg = err_obj[0]["msg"]
    var_val = err_obj[0]["input"]
    print("Usage Error: error encountered while loading environment variables")
    print(f"Error exp: {err_var}='{var_val}'")
    print(f"Error msg: {err_msg}")
