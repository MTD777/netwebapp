import time
from logging_automation import log_message

def retry(task, logger, retries=3, wait_times=[5, 7]):
    for attempt in range(retries):
        try:
            return task()
        except Exception as e:
            log_message(logger, f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                wait_time = wait_times[attempt] if attempt < len(wait_times) else wait_times[-1]
                log_message(logger, f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
    return False
