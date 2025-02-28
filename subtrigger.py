import asyncio


def run_echo():
    from subprocess import Popen, PIPE

    p = Popen(["echo", "Hello, world!"], stdout=PIPE)
    return p.communicate()[0]


async def main():
   return await asyncio.to_thread(run_echo)


def run_async_echo():
    return asyncio.run(main())
