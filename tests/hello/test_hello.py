#!/bin/python3
import pytest

from project.hello import hello, main


def test_hello():
    assert hello() == "Hello, world!"


def test_hello_input():
    assert hello("test") == "Hello, test!"


def test_main(capsys):
    main("main")
    captured = capsys.readouterr()
    assert captured.out == "Hello, main!\n"
