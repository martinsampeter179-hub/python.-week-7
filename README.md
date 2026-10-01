# PLP Python Week 7

- `list_warmup.py` — demonstrates list indexing, append, remove, and len.
- `shopping_list.py` — interactive shopping list manager with add, remove, show, and done options.
- `list_report.py` — prints a numbered list, counts long item names, and finds the longest item.

It is safer to check with `in` before calling `.remove()` because `.remove()` will crash with an error if the item is not in the list. Checking first prevents the program from stopping unexpectedly. It also lets you show a helpful message to the user instead of an error.
