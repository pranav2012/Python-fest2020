#!/usr/bin/env python3

import argparse
import random
import matplotlib.pyplot as plt


def fern(array, iterations):
    for i in range(iterations):
        x = array[i][0]
        y = array[i][1]

        probability = random.random()
        if probability < 0.01:
            array.append(_func1(x, y))
        elif probability > 0.01 and probability < 0.85:
            array.append(_func2(x, y))
        elif probability > 0.05 and probability < 0.92:
            array.append(_func3(x, y))
        else:
            array.append(_func4(x, y))
    return array


def _func1(x, y):
    return [(0 * x), (0.16 * y)]


def _func2(x, y):
    return [(0.85 * x + 0.04 * y), (-0.04 * x + 0.85 * y + 1.60)]


def _func3(x, y):
    return [(0.20 * x - 0.26 * y), (0.23 * x + 0.22 * y + 1.60)]


def _func4(x, y):
    return [(-0.15 * x + 0.28 * y), (0.26 * x + 0.24 * y + 0.44)]


def plot(array):
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Barnsley Fern")

    for i in range(len(array)):
        plt.scatter(array[i][0], array[i][1])
    plt.show()


def to_file(array):
    with open("b-fern-py.data", "a") as file:
        for i in range(len(array)):
            x = array[i][0]
            y = array[i][1]
            newline = str(x) + ", " + str(y) + "\n"
            file.write(newline)


def main():
    parser = argparse.ArgumentParser(description="Create a Barnsley Fern")
    parser.add_argument(
        "--tofile", action="store_true", help="store output to a csv file",
    )
    args = parser.parse_args()
    array = [[0, 0]]
    if args.tofile:
        to_file(fern(array, 10000))
    else:
        plot(fern(array, 10000))


if __name__ == "__main__":
    main()
