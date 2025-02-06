# advtime

`advtime` is an advanced and enhanced time handling library, improving precision, multi-threading, and cryptographic security.

## Features

- High-precision nanosecond time resolution
- UTC timestamps in ISO 8601 format
- Cryptographic time-based hashing
- Threaded sleep for non-blocking delays

## Installation

```bash
pip install advtime
```

USAGE:
from advtime import advtime

print(advtime.high_precision_time()) # Nanosecond resolution
print(advtime.utc_timestamp()) # ISO 8601 format
print(advtime.time_hash("secure_seed")) # Secure timestamp hash
advtime.threaded_sleep(2) # Non-blocking sleep
