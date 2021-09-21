import time

import loop

start = time.monotonic()
loop.loop()
end = time.monotonic()
elapsed = (end - start) * 1000

print(f"Took: {elapsed} milliseconds")

with open('output.txt', 'a+') as f:
    f.write("%s\n" % elapsed)