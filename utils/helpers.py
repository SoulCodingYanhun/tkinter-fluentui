import uuid
from datetime import datetime
from typing import Callable
import time

def generate_id() -> str:
    """
    Generate a unique ID.
    """
    return str(uuid.uuid4())

def format_date(date: datetime, format_str: str = "%Y-%m-%d") -> str:
    """
    Format a date according to the given format string.
    """
    return date.strftime(format_str)

def debounce(wait: float):
    """
    Decorator to debounce a function.
    """
    def decorator(fn):
        last_called = None
        timer = None

        def debounced(*args, **kwargs):
            nonlocal last_called, timer

            def call_func():
                nonlocal last_called
                last_called = time.time()
                return fn(*args, **kwargs)

            if timer is not None:
                timer.cancel()

            if last_called is None or time.time() - last_called >= wait:
                return call_func()
            else:
                timer = threading.Timer(wait - (time.time() - last_called), call_func)
                timer.start()

        return debounced
    return decorator

def throttle(wait: float):
    """
    Decorator to throttle a function.
    """
    def decorator(fn):
        last_called = 0

        def throttled(*args, **kwargs):
            nonlocal last_called
            now = time.time()
            if now - last_called >= wait:
                last_called = now
                return fn(*args, **kwargs)

        return throttled
    return decorator

def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Clamp a value between a minimum and maximum.
    """
    return max(min_value, min(value, max_value))

def lerp(start: float, end: float, t: float) -> float:
    """
    Linear interpolation between start and end values.
    """
    return start + (end - start) * t
