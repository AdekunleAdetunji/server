#!/usr/bin/python3
"""
Initialize and configure the logger for the application. The logger will print
to both the console and a specified log file assigned to the "debug"
environment variable
"""

import logging
from .setup import LoadEnv
from pydantic import ValidationError

# Initialize the logger
logger = logging.getLogger(__name__)

# Define the log format string
format_str = "[%(asctime)s - %(levelname)s] - %(message)s"

# Configure the basic logging to the console
logging.basicConfig(format=format_str, level=logging.DEBUG)

# Try to load environment variables using the LoadEnv class
try:
    env_vars: LoadEnv = LoadEnv()  # type: ignore

# Catch and log any validation errors encountered when loading environment
# variables
except ValidationError as v:
    # Extract error information from the ValidationError object
    err_obj = v.errors()
    err_var = err_obj[0]["loc"][0]
    err_msg = err_obj[0]["msg"]
    var_val = err_obj[0]["input"]

    # Log the error information
    logger.error(
        "Unable to load environment variables\n"
        "{"
        f"err_exp: '{err_var}={var_val}', "
        f"err_msg: {err_msg}"
        "}"
    )
    exit()

# Add a file handler to the logger if the environment variables were loaded
# successfully
else:
    # Create a file handler with the log file path specified in env_vars.DEBUG
    file_handler = logging.FileHandler(env_vars.DEBUG)

    # Create a formatter using the defined format string
    formatter = logging.Formatter(format_str)

    # Set the formatter for the file handler
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)
