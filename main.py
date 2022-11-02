from decimal import DivisionByZero
import logging


log = logging.getLogger(__name__)


class CustomException(Exception):
    pass


class CalculationError(Exception):
    pass


def calculate(a: int, b: int):
    if a == 2:
        # this func will fail
        raise CalculationError()
    return a + b

    # code linting


def greet():
    """_summary_

    Args:
        a (_type_): an integer value
        b (_type_): an integer value

    Returns:
        _type_: sum of two int
    """
    try:
        a = 10
        b = 20
        # total = a/0
        raise CustomException("sdfdsfsdf")
        print(total)
    except ZeroDivisionError:
        log.exception("DivisionByZero")
        return 0
    else:
        print("Success")
        return total
    finally:
        print("must")


if __name__ == "__main__":
    try:
        result = calculate(2, 3)
    except CalculationError:
        log.error("Calculation failed")
    else:
        print(result)
