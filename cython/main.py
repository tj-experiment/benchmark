import time

import loop

start = time.monotonic_ns()
loop.loop()
end = time.monotonic_ns()
elapsed = end - start//1000000

print(f"Took: {elapsed} milliseconds")

with open('output.txt', 'a+') as f:
    f.write("%s\n" % elapsed)