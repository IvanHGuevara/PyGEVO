import asyncio

class General_functions:

    def async_map(coroutine_func, iterable):
        loop = asyncio.get_event_loop()
        future = asyncio.gather(*(coroutine_func(param) for param in iterable))
        return loop.run_until_complete(future)