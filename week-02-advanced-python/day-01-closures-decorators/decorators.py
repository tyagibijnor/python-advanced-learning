import logging
import math
from functools import wraps

logger = logging.getLogger(__name__)


def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            "Starting function: %s | args=%s | kwargs=%s",
            func.__name__,
            args,
            kwargs,
        )

        try:
            result = func(*args, **kwargs)

            logger.info(
                "Function completed successfully: %s",
                func.__name__,
            )

            return result

        except Exception:
            logger.exception(
                "Function failed: %s",
                func.__name__,
            )
            raise

    return wrapper


@logging_decorator
def calculate_bonus(salary, percentage=10):
    if isinstance(salary, bool) or not isinstance(salary, (int, float)):
        raise TypeError("Salary must be a number")

    if not math.isfinite(salary):
        raise ValueError("Salary must be finite")

    if salary < 0:
        raise ValueError("Salary cannot be negative")

    if isinstance(percentage, bool) or not isinstance(percentage, (int, float)):
        raise TypeError("Percentage must be a number")

    if not math.isfinite(percentage):
        raise ValueError("Percentage must be finite")

    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100")

    return salary * percentage / 100


@logging_decorator
def employee_salary(salary, bonus=5000):
    if isinstance(salary, bool) or not isinstance(salary, (int, float)):
        raise TypeError("Salary must be a number")

    if not math.isfinite(salary):
        raise ValueError("Salary must be finite")

    if salary < 0:
        raise ValueError("Salary cannot be negative")

    if isinstance(bonus, bool) or not isinstance(bonus, (int, float)):
        raise TypeError("Bonus must be a number")

    if not math.isfinite(bonus):
        raise ValueError("Bonus must be finite")

    if bonus < 0:
        raise ValueError("Bonus cannot be negative")

    return salary + bonus
