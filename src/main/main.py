"""Default module docstring."""

import logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the main function."""
    logger.info("This is the main module.")


if __name__ == "__main__":
    main()
