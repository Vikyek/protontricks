**What:** I implemented caching using the `@functools.lru_cache()` decorator for the `is_steam_deck()` and `is_steamos()` functions in `src/protontricks/util.py`.

**Why:** Both of these functions repeatedly checked the file system by reading `/etc/os-release` or `/run/host/os-release` on every call. Since the operating system environment won't change while protontricks is running, these file reads were redundant and introduced unnecessary I/O and latency. Caching the results ensures we only do the expensive operation once.

**Measured Improvement:** I added two small benchmark scripts during development that ran each function 1000 times in a loop.
- **`is_steam_deck()` baseline:** ~0.068 seconds
- **`is_steam_deck()` optimized:** ~0.0003 seconds
- **`is_steamos()` baseline:** ~0.074 seconds
- **`is_steamos()` optimized:** ~0.0003 seconds
This is an over 200x performance increase on these calls and completely eliminates disk access after the initial execution.

I also added an `autouse` fixture to `conftest.py` that clears these caches for every test, ensuring our mocked filesystem state changes during tests do not break or cross-contaminate.
