# Programming Fundamentals Project: Inventory Tracker

**Replace this README before submitting your final project with:**

- **Title and one-line summary:** what you built and for whom.
- **Business scenario:** your stakeholder, their problem, and why it
  matters.
- **What it does:** what your script does with the transaction file.
- **Findings:** what your real run showed, such as how many lines were
  skipped and why, and which items are low on stock.
- **Key decisions:** your class attributes and why, your main assumption,
  and your search approach with its Big-O.
- **How to run it:** the exact command.
- **Reflection:** 2-3 bullets on what you learned and what you'd improve,
  linking to `analysis/REFLECTION.md`.

Write it for an employer who has never seen this assignment.

---

## Setup

### 1. Start in a new folder

Work in a folder that is **not** inside an existing git repo. Check with:

```bash
git status
```

You want to see `fatal: not a git repository`. If you see a branch name
instead, `cd` somewhere else first, such as a new `marcy-projects` folder.

### 2. Use the template, not Fork

On this repo's GitHub page, click **"Use this template" → "Create a new
repository."** Don't click **Fork**: a fork stays linked to Marcy's repo,
and this project is yours. Name it something like `inventory-tracker` and
keep it **public**.

### 3. Clone your new repo

From **your** new repo's page (not the template), copy the HTTPS URL from
the green **Code** button:

```bash
git clone <the URL you copied>
cd <your-repo-name>
```

### 4. Check `.gitignore`

Your repo already has a `.gitignore`. Confirm it has these lines, or create
the file with them if it's missing:

```
.DS_Store
.vscode/
__pycache__/
*.pyc
.venv/
venv/
```

- `.DS_Store`: Mac folder files that have nothing to do with your project.
- `.vscode/`: your personal VS Code settings.
- `__pycache__/` and `*.pyc`: files Python generates when it runs your
  code.
- `.venv/` and `venv/`: a Python virtual environment, if you make one to
  install pandas for Above & Beyond.

Don't ignore `inventory.json`. It's your script's output, and it's part of
your project.

### 5. Put your name on the LICENSE

`LICENSE` is the MIT License, which lets others reuse your code with
credit. Open it and replace `[YOUR NAME]` with your name, then commit:

```bash
git add LICENSE
git commit -m "add my name to LICENSE"
```

## The project

- Pick your stakeholder in `PROJECT_OVERVIEW.md` **and delete the other 3 data
  files in `data/`**.
- Open `CHECKLIST_RUBRIC.md`. The MVP checklist at the top is the
  minimum to pass (it's also in the LMS), then Above & Beyond, then a
  day-by-day plan, and the rubric at the bottom.
- Write your code in `starter/inventory.py` and your reflection in
  `starter/REFLECTION.md`.
- Run your script from the repo's **top folder**, not from inside
  `starter/`, or Python won't find `data/`:

  ```bash
  python3 starter/inventory.py
  ```

- Commit as you go, not all at the end.

## Before you submit

Your final repo is for employers, not for school. Before your final push:

- **Delete `CHECKLIST_RUBRIC.md` and `PROJECT_OVERVIEW.md`.** They're school-facing and stay in the LMS.
- **Delete every Instructions (delete before your final push) block and
  every `_TODO_` in `starter/REFLECTION.md`.** Keep the headings and your
  answers.
- **Rename the `starter` folder to `analysis`:**

  ```bash
  git mv starter analysis
  ```

  Then run it with `python3 analysis/inventory.py`.
- Replace this README with your own, using the sections at the top.
