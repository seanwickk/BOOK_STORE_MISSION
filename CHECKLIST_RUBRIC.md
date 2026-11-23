# Checklist & Rubric: 5-Day Sprint

This file has four parts:

1. **MVP checklist:** the minimum to pass.
2. **Above & Beyond:** optional stretch work.
3. **Day-by-day plan:** what to do each day of the sprint.
4. **Rubric:** how your project is graded.

## MVP checklist

The minimum for a complete, passing project. It's the same list as the
MVP checklist in the LMS.

- [ ] **Scenario chosen** from `PROJECT_OVERVIEW.md`, **with the other 3 data
  files deleted**.
- [ ] **Assumptions written down** (Question, Assumption, Risk) in
  `REFLECTION.md`, including what counts as low stock.
- [ ] **Your own class**, with attributes that fit your stakeholder's
  need, used throughout (no separate lists or dicts holding the same
  data).
- [ ] **At least 2 standalone functions** (not methods) with clear
  parameters and a `return`. `print_summary` is the only exception.
- [ ] **Batch processing:** a loop applies the `ADD`, `REMOVE`, and
  `SEARCH` lines from your data file.
- [ ] **At least 3 different types of edge case** handled without
  crashing. Each one is skipped with a specific printed reason or fixed on
  purpose.
- [ ] **At least one `try`/`except`** for a quantity that isn't a number.
- [ ] **`find_item`** uses a linear scan or a dict lookup.
- [ ] **`print_summary`** prints every item and a separate low-stock list.
- [ ] **`export_to_json`** writes `inventory.json` and is called by your
  script.
- [ ] **Docstrings you wrote yourself** on every function and method.
- [ ] **`REFLECTION.md` complete:** all six sections.
- [ ] **Your own `README.md`**, covering:
  - title and one-line summary
  - business scenario
  - what it does
  - findings
  - key decisions
  - how to run it
  - reflection
- [ ] **Clean submission:** no leftover `TODO`s, debug `print()`s, or
  unused code. **Every Instructions block deleted from `REFLECTION.md`.**
  **School-facing files deleted (`CHECKLIST_RUBRIC.md` and `PROJECT_OVERVIEW.md`), and `starter/`
  renamed to `analysis/`.**
- [ ] **Public GitHub repo** with at least 3 commits with clear messages.
- [ ] **Day 5 share-out:** a pair repo review and a 90-second PREP
  walkthrough. Not graded.

`tools/search.html` is optional.

## Above & Beyond (optional)

These go beyond what was taught in class, on purpose. You'll need to
research them yourself. Each one has a starting link. A complete MVP
without any of these is still a full, passing submission. Pick one or two
if you have time.

**Use AI to learn, not to do it for you.** Ask it to explain a concept,
give you a small example on different data, or review code you wrote.
Don't paste in the task and copy the answer. In `REFLECTION.md`, add a
short note on what you looked up and what you learned.

**Some items use given code that isn't in your repo.** It lives in the
`above_and_beyond/` folder on the `project-scope` branch of the original
template repo. Go to the template on GitHub, switch to that branch, and
copy the file you need.

