import logging
import functools

logger = logging.getLogger(__name__)

def log_function(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        logger.info(f"Entering {func.__name__} function")
        try:
            result = await func(*args, **kwargs)
            logger.info(f"Exiting {func.__name__} function")
            return result
        except Exception as e:
            logger.exception(f"Exception in {func.__name__}: {e}")
            raise
    return wrapper
