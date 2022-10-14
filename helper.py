"""
General Helper Functions
"""
from os import system
import time
from art import tprint


def main_title():
    """
    Prints the program's main title using print art
    """
    tprint("        Nick's")
    tprint("Practice")
    tprint("           Log")


def sleep():
    """
    Set a general timer to delay text printing
    """
    time.sleep(1.5)


def long_sleep():
    """
    Set a longer timer to delay text printing
    """
    time.sleep(2.5)


def short_sleep():
    """
    Set a longer timer to delay text printing
    """
    time.sleep(0.7)


def clear_screen():
    """
    Clear the user terminal
    """
    system('clear')
