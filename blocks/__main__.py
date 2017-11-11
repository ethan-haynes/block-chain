"""The main entry point.
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
