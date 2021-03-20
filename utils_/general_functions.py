import asyncio
import gevent
from gevent.pool import Group
class General_functions:

    def async_map_a(coroutine_func, iterable):
        loop = asyncio.get_event_loop()
        future = asyncio.gather(*(coroutine_func(param) for param in iterable))
        return loop.run_until_complete(future)

    def async_map_g(f, iterable):
        group = Group()
        return group.map(f, iterable)

