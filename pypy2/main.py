import time


def main():
    start = time.time()
    for i in range(10000000):
        continue

    end = time.time()
    elapsed = (end - start) * 1000

    print("Took: {} milliseconds".format(elapsed))

    with open('output.txt', 'a+') as f:
        f.write("%s\n" % elapsed)


if __name__ == "__main__":
    main()