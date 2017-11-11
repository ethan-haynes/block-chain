#!/usr/bin/env python
"""The main entry point. Invoke as `http' or `python -m httpie'.
"""
import sys

def main():
    try:
        from .server import start
        sys.exit(start())
    except KeyboardInterrupt:
        from . import ExitStatus
        sys.exit(ExitStatus.ERROR_CTRL_C)


if __name__ == '__main__':
    main()
