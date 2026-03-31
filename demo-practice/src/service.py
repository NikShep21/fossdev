import fastapi
import numpy
import requests


def get_dependency_versions() -> dict[str, str]:
    """Return versions of third-party dependencies used in the project."""
    return {
        "requests": requests.__version__,
        "numpy": numpy.__version__,
        "fastapi": fastapi.__version__,
    }


def calculate_mean(values: list[float]) -> float:
    """Calculate the arithmetic mean of the provided values."""
    array = numpy.array(values, dtype=float)
    return float(array.mean())
