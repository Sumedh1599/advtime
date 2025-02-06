import unittest
from advtime import advtime

class TestAdvTime(unittest.TestCase):
    def test_high_precision_time(self):
        time1 = advtime.high_precision_time()
        time2 = advtime.high_precision_time()
        self.assertTrue(time1 < time2)  # Time should always increase

    def test_utc_timestamp(self):
        timestamp = advtime.utc_timestamp()
        self.assertTrue(timestamp.endswith("Z") or "T" in timestamp)  # ISO 8601 check

    def test_time_hash(self):
        hash1 = advtime.time_hash("test")
        hash2 = advtime.time_hash("test")
        self.assertNotEqual(hash1, hash2)  # Hash should be unique

    def test_threaded_sleep(self):
        import time
        start = time.time()
        thread = advtime.threaded_sleep(2)
        thread.join()  # Wait for sleep to finish
        end = time.time()
        self.assertTrue(end - start >= 2)  # Ensure sleep worked

if __name__ == "__main__":
    unittest.main()
