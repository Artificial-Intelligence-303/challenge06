# Challenge 6: An Agent That Decides by Expected Utility

|                    |                                             |
| :----------------- | :------------------------------------------ |
| `Tuesday 27 Oct`   | Released, in lab                            |
| `Thursday 5 Nov`   | Due at 11:00am, the start of class          |
| `Tuesday 10 Nov`   | Verbal checks, in lab                       |
| Points             | 3                                           |

A coding agent has just written a change. It estimates how likely the
change is to be buggy, and then it has to do something: merge it, ask a
teammate to review it, or throw it away. Before acting it may run the
tests, which costs time, or a quick static checker. Whether running them
is worth it depends on whether their answer could change what the agent
does.

This is the choice every tool-using agent makes before it calls a tool,
and Challenge 7 builds one: is the answer worth what the call costs?

You write the three functions that make those decisions. The agent, its
utilities, its tools and the Bayes' rule step are provided.

## Course learning outcomes

1. **Outcome 1.** Correctly implement an intelligent agent and accurately
   describe its properties. You implement the decision rule of an agent
   that acts under uncertainty, and explain from its output when it looks
   before it acts.
2. **Outcome 5.** Evaluate intelligent systems while considering their
   social, political, and ethical implications. You change one of the
   agent's utilities and argue who that change protects and who it costs.

## The agent

| Piece        | In `src/agent.py`                                         |
| :----------- | :-------------------------------------------------------- |
| States       | the change is `correct` or `buggy`                        |
| Actions      | `merge`, `review`, `discard`                              |
| `UTILITIES`  | how much the team prefers each action in each state       |
| `TOOLS`      | `tests` and `lint`: P(result \| state) for each result    |
| `COSTS`      | what calling each tool costs, in the same units           |
| `CHANGES`    | five kinds of change and the agent's P(buggy) for each    |
| `next_step`  | calls the tool that gains the most over its cost, or acts |

Every number in `agent.py` is invented for this challenge.

## What you implement

Three functions in `src/decisions.py`. Everything else is provided. None of
them knows anything about code: each works for any states, any actions and
any tool, and the tests check that on a second problem.

### 1. `expected_utility(belief, utilities, action)`

The sum over states of P(state) times U(action, state).

### 2. `best_action(belief, utilities)`

The action with the highest expected utility, and that expected utility.
A tie goes to the action listed first.

### 3. `value_of_information(belief, utilities, tool)`

For each result the tool can give, its probability times the expected
utility of the best action after seeing it. Add those, then subtract the
expected utility of the best action now.

### Provided: `result_probability` and `posterior`

At the bottom of `decisions.py`. They are Challenge 5's law of total
probability and Bayes' rule, for one tool result: `result_probability`
gives P(result), and `posterior` gives the belief after seeing it. Call
both from `value_of_information`.

The docstring at the top of `decisions.py` shows the shape of every table.

### From the formula to code

Every formula here is a sum, and every sum becomes a loop: start a total at
0, loop over the states (or the results), and add one term each time.

| Formula | Python |
| :------ | :----- |
| P(s) | `belief[state]` |
| U(a, s) | `utilities[action][state]` |
| P(r \| s) | `tool[result][state]` |
| sum over states of ... | `for state in belief:` with `total += ...` |

Each function's docstring works one example by hand, with P(buggy) = 0.5.
Check each function against it as you go, before moving to the next: the
later functions call the earlier ones.

```
uv run python
>>> import sys; sys.path.insert(0, "src")
>>> from decisions import expected_utility
>>> from agent import UTILITIES
>>> expected_utility({"correct": 0.5, "buggy": 0.5}, UTILITIES, "merge")
-35.0
```

## Running it

```
uv run python src/main.py              every change, and the agent's next step
uv run python src/main.py risk 0.25    one change with P(buggy) = 0.25
uv run pytest                          run the tests
uv run ruff check src tests            check your style
uv run ruff format src tests           fix most style problems automatically
uv run gatorgrade                      run the checks the way they are graded
```

## Style

Same as last time: the [Google Python Style
Guide](https://google.github.io/styleguide/pyguide.html), checked by
`uv run ruff check src tests`.

## Evaluation

This challenge is worth **3 points**.

| Component                 | Value   |
| :------------------------ | :------ |
| Programming               | 1       |
| Written reflection        | 1       |
| Verbal check              | 1       |
| **Total**                 | **3**   |

### Programming, 1 point

Run by `gatorgrade`, awarded as the fraction of the **code** checks that
pass. These are:

- `expected_utility` and `best_action` give the right values and actions
  on the coding agent, on an umbrella problem, and with three states.
- `value_of_information` gives the right values, is 0 when no answer can
  change the action, and is never negative.
- The agent merges a typo fix without testing and runs the tests on a
  refactor.
- Style passes `ruff` and type annotations check out under `mypy`.
- No `TODO` markers are left in `src/decisions.py`.

`gatorgrade` also runs two checks on `docs/summary.md`. Those belong to the
reflection below, not to this point.

Autograder results are preliminary. The final grade is determined by the
instructor.

### Written reflection, 1 point

Complete `docs/summary.md`. Two questions and the disclosure, **200 words
minimum across all of them**. You are graded on whether the reasoning is
correct and specific to what your run printed, not on length.

### Verbal check, 1 point

During lab you answer two or three questions about your own code, in the
context of this assignment. Nothing to prepare beyond understanding what
you wrote.

## AI use on this challenge

Full policy: **[AI in this course](https://areweagentsyet.com/ai/)**. AI
tools are allowed here, you disclose them, and you have to be able to
explain what you submit.

> ### The skill this time: ask what the tool is assuming about people
>
> Every utility in this agent is a judgment about people: how much a bug
> costs the users, how much a review costs a teammate. When a tool, or an
> agent, gives you an answer, ask whose costs it counted and whose it left
> out.

Concretely, for this assignment:

- **Write the three functions yourself.** They are this week's idea.
- **Check one value of information by hand.** For "rename a variable",
  work out P(buggy) after a failing test and after a passing one, pick the
  best action for each, and compare with what `main.py` prints.
- **A tool is useful** for the Python around the decisions: how to find
  the key with the largest value in a dictionary, or how to build a new
  dictionary from an old one.

## How this assignment was built

You are asked below to disclose your AI use, so here is mine.

I decided the shape: an agent that acts on a belief, chooses between
acting now and calling a tool by the value of information, and has its
utilities written where you can change them.

I used Claude to draft `agent.py`, the tests and `main.py`, and to compute
every number the tests expect. I ran the reference solution and the
unfinished starter against every check, and checked the checks against
wrong versions of all three functions, not only against empty ones.

## Disclosing your AI use

At the end of `docs/summary.md` there is a disclosure section. Answer three
things, a sentence or two each:

1. **Which tool.** Name it. If you used more than one, name each.
2. **What you used it for.** Which part of the assignment.
3. **What you did with what it gave you.** Accepted it, edited it, checked
   it against something, or threw it out.

**If you did not use any tool, write that.** That is a complete and
perfectly good answer.

Disclosing costs you nothing. There is no version of this where naming a
tool loses you points.
