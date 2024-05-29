#!/usr/bin/env python3
"""
This module sets up and configures the server environment variables, ensuring
they are loaded and validated correctly.
"""
import logging
from pathlib import Path
from pydantic import Field
from pydantic import field_validator
from pydantic import ValidationInfo
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
from pydantic.networks import IPvAnyAddress
from typing import Union
from typing_extensions import Annotated


class LoadEnv(BaseSettings):
    """
    LoadEnv is a subclass of pydantic_settings.BaseSettings that loads and
    validates the required environment variables.

    Attributes:
        HOST (IPvAnyAddress): The IP address on which the server runs.
        PORT (Annotated[int, Field(gt=0, lt=65535)]): The port number on which
                                                      the server runs.
        TEST_PORT (Annotated[int, Field(gt=0, lt=65535)]): The port number on
                                                      which the test servers
                                                      run.
        LINUXPATH (Path): The path to the Linux search file.
        SSL (bool): Whether SSL is enabled or not.
        REREAD_ON_QUERY (bool): Whether to reload the search string file
                                momentarily.
        CERTFILE (Path | None): The path to the SSL certificate file.
        KEYFILE (Path | None): The path to the SSL key file.
        ALGORITHM (str): The search algorithm to use
        DEBUG (Path): The path to the debug log file.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    HOST: IPvAnyAddress
    PORT: Annotated[int, Field(gt=0, lt=65535)]
    TEST_PORT: Annotated[int, Field(gt=0, lt=65535)]
    LINUXPATH: Path
    SSL: bool = True
    REREAD_ON_QUERY: bool = False
    CERTFILE: Union[Path, None] = None
    KEYFILE: Union[Path, None] = None
    ALGORITHM: str
    DEBUG: Path

    @field_validator("LINUXPATH", mode="before")
    @classmethod
    def validate_linux_path(cls, linux_path: str, info: ValidationInfo) -> str:
        """
        Validates that the LINUXPATH points to an existing file.

        Args:
            linux_path (str): The path to the Linux search file.
            info (ValidationInfo): Pydantic validation information.

        Returns:
            str: The validated Linux path.

        Raises:
            ValueError: If the file does not exist or the path is empty.
        """
        # create a path object from the value supplied to the LINUXPATH
        # environment variable
        path_obj: Path = Path(linux_path)

        # check if the file exist, raise error if it does not exist
        if not path_obj.is_file():
            field_name: Union[str, None] = info.field_name
            msg = "Invalid file path"
            raise ValueError(msg)
        return linux_path

    @field_validator("CERTFILE", "KEYFILE", mode="before")
    @classmethod
    def validate_ssl_path(
        cls, path_str: str, info: ValidationInfo
    ) -> Union[str, None]:
        """
        Validates the SSL certificate and key file paths if SSL is enabled.

        Args:
            path_str (str): The path to the SSL file.
            info (ValidationInfo): Pydantic validation information.

        Returns:
            str | None: The validated path or None if SSL is disabled.

        Raises:
            ValueError: If the file does not exist or the path is empty.
        """
        # get the value assigned to the ssl environment variable
        SSL: Union[bool, None] = info.data.get("SSL")
        if SSL:
            # create a path object from the value supplied to the
            # CERTFILE or KEYFILE environment variable
            path_obj: Path = Path(path_str)

            # check if the file exist, raise error if it does not exist
            if not path_obj.is_file():
                field_name: Union[str, None] = info.field_name
                msg = "Invalid file path"
                raise ValueError(msg)
            return path_str
        return None

    @field_validator("ALGORITHM")
    @classmethod
    def validate_algorithm(cls, value: str):
        """
        Validates that the search algorithm values is among the defined
        search algorithms

        Args:
            value (str): The search algorithm value

        Returns:
            str: The validated algorithm value
        """
        algorithms = ["jump", "bisect", "recursive", "iterative", "linear"]
        if value not in algorithms:
            raise ValueError(f"Value must be one of {algorithms}")
        return value

    @field_validator("DEBUG", mode="before")
    @classmethod
    def validate_debug_path(cls, path_str: Union[str, None]) -> str:
        """
        Validates and sets the path for the debug log file.

        Args:
            path_str (str | None): The path to the debug log file.

        Returns:
            str: The validated debug log path. Defaults to './debug.log' if not
               provided.

        Raises:
            logging.warning: If the path is not valid.
        """
        # raise a warning if no value is assigned to the DEBUG environment
        # variable
        if not path_str:
            logging.basicConfig(
                format="%(levelname)s: %(message)s", level=logging.DEBUG
            )
            logging.warning(
                "No debug file path is provided, will write debug information "
                f"to 'debug.log' file in the working direcotory of the server "
                f"script"
            )

        # return a "./debug.log" string if DEBUG environment variable has no
        # value assigned to it, else return the value
        return "./debug.log" if not path_str else path_str


if __name__ == "__main__":
    import os

    model = LoadEnv()  # type: ignore
    print(model)
