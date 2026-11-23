# Data Source

Four batch files, one per scenario in `PROJECT_OVERVIEW.md`. Each is 430 lines of
transactions for a fictional business. They're not from a public dataset.
Bookstore item names are real public-domain book titles (via
[Project Gutenberg](https://www.gutenberg.org/), used only as names). The
other three files use plain, generic item names, not any real company's
catalog.

| File | Items | Categories |
|---|---|---|
| `bookstore_transactions.txt` | 25 titles | Adventure, Classic, Fantasy, Gothic, Mystery, Romance, Science Fiction |
| `restaurant_transactions.txt` | 28 items | Dairy, Dry Goods, Produce, Protein |
| `healthcare_transactions.txt` | 26 items | Equipment, Medication, PPE, Wound Care |
| `athletic_transactions.txt` | 26 items | Accessories, Apparel, Equipment, Footwear |

Item counts are the distinct names after normalizing case and stray
spaces.

430 lines is on purpose: it's too long to check by eye, so you need code
to find the problems.

## Edge cases: the same in every scenario

**All four files contain the same 11 types of edge case.** Only the item
names and line numbers differ. Whichever scenario you pick, you're
looking for the same kinds of problems.

| # | Edge case | Planted lines | Example (bookstore) |
|---|---|---|---|
| 1 | Blank line | 2 | *(an empty line)* |
| 2 | `ADD` with an empty quantity | 1 | `ADD,Moby-Dick,,Adventure` |
| 3 | `ADD` with a quantity that isn't a number | 2 | `ADD,Little Women,five,Classic` (the other uses `N/A`) |
| 4 | `REMOVE` for an item that was never added | 2 | `REMOVE,Nonexistent Item Nobody Ever Added,3` |
| 5 | `REMOVE` for more than is in stock | 1 planted, plus more (see below) | `REMOVE,Alice's Adventures in Wonderland,9999` |
| 6 | Lowercase command | 1 | `add,Dracula,5,Gothic` |
| 7 | Misspelled command | 1 | `ADDD,War and Peace,5,Classic` |
| 8 | Extra spaces around the item name | 1 | `ADD,  The War of the Worlds  ,7,Science Fiction` |
| 9 | Too many fields | 1 | `ADD,The Picture of Dorian Gray,7,Gothic,extra,fields` |
| 10 | `REMOVE` with no quantity field | 1 | `REMOVE,Emma` |
| 11 | `SEARCH` with an empty item name | 1 | `SEARCH,` |

**The one difference between scenarios is #5.** Besides the planted
`9999` line, normal `REMOVE` lines sometimes ask for more than is left
once an item's stock runs low. How often depends on the file:

| Scenario | "REMOVE more than in stock" lines, including the planted one |
|---|---|
| Restaurant | 6 |
| Bookstore | 9 to 11 |
| Healthcare | 12 to 14 |
| Athletic | 12 to 14 |

The exact count depends on your design choice. If your code skips an
over-sized `REMOVE`, you get the lower number. If it sets the quantity to
0 instead, you get the higher number. Both are fine if your code prints a
message and `REFLECTION.md` explains the choice.

## What "handled" means

You need to handle **at least 3 different types** from the table, not the
same type three times. A type is handled when your code does one of two
things on purpose, without crashing:

- **Skips the line and prints a specific reason**, such as
  `SKIPPED - quantity is not a whole number: ADD,Little Women,five,Classic`.
- **Fixes the line and uses it**, such as uppercasing `add` or stripping
  the extra spaces. Say in `REFLECTION.md` that you chose to fix it rather
  than skip it.

Don't edit the data file to remove problem lines. Everyone who picks the
same scenario tests against the same file.
