"""
Command-line inventory tracker -- you choose the scenario.

See ../PROJECT_OVERVIEW.md to pick your stakeholder and data file. Design your own
class for one inventory item, based on what *your* stakeholder needs.
There's no single right set of attributes, and that's on purpose.

Run it from your repo's top folder (not from inside this folder):
    python3 starter/inventory.py
Before your final push you'll rename this folder to analysis/.
"""
import json


class YourInventoryItem:
    """
    TODO: rename this class to something that fits your scenario, and
    write a real docstring. What does one of these represent? At minimum
    you'll need a name and a quantity. Add what your stakeholder asked
    for, not more and not less.
    """

    def __init__(self):
        # TODO: add your own parameters (self, plus each attribute you're
        # tracking) and store each one as self.whatever = whatever.
        pass

    def is_low_stock(self):
        """TODO: write your own docstring."""
        # TODO: return True or False. Your stakeholder didn't say what
        # "low" means, so decide, and write down the assumption in
        # REFLECTION.md's "Assumptions" section.
        pass


def read_batch_file(filepath):
    """
    Read the batch file at `filepath` and return a list of its lines
    (strings), unchanged. Deciding whether a line is usable happens in
    validate_line(), not here. Use this docstring as the model for the
    ones you write below: what the function does, what it takes, and what
    it returns.
    """
    # TODO: implement
    pass


def validate_line(line):
    """TODO: write your own docstring. What makes an ADD, REMOVE, or
    SEARCH line valid? What do you return for a valid line, and what for
    an invalid one?"""
    # TODO: implement. One choice worth making on purpose: a quantity can
    # be present but not a number ("five"). Wrap int(quantity) in a
    # try/except ValueError. That asks Python "did this work?" instead
    # of trying to predict every way it could fail.
    pass


def process_transactions(lines):
    """TODO: write your own docstring."""
    # TODO: implement. Loop over the lines, apply each valid one to your
    # collection of items, and print a specific message for each line
    # you skip. Return the collection at the end. The full inventory
    # printout is print_summary's job, not this function's.
    pass


def find_item(items, name):
    """TODO: write your own docstring."""
    # TODO: implement
    pass


def export_to_json(items, filepath="inventory.json"):
    """TODO: write your own docstring. json.dump can't write your objects
    directly, so turn each one into a dict first."""
    # TODO: implement
    pass


def print_summary(items):
    """TODO: write your own docstring."""
    # TODO: implement. This one only prints, so it doesn't need to return
    # anything.
    pass


# TODO: point this at the data file for the scenario you chose.
lines = read_batch_file("data/____________.txt")
items = process_transactions(lines)
print_summary(items)
export_to_json(items)
