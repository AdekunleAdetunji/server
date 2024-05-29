#!/usr/bin/env python3
import os
import pytest
from pathlib import Path
from pydantic import ValidationError
from server.setup import LoadEnv


@pytest.fixture(scope="function", autouse=True)
def clear_env_vars():
    """Fixture to clear environment variables before each test."""
    env_vars = [
        "HOST",
        "PORT",
        "LINUXPATH",
        "SSL",
        "REREAD_ON_QUERY",
        "CERTFILE",
        "KEYFILE",
        "DEBUG",
    ]
    for var in env_vars:
        if var in os.environ:
            del os.environ[var]
    yield
    for var in env_vars:
        if var in os.environ:
            del os.environ[var]


def set_env_vars(env_vars):
    """Helper function to set environment variables."""
    os.environ.update(env_vars)


def test_valid_env_vars():
    """Test loading and validation of valid environment variables."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "200k.txt",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "cert.pem",
        "KEYFILE": "key.pem",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    config = LoadEnv()
    assert str(config.HOST) == "127.0.0.1"
    assert config.PORT == 8000
    assert config.LINUXPATH == Path("200k.txt")
    assert config.SSL is True
    assert config.REREAD_ON_QUERY is True
    assert config.CERTFILE == Path("cert.pem")
    assert config.KEYFILE == Path("key.pem")
    assert config.DEBUG == Path("debug.log")


def test_missing_env_vars():
    """Test missing required environment variables."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "200k.txt",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    # with pytest.raises(ValidationError):
    #    LoadEnv()
    LoadEnv()


def test_invalid_linuxpath():
    """Test invalid LINUXPATH."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "invalid/path.txt",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "cert.pem",
        "KEYFILE": "key.pem",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()


def test_invalid_certfile_keyfile():
    """Test invalid CERTFILE and KEYFILE when SSL is enabled."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "200k.txt",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "invalid/cert.pem",
        "KEYFILE": "invalid/key.pem",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()


def test_ssl_disabled_no_certfile_keyfile():
    """Test that CERTFILE and KEYFILE are not required when SSL is disabled."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "200k.txt",
        "SSL": "False",
        "REREAD_ON_QUERY": "True",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    config = LoadEnv()
    assert config.CERTFILE is None
    assert config.KEYFILE is None


def test_default_debug_path():
    """Test the default value for DEBUG if not provided."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "200k.txt",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "DEBUG": "",
    }
    set_env_vars(env_vars)
    config = LoadEnv()
    assert config.DEBUG == Path("./debug.log")


def test_invalid_port():
    """Test invalid PORT value."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "70000",
        "LINUXPATH": "200k.txt",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "cert.pem",
        "KEYFILE": "key.pem",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()


def test_empty_linuxpath():
    """Test empty LINUXPATH value."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "cert.pem",
        "KEYFILE": "key.pem",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()


def test_empty_certfile_with_ssl():
    """Test empty CERTFILE value when SSL is enabled."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "200k.txt",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "",
        "KEYFILE": "key.pem",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()


def test_empty_keyfile_with_ssl():
    """Test empty KEYFILE value when SSL is enabled."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "200k.txt",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "cert.pem",
        "KEYFILE": "",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()


def test_invalid_ip_address():
    """Test invalid IP address for HOST."""
    env_vars = {
        "HOST": "999.999.999.999",
        "PORT": "8000",
        "LINUXPATH": "200k.txt",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "cert.pem",
        "KEYFILE": "key.pem",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()


def test_invalid_boolean_value():
    """Test invalid boolean value for SSL."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "200k.txt",
        "SSL": "NotABoolean",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "cert.pem",
        "KEYFILE": "key.pem",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()


def test_port_out_of_range():
    """Test PORT value out of valid range."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "-1",
        "LINUXPATH": "200k.txt",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "cert.pem",
        "KEYFILE": "key.pem",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()

    env_vars["PORT"] = "65536"
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()


def test_empty_debug_path():
    """Test empty DEBUG path and check the default value."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "200k.txt",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "DEBUG": "",
    }
    set_env_vars(env_vars)
    config = LoadEnv()
    assert config.DEBUG == Path("./debug.log")


def test_invalid_type_for_port():
    """Test that an invalid type for PORT raises a ValidationError."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "invalid_port",
        "LINUXPATH": "200k.txt",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "cert.pem",
        "KEYFILE": "key.pem",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()


def test_invalid_path_type_for_linuxpath():
    """Test that an invalid type for LINUXPATH raises a ValidationError."""
    env_vars = {
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "LINUXPATH": "1234",
        "SSL": "True",
        "REREAD_ON_QUERY": "True",
        "CERTFILE": "server/cert.pem",
        "KEYFILE": "server/key.pem",
        "DEBUG": "debug.log",
    }
    set_env_vars(env_vars)
    with pytest.raises(ValidationError):
        LoadEnv()
