"""
Command-line inventory tracker -- you choose the scenario.

See ../PROJECT_OVERVIEW.md to pick your stakeholder and data file. Design your own
class for one inventory item, based on what *your* stakeholder needs.
There's no single right set of attributes, and that's on purpose.

Run it from your repo's top folder (not from inside this folder):
    python3 starter/inventory.py
Before your final push you'll rename this folder to analysis/.
"""





class Book_Smart:
    """
    TODO: rename this class to something that fits your scenario, and
    write a real docstring. What does one of these represent? At minimum
    you'll need a name and a quantity. Add what your stakeholder asked
    for, not more and not less.
    """

    def __init__(self,commands,item,quantity,category):
        self.commands = commands
        self.item = item  
        self.quantity = quantity
        self.category = category # Each required field list on Bookstore/.txt_FILE



    def is_low_stock(self):
        if self.quantity <= 5:
            return True
        return False
        """ Evaluating Notable Low Book Stock"""




book_watch = Book_Smart("ADD", "RISE and fallen", 5, "Gothic")

print( "Is this book low on stock?", (book_watch.is_low_stock()), "!")

def read_batch_file(filepath):
    '''Creating list for txt.file'''
    with open(filepath) as f:
        books = [line for line in f.read().splitlines()] 
    return books
print(read_batch_file("bookstore_transactions.txt"))






def validate_line(line):
    """ Validating list since edge cases errors"""
    """TODO: write your own docstring. What makes an ADD, REMOVE, or
    SEARCH line valid? What do you return for a valid line, and what for
    an invalid one?"""
    parts = line.strip().split()

    if not parts:
        return False
    commands = parts[0]
######ADD######
    if commands == "ADD":
        if len(parts) != 4:
            return False, "False field amount"
        try: 
            if parts[2].isdigit:
                return None
        except:
            KeyError
            return "String formatting is invalid retry"
#####REMOVE#####
    if commands == "REMOVE":
        if len(parts) != 3:
            return False, "False field amount"
        try: 
            if parts[2].isdigit:
                return None
        except:
            KeyError 
            return "String formatting is invalid retry"
        if parts[2] <=100:
            return  False, "key Error amount can not be negative"

#####SEARCH#####
    if commands == "SEARCH":
        if len(parts) != 2:
            return False, "False field amount"
        
#### Missed key value ###


    
        
        





           
    

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
