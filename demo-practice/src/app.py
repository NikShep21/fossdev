import requests


def get_status_message() -> str:
    """Return a status message for the demo application."""
    return "Running app"


def main() -> None:
    """Run the demo application."""
    _ = requests.__version__
    print(get_status_message())


if __name__ == "__main__":
    main()
