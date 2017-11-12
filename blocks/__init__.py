__version__ = '1.0.0-dev'
__author__ = 'Ethan Haynes'
__licence__ = 'MIT'


class ExitStatus:
    """Exit status code constants."""
    OK = 0
    ERROR = 1
    PLUGIN_ERROR = 7

    ERROR_CTRL_C = 130

    ERROR_TIMEOUT = 2
    ERROR_TOO_MANY_REDIRECTS = 6

EXIT_STATUS_LABELS = dict(
    (value, key)
    for key, value in ExitStatus.__dict__.items()
    if key.isupper()
)
