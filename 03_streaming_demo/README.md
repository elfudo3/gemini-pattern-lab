# Project 3: Streaming Demo

Streaming responses — printing the reply token by token as it arrives instead of waiting for the whole thing.

## Files

**`stream_basics.py`** — Calls `client.models.generate_content_stream()` and iterates over the chunks, printing each `chunk.text` as it comes in so the output appears progressively rather than all at once.

## Notes

- Each chunk can be empty, so guard with `if chunk.text:` before printing.
- Use `print(..., end="", flush=True)` to append chunks on one line and flush immediately, otherwise the terminal buffers the output and the streaming effect is lost.
