import asyncio
import gevent
from gevent.pool import Group
from multiprocessing.pool import ThreadPool
import multiprocessing
class General_functions:
    
    #interface
    def async_map(f,iterable):
        def async_map_a(coroutine_func, iterable):
            loop = asyncio.get_event_loop()
            future = asyncio.gather(*(coroutine_func(param) for param in iterable))
            return loop.run_until_complete(future)

        def async_map_g(f, iterable):
            group = Group()
            return group.map(f, iterable)

        def async_map_m(f, iterable):
            with ThreadPool(processes=multiprocessing.cpu_count()) as pool:
                results = pool.map(f, iterable)
            return results

        def map(f, iterable):
            return map(f, iterable)

        return async_map_g(f,iterable)