
import time

def poll_for_condition(func, retries=5, delay=2):
    for i in range(retries):
        result = func()
        if result:
            return result
        time.sleep(delay)
    raise TimeoutError("Polling failed after retries")
