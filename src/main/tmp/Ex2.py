#$end

from tqdm import tqdm, trange
from time import sleep
import chime

chime.theme('mario')
chime.notify_exceptions()

# More about tqdm at https://pypi.org/project/tqdm/#iterable-based

# for i in trange(1000):
#     sleep(0.001)

# pbar = tqdm(total=100)
# for i in range(10):
#     sleep(0.1)
#     pbar.update(10)
# pbar.close()

pbar = tqdm(["a", "b", "c", "d", "e", "f", "g", "h", "i"], colour='green', desc='Processing...')
for char in pbar:
    sleep(0.5)
    pbar.set_description("Processing %s" % char)

# with tqdm(total=100) as pbar:
#     for i in range(10):
#         sleep(0.1)
#         pbar.update(10)

chime.success()


