# Project 2: Study Coach

Multi-turn conversations and chat history.

## Files

**`chat_basics.py`** — Creates a chat with `client.chats.create()` and sends two messages, where the second one relies on information from the first to prove the history is being carried.

**`chat_history.py`** — Prints the accumulated history so you can see the alternating `user` / `model` turns that get resent on every request.

**`chat_resume.py`** — Seeds a chat with a history I wrote by hand, showing that a conversation can be rebuilt from stored turns rather than be held in memory.

**`coach.py`** — An interactive `while True` loop with a `system_instruction` set once at chat creation, so the coaching behaviour applies to the whole conversation.

## Notes

- Roles must be `user` or `model`.
- `print(response.usage_metadata)` after a call to see how many tokens are being used each call, thought-tokens used, etc.
