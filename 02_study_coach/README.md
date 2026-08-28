# Project 2

Project 2 covers **multi-turn** conversations and **chat history**.

`chat_basics.py` - creates a chat with `client.chats.create()` and sends two messages, where the second one relies on information from the first to prove the history is being carried 

`chat_history.py` - prints the accumalated history so you can see the alternating `user` / `model` turns that get resent on every request 

`chat_resume.py` - seeds a chat with a history I wrote by hand, showing that a conversation can be rebuilt from stored turns rather than be held in memory

`coach.py` - an interactive `while True` loop with a `system_insturction` set at once at chat creation, so the coaching behaviour applies to the whole conversation

---

> Roles must be `user` or `model`

- `print(response.usage_metadata)` - after a call to see how many tokens are being used each call,  thought-tokens used, etc.