- [ ] **Prove your Big-O answer with timing.** Write a second `find_item`
  that uses the other approach (dict if you used a list, or the reverse).
  Build a much bigger inventory, time both versions, and report the real
  numbers in `REFLECTION.md`. You practiced the pieces in the Lookups
  Matter and Stress-Test labs.
  Start here: [Python docs: `time.perf_counter`](https://docs.python.org/3/library/time.html#time.perf_counter)
  and [Python tutorial: dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).
- [ ] **Debug `above_and_beyond/debug_challenge.py`.** It's a short
  grade-tracking script with 3 bugs and no hints. Find each bug, name the
  exact line and what's wrong, fix it, and write it up in
  `REFLECTION.md`.
  Start here: [Python Tutor](https://pythontutor.com/) (step through
  the code line by line) and [Python tutorial: errors and exceptions](https://docs.python.org/3/tutorial/errors.html).
- [ ] **Handle a 4th type of edge case** from `data/SOURCE.md`, beyond
  the 3 the MVP requires.
- [ ] **Extend `tools/search.html`.** This means learning some JavaScript.
  Add sorting, a filter by one of your attributes, or a count of low-stock
  items at the top. Note what you changed in `REFLECTION.md`.
  Start here: [MDN: JavaScript first steps](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting)
  and [MDN: `Array.prototype.sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort).
- [ ] **Preview Module 2 with pandas.** Copy
  `above_and_beyond/preview_pandas.py` into your repo's top folder and run
  `python3 preview_pandas.py` (install pandas first with
  `pip install pandas`). In `REFLECTION.md`, write 1-2 sentences comparing
  its output to your own summary. What did pandas do with the bad lines
  that your code handled differently?
  Start here: [pandas: 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html).

## Day-by-day plan

**4 build days, then a share-out day.** Work through the items in order.

### How the sprint works

A sprint is a short, fixed block of time. A team commits to a set of work,
builds it, then stops and shows what they built. Professional software
teams plan their work this way. This project is your first sprint.

- **Sprint planning (Day 1):** understand the goal before you write code.
  The scope is already set (the MVP checklist at the top of this file). Your job is to
  understand it.
- **Daily check-in:** at the start of each build day, answer three
  questions in 2 minutes. What did I finish yesterday? What am I doing
  today? Is anything blocking me?
- **Backlog:** useful work that is deliberately left out of this sprint.
  The Above & Beyond section near the top of this file is your backlog.
- **Sprint review (Day 5):** you show working code to your classmates. It
  isn't a status update.

### Day 1: Plan and build your class

- [ ] Create your repo from the template with **"Use this template"** (not
  Fork) and clone it. See `README.md`.
- [ ] Confirm `.gitignore`, `LICENSE`, and the git history are there.
  Replace `[YOUR NAME]` in `LICENSE` with your name and commit.
- [ ] Check Python works: `python3 --version`.
- [ ] Read all 4 scenarios in `PROJECT_OVERVIEW.md`. **Pick one and delete the
  other 3 data files**.
- [ ] Read `starter/REFLECTION.md` so you know what you'll need to explain
  at the end.
- [ ] Write your QAR assumptions in the "Assumptions" section of
  `REFLECTION.md`. Include at least what counts as "low stock."
- [ ] Sketch your class's attributes on paper or in a scratch file, based
  on your stakeholder's words.
  - Common mistake: choosing attributes that don't answer your
    stakeholder's question, or copying them from another scenario.
- [ ] Trace the first 3 lines of your data file by hand. What makes an
  `ADD` line valid or invalid?
- [ ] Write `__init__` to store your attributes, and an `is_low_stock`
  method that uses your assumption.
- [ ] Create 2 objects and change one. Confirm the other one didn't
  change.
- [ ] Write a docstring for the class and each method in your own words.
- [ ] Commit: `git commit -m "add [scenario] item class"`.

### Day 2: Read and validate lines

- [ ] `read_batch_file` reads your data file and returns a list of lines.
- [ ] `validate_line` tells a valid `ADD`, `REMOVE`, or `SEARCH` line from
  an invalid one. Test it on 3 to 5 lines you copy from the data file
  before running the whole file.
- [ ] Use at least one `try`/`except ValueError` for a quantity that isn't
  a number.
- [ ] Write a docstring for each function in your own words.
  - Common mistake: writing one long function that reads, validates, and
    prints. Keep each function to one job.
- [ ] Commit: `git commit -m "add batch file parsing and validation"`.

### Day 3: Process the real file and handle edge cases

- [ ] `process_transactions` loops over every line in your data file and
  updates a collection of your objects. `ADD` creates or restocks an item,
  `REMOVE` lowers its quantity, and `SEARCH` looks one up.
- [ ] `find_item` finds an item by name with either a linear scan or a
  dict lookup. Pick one.
- [ ] Handle at least **3 different types** of edge case from
  `data/SOURCE.md`. Each one either skips the line with a specific printed
  reason or fixes it on purpose. The script must not crash.
  - Common mistake: letting one bad line crash the whole script. Run the
    full file, not just the lines that work.
  - Common mistake: keeping item data in separate lists instead of using
    your class.
- [ ] Commit: `git commit -m "process real batch file, handle edge cases"`.
- [ ] Push. By the end of Day 3 you should have at least 3 commits on
  GitHub.

### Day 4: Finish, reflect, write your README

- [ ] `print_summary` prints every item and then a separate low-stock
  list.
- [ ] `export_to_json` writes `inventory.json`, and your script calls it.
- [ ] Optional: check your results with `tools/search.html`. This is a
  small web page (given code) that reads your `inventory.json` and filters
  your items as you type. To open it, run `python3 -m http.server` in your
  repo's top folder, then go to `http://localhost:8000/tools/search.html`
  in your browser. Press `Control+C` in Terminal to stop the server.
- [ ] Fill in every section of `REFLECTION.md`: assumptions, edge cases,
  function scope, Big-O, AI-assisted edge-case discovery, and one real AI
  prompt, checked.
  - Common mistake: a Big-O answer copied from a textbook that doesn't
    mention your own `find_item`.
  - Common mistake: an AI answer with no specific way to check what the AI
    suggests.
- [ ] **Delete every Instructions (delete before your final push) block
  and every `_TODO_` in `REFLECTION.md`.** Keep the `##` headings and
  your own answers.
- [ ] Clean up: no leftover `TODO` comments, placeholder docstrings, debug
  `print()` lines, or unused variables.
- [ ] Replace the text of `README.md` with your own project README. Write
  it for an employer who has never seen this assignment and will skim it
  in under a minute:
  - **Title and one-line summary:** what you built and for whom.
  - **Business scenario:** your stakeholder, their problem, and why it
    matters to them.
  - **What it does:** what the script does with the transaction file.
  - **Findings:** what your run showed. For example, how many lines were
    skipped and why, and which items are low on stock. Use your real
    output.
  - **Key decisions:** your class attributes and why, your main
    assumption, and your search approach with its Big-O.
  - **How to run it:** the exact command.
  - **Reflection:** 2 or 3 bullets on what you learned and what you'd
    improve next. Link to `analysis/REFLECTION.md` for the full version.
- [ ] **Delete `CHECKLIST_RUBRIC.md` (this file) and `PROJECT_OVERVIEW.md`.** They're school-facing, not
  employer-facing, and stay available in the LMS.
- [ ] **Rename the `starter` folder to `analysis`** with
  `git mv starter analysis`. Then run `python3 analysis/inventory.py` once
  to confirm it still works.
- [ ] Final push. Open your repo in a private browser window to confirm
  it's public.

### Day 5: Share-out

No slides. You'll do two things in class, in TIP style:

- **Pair repo review.** You and a partner review each other's repo and
  code against the checklist in the share-out handout, then trade one
  strength and one fix.
- **90-second project walkthrough.** Answer "Walk me through your
  project" using PREP (Point, Reason, Example, Point). Your instructor
  times it and stops you at 110 seconds. Classmates score each part of
  PREP and give feedback, then you try again.

To prepare:

- [ ] Your README is finished. Its summary, business scenario, and key
  decisions are your talking points.
- [ ] Practice your walkthrough out loud once with a timer. Aim for 90
  seconds.
- [ ] After the share-out, write your improvement plan in the share-out
  handout and **push those fixes within 48 hours**.

---

## Rubric

**Point scale:** Below Expectations = 1, Approaching = 2, Meets = 4,
Exceeds = 5 (extra credit; most Exceeds levels require Above & Beyond
work). 5 skills × 4 points = **20 points at Meets**.

Your instructor grades your script, `REFLECTION.md`, your own `README.md`,
and your commit history together. Exceeds levels point to the Above &
Beyond section above. The Day 5
share-out is practice and isn't graded.

There's no single correct class. You're graded on whether your attributes
fit **your** stakeholder's need and whether you use the class
consistently.

---

### Technical Skills

#### `control-flow-loops`

*Using loops and conditionals that branch on real conditions in the data,
not just the happy path.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus handles a **4th** type of edge case beyond the 3 the MVP requires (Above & Beyond). |
| **Meets** | 4 | The loop correctly applies `ADD`, `REMOVE`, and `SEARCH` lines from the student's 430-line data file, **and** handles **at least 3 different types** of edge case from `data/SOURCE.md` without crashing. Each one either skips the line with a specific printed reason or fixes it on purpose. Three lines of the same type count as one. |
| **Approaching** | 2 | Works on well-formed lines but crashes or gives wrong results on 1-2 of the required edge cases, or fewer than 3 different types are handled. |
| **Below Expectations** | 1 | The script crashes on the full data file, or only the happy path was tested. |

#### `functions-modular-programming`

*Breaking a script into small, single-purpose functions with clear
parameters and return values.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the function-scope explanation in `REFLECTION.md` connects to something concrete from the student's own debugging, not just the definition. |
| **Meets** | 4 | (1) At least 2 standalone functions (not methods) with clear parameters and an explicit `return`; `print_summary` is the only exception. (2) **Every function and method has a docstring the student wrote**; the one given example doesn't count. (3) `REFLECTION.md` explains, in the student's own words, why a local variable doesn't leak out of its function. |
| **Approaching** | 2 | Functions exist but mix jobs (e.g. one function reads the file *and* prints the summary), some docstrings are missing or templated, or the scope explanation is vague or wrong. |
| **Below Expectations** | 1 | All logic in one long block with no real functions, docstrings mostly missing, or the scope explanation is missing or copied. |

#### `object-oriented-programming`

*Bundling related data and behavior into a class, and deciding what
belongs on that class for a real need.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the class has additional behavior clearly motivated by the stakeholder's stated need, not just extra attributes. |
| **Meets** | 4 | The attributes are a reasonable answer to *this* stakeholder's need, and the README's "Key decisions" section explains why. `__init__` stores them; `is_low_stock` works and uses a stated assumption (`REFLECTION.md`, "Assumptions"); multiple instances hold independent values; the class is used throughout, with no parallel lists or dicts holding the same data. |
| **Approaching** | 2 | The class is mostly used, but the attributes don't clearly connect to the stakeholder's need (e.g. bookstore-style fields in a healthcare scenario), the low-stock rule has no stated assumption, or some item data is kept in a parallel structure. |
| **Below Expectations** | 1 | Item data lives in loose lists or dicts instead of a class, or the core methods are missing or wrong. |

#### `algorithmic-complexity-big-o`

*Reasoning about how runtime changes as the input grows.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Implemented **both** a linear scan and a dict lookup and timed them on a larger inventory, with real numbers in `REFLECTION.md` (Above & Beyond). |
| **Meets** | 4 | `REFLECTION.md` correctly labels the student's own `find_item` as O(n) (linear scan) or O(1) average (dict lookup) and explains, using their own code, why it matters as the inventory grows. |
| **Approaching** | 2 | The label is wrong for what the code does, or the explanation is a textbook definition not tied to their own `find_item`. |
| **Below Expectations** | 1 | No real Big-O reasoning, or it has nothing to do with the actual search code. |

---

### Professional Skills

#### `attention-to-detail`

*Catching subtle mistakes, checking your own work before calling it done,
and using AI to find more problems without trusting it blindly.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Completed the `debug_challenge.py` exercise: found and named all 3 bugs at the exact line, fixed them, and confirmed the corrected output (Above & Beyond). |
| **Meets** | 4 | All 3: (1) no leftover debug `print()`s, `TODO`s, or unused variables, school-facing files removed, every Instructions block deleted from `REFLECTION.md`, and `starter/` renamed to `analysis/`; (2) `REFLECTION.md` lists 3 different edge cases with the exact line and what the code does, and the README's "Findings" section reports what the real run printed (e.g. how many lines were skipped and why); (3) the "AI-assisted edge-case discovery" section names a specific prompt **and** a specific check the student would run before trusting the suggestions. "Ask AI for edge cases" with no check doesn't meet this bar. |
| **Approaching** | 2 | 1-2 of the 3 criteria are met. For example, edge cases are handled but the README's findings don't show it, or the AI section names a prompt but no check. |
| **Below Expectations** | 1 | Leftover debug code, fewer than 3 different edge cases, or generic AI answers ("AI would help me find bugs"). |

### Reflection AI line (formative)

*Did you ask the AI well, and check what it gave you?* This covers
`REFLECTION.md`'s "One real AI prompt, checked" section. It's scored and
you get feedback on it, but it doesn't count toward the five skill scores
above. Didn't use AI? You can still earn Meets: write the prompt you would
have used, label it "not sent," and run the same check on your own code.

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you show a second version of the prompt and say what you changed and why (compare and optimize). Or your check caught a real flaw in the AI's answer, and you explain what you fixed. |
| **Meets** | 4 | One real prompt from your sprint, pasted word for word. You name at least one technique it uses and point to where it appears in the prompt. You show what came back, trimmed but not reworded. You checked it one concrete way: a case you worked by hand, a test you wrote, or re-running on your data file. You say what the check showed. |
| **Approaching** | 2 | The prompt is pasted, but the technique is named without pointing to where it shows up. Or the check is vague, such as "it looked right" or "it ran." Or the prompt was clearly rewritten after the fact. |
| **Below Expectations** | 1 | No prompt. Or a prompt with no output and no check. Or the AI's answer is accepted with no verification at all. |

### Common mistakes that cost points

1. One long function that reads, validates, and prints, instead of
   separate functions.
2. One bad line crashes the whole script.
3. Item data kept in separate lists instead of your class.
4. Only testing lines that work. Run the full file.
5. Copying another scenario's attributes, such as a healthcare inventory
   that tracks "genre."
6. Claiming edge cases in `REFLECTION.md` that your README's findings and
   real output don't back up.
