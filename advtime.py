import time
import threading
import hashlib
from datetime import datetime, timezone

class advtime:
    @staticmethod
    def high_precision_time() -> float:
        """Get high-precision time (nanoseconds resolution)."""
        return time.perf_counter_ns() / 1e9

    @staticmethod
    def utc_timestamp() -> str:
        """Get current UTC timestamp in ISO 8601 format."""
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def time_hash(seed: str = "") -> str:
        """Generate a secure SHA-256 hash of the current timestamp."""
        timestamp = str(time.time()).encode()
        return hashlib.sha256(timestamp + seed.encode()).hexdigest()

    @staticmethod
    def threaded_sleep(seconds: float):
        """Threaded sleep function to avoid blocking main process."""
        thread = threading.Thread(target=time.sleep, args=(seconds,))
        thread.start()
        return thread

if __name__ == "__main__":
    print("Testing advtime...")
    print("High-precision time:", advtime.high_precision_time())
    print("UTC Timestamp:", advtime.utc_timestamp())
    print("Time Hash:", advtime.time_hash("Brewlock"))
    print("Starting threaded sleep for 3 seconds...")
    advtime.threaded_sleep(3)
