import asyncio
from datetime import datetime
import colorama
import warnings
import random

warnings.filterwarnings("ignore", category=DeprecationWarning)

def main():
    loop = asyncio.get_event_loop()

    t0 = datetime.now()
    print(colorama.Fore.RED + "App started.", flush=True)
    data = asyncio.Queue()
    task1 = loop.create_task(generate_data(20, data))
    task2 = loop.create_task(generate_data(20, data))
    task3 = loop.create_task(process_data(40, data))
    final_task = asyncio.gather(task1, task2, task3)
    loop.run_until_complete(final_task)
    dt = datetime.now() - t0
    print(colorama.Fore.GREEN + "App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()), flush=True)
    print("App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()), flush=True)

async def generate_data(num: int, queue: asyncio.Queue):
    for idx in range(1, num+1):
        data = idx * idx, datetime.now()
        await queue.put(data)
        print(colorama.Fore.LIGHTYELLOW_EX + " -- generated item {}".format(idx), flush=True)
        await asyncio.sleep(random.random() + .5)

async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        value, time = await data.get()
        processed += 1
        dt = datetime.now() - time

        print(colorama.Fore.GREEN +
              " +++ Processed value {} after {:,.2f} sec.".format(value, dt.total_seconds()), flush=True)
        await asyncio.sleep(.5)

if __name__ == "__main__":
    main()

