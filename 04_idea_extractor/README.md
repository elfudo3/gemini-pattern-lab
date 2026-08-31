# Project 4: Idea Extractor

Structured output — getting validated Python objects back instead of a blob of text.

## What this covers

Every project so far returned prose. Useful to read, painful to use in code: the
format drifts between runs, so any attempt to pull values out with string
parsing breaks. Structured output fixes that by sending a schema along with the
prompt, so the response is constrained to a shape I defined.

The key idea: one Pydantic class does three jobs at once. It's my Python data
type, it's the instruction to the model about what to produce, and it's the
validation of what comes back.

## Files

**`models.py`** — Defines the `Idea` class with Pydantic, describing the fields
each extracted action item should have and which ones are optional.

**`extract.py`** — Reads messy notes from a file, sends them with
`response_schema=list[Idea]`, and gets back real Python objects via
`response.parsed`.

**`sample_input.txt`** — Deliberately unstructured standup notes with implied
priorities and some items that have no owner.

## Running

From inside this folder, with the venv active:

    cd 04_idea_extractor
    python extract.py
