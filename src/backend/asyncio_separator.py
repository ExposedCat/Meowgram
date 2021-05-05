import asyncio
import threading


class AsyncioEventLoopThread():

    loop = None
    thread = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop = asyncio.new_event_loop()

    def run_loop(self):
        self.loop.run_forever()

    def run_thread(self):
        self.thread = threading.Thread(target=self.run_loop)
        self.thread.start()

    def run(self, function, args):
        return asyncio.run_coroutine_threadsafe(function(*args), self.loop)


aio = AsyncioEventLoopThread()
aio.run_thread()
