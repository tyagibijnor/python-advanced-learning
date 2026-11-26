import logging

from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent / "application.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format=(
        "%(asctime)s | %(levelname)s | "
        "%(filename)s | %(funcName)s | %(lineno)d | %(message)s"
    ),
)

logger = logging.getLogger(__name__)


def process_payment():
    logger.info("Processing payment")

    try:
        raise ValueError("Payment processing failed")

    except ValueError:
        logger.exception("Payment processing encountered an error")


if __name__ == "__main__":
    process_payment()
