import random
import string

BASE62_CHARS = string.ascii_letters + string.digits
# abc...xyzABC...XYZ0123456789


def generate_short_code(length: int = 6) -> str:
    """
    Generate a random Base62 short code.

    Example:
        Ab3xY9
        z8LpQ2
    """
    return "".join(random.choices(BASE62_CHARS, k=length))