import asyncio
import threading

asyncio_loop = None


def start_asyncio_loop():
    global asyncio_loop
    asyncio_loop = asyncio.new_event_loop()
    asyncio_loop.run_forever()


asyncio_thread = threading.Thread(target=start_asyncio_loop)
asyncio_thread.start()


def async_run(function, args):
    return asyncio.run_coroutine_threadsafe(function(*args), asyncio_loop)
