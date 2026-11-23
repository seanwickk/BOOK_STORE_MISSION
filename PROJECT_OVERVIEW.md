# Project Overview: Inventory Tracker

## The objective

Pick one of 4 stakeholder scenarios (see **Choose your scenario** below) and build a
plain-Python command-line inventory tracker for them:

- **Design your own class** for one inventory item, based on what your
  stakeholder needs. There's no single right answer.
- **Write separate functions** to read and validate a 430-line batch file
  of `ADD`, `REMOVE`, and `SEARCH` transactions.
- **Handle at least 3 different types** of bad input without crashing.
- **Export your results** to `inventory.json`.
- **Write a reflection** on your assumptions, your edge cases, scope,
  Big-O, and how you'd use AI to find more edge cases and check what it
  tells you.
- **Write a README an employer can read**, then share your project out
  loud on Day 5.

## Why it matters

This is the first project where you write real code. Module 0 was
terminal-only. No one hands you the data model this time. Deciding what
to track for a real problem is a core analyst skill. You'll keep using
the habits from this project for the rest of the program: designing a
class, validating messy input, and checking AI's answers instead of
trusting them. Python comes back in **Module 3**, and in **Module 4**
you'll combine it with SQL.

## Choose your scenario

Pick **one** of the four scenarios below. Each one gives you a stakeholder,
what they need, and a batch file of 430 transactions in `data/`. **Once you
choose, delete the other three data files from your repo**.

### What the data gives you

Every data file has the same format, one transaction per line:

```
COMMAND,item name,quantity,category
```

- `COMMAND` is `ADD`, `REMOVE`, or `SEARCH`.
- `ADD` lines have all four fields. `REMOVE` lines have three (no
  category). `SEARCH` lines have two (just the item name).
- That's all the data there is. Everything your stakeholder asks for below
  can be answered with these fields. You don't need to invent new ones.

None of the scenarios tell you what attributes your class needs. Choosing
them from what your stakeholder says is part of the assignment.

### Option 1: Bookstore Inventory

**Stakeholder:** Maya, who owns a small independent used bookstore.

> "I'm still tracking my inventory in a notebook and it's a mess. I need
> to know how many copies of each title I have, look up a title fast when
> a customer asks, and get a warning before I run out of something. I
> shelve by genre, so it helps to see that too."

**Data:** `data/bookstore_transactions.txt`

### Option 2: Restaurant Kitchen Inventory

**Stakeholder:** Diego, kitchen manager at a mid-size restaurant.

> "We run out of things mid-service and it's always a scramble. I need to
> know what's low *before* dinner rush, not during it. I think about stock
> by section: produce, protein, dairy, dry goods. I don't care about a
> fancy interface. I care about not getting caught short on a Friday
> night."

**Data:** `data/restaurant_transactions.txt`

### Option 3: Healthcare / Medical Supplies Inventory

**Stakeholder:** Priya, supply coordinator at a community health clinic.

> "If we run out of gloves or gauze mid-appointment, that's a real
> problem, not an inconvenience. I need to know what's running low in
> each supply category. And if a line in our log is wrong, I need to know
> about it. It can't quietly change our counts."

**Data:** `data/healthcare_transactions.txt`

### Option 4: Athletic Wear / Sporting Goods Inventory

**Stakeholder:** Jordan, manager at a local sporting goods store.

> "Customers ask for a specific size. Our system already lists each size
> as its own item, like `Running Shoes (M)` and `Running Shoes (W)`. I
> need to know what's in stock, what's almost out, and I need to look
> something up fast when someone's standing at the counter."

**Data:** `data/athletic_transactions.txt`

### Before you write code: Question, Assumption, Risk

Stakeholders rarely tell you everything. Use QAR, the TIP framework,
to write down what you don't know. Do this before you code. Record it
in the "Assumptions" section of `starter/REFLECTION.md`.

- **Question:** what didn't your stakeholder say that your code still
  needs to decide? For example, none of them say how many units count
  as "low."
- **Assumption:** what will you assume for now? For example, "Low means
  fewer than 5 units."
- **Risk:** what goes wrong if your assumption is wrong, and how would
  you check it? For example, ask the stakeholder, or look at how much a
  typical `REMOVE` line takes out in your data file.

Then re-read your stakeholder's words. What would you need to track to
answer their questions? Sketch your class from that, not from what a
spreadsheet usually has.

## Deliverables at a glance

- A **public GitHub repo** created with "Use this template" (not Fork).
- One scenario chosen below, **with the other 3 data files
  deleted**.
- `starter/inventory.py` complete (**renamed to `analysis/` before your
  final push**). It needs:
  - your own class and the batch-file functions
  - docstrings you wrote yourself
  - at least one `try`/`except`
  - a call to `export_to_json`
- At least **3 different types** of edge case handled. They must be real
  lines in your data file.
- `starter/REFLECTION.md` complete, with all six sections and **every
  Instructions (delete before your final push) block deleted**.
- Your own **README.md** replacing this template's, with these sections:
  title and one-line summary, business scenario, what it does, findings,
  key decisions, how to run it, and reflection.
- At least **3 commits** with clear messages.
- **Day 5 share-out:** a pair repo review and a 90-second project
  walkthrough. No slides.

## Skills you'll practice

- **Control flow:** loops and conditionals that handle messy input, not
  just the happy path.
- **Functions and modular programming:** small functions, each with one
  job, clear inputs, and a return value.
- **Object-oriented programming:** deciding what data and behavior belong
  in a class for your scenario.
- **Algorithmic complexity (Big-O):** how your code's runtime changes as
  the data grows.
- **Attention to detail:** finding real problems in a file too long to
  check by eye, and showing proof you handled them.

## Above & Beyond (optional)

Finished the MVP with time to spare? The Above & Beyond section in
`CHECKLIST_RUBRIC.md` has 5 stretch items. They go past what
was taught in class, so you'll research them yourself, with starter
links. None are required.

## Timeline

5 days: 4 build days and a share-out day. See `CHECKLIST_RUBRIC.md`.

## Where to start

Go to `README.md`. It walks you through setting up your repo.
