# Project 5: Tool Assistant

Function calling — letting the model request that my Python functions be run.

## What this covers

The model never runs code. It has no access to my machine or the network. What
it does is return a *request* — "call get_weather with city='Dublin'" — and my
code decides whether to run it, runs it, and sends the result back. The model
then writes its reply using that result.

That's why a model can "check the weather" without touching the internet: it
isn't checking anything, my function is.

## Files

**`tools.py`** — The Python functions the model can request. The docstrings and
type hints aren't decoration: they're the only description the model gets, so
vague ones lead to the wrong tool being picked or bad arguments being passed.

**`assistant.py`** — Passes the functions to `chats.create()`, which turns on
automatic function calling. The SDK handles the request/execute/respond loop.

## What surprised me

- **The model then invented an explanation.** Both times it told me there was a
  "temporary service error." There was no service and no error of that kind —
  it had no access to the exception, so it guessed the most plausible reason a
  weather lookup might fail. The explanation read like a diagnosis and was
  fiction.
- **A broken tool gets retried.** One run showed `get_weather` firing twice
  before the model gave up, costing tokens on a call that could never succeed.
- **Print statements inside tools are the only reliable proof they ran.** In one
  run the debug line vanished entirely, which was the only signal that the tool
  wasn't being called at all.

## The principle

Fluency is not evidence. A confident, well-formatted answer says nothing about
whether the pipeline underneath it worked. Everything crossing the boundary
between my code and the API needs to be logged, because that's the only part I
can actually observe.
