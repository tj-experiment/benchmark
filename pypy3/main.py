import time

def main():
    start = time.monotonic()
    for i in range(10_000_000):
        continue

    end = time.monotonic()
    elapsed = (end - start) * 1000

    print(f"Took: {elapsed} milliseconds")

    with open('output.txt', 'a+') as f:
        f.write("%s\n" % elapsed)


if __name__ == "__main__":
    main()