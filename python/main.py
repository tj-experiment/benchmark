import time

import duration as duration
import elapsed as elapsed


def main():
    start = time.monotonic_ns()
    for i in range(10_000_000):
        continue

    end = time.monotonic_ns()
    elapsed = end - start // 1000000

    print(f"Took: {elapsed} milliseconds")

    with open('output.txt', 'a+') as f:
        f.write("%s\n" % elapsed)


if __name__ == "__main__":
    main()