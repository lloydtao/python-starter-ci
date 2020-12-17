#!/bin/python3
"""
Print a friendly statement to the console.
"""

import argparse


def hello(s="world"):
    message = "Hello, " + s + "!"
    return message


def main(word):
    output = hello(word)
    print(output)


if __name__ == "__main__":

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "word",
        help="customise the subject of the output message",
        nargs="?",
        default="world",
        type=str,
    )
    args = parser.parse_args()

    # Call main function
    main(args.word)
