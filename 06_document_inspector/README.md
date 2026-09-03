# Project 6: Document Inspector

Multimodal input — sending images and PDFs alongside a text prompt.

## Files

**`inspect_image.py`** — Reads an image as bytes and sends it with
`types.Part.from_bytes()`, asking the model to describe it.

**`inspect_pdf.py`** — The same thing with `mime_type="application/pdf"`. The
model sees layout, tables and diagrams rather than flattened extracted text.

**`extract_from_image.py`** — Combines this project with Project 4: an image
goes in, a validated Pydantic object comes out. Image in, typed data out.

## Notes

These scripts use `Path(__file__).parent` to locate their sample files, so they
work from any directory — unlike Project 4, which has to be run from inside its
own folder.

