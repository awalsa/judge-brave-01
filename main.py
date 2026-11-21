"""Write one short text for the AI judge: 1-280 characters, UTF-8.

The text itself is the entry. It is kept short and plain on purpose:
the judge weighs a slow, concrete image over length, so the program
refuses to write anything outside the gate instead of submitting it.
"""

import os

TEXT = "You have read a hundred voices today, each one asking to be chosen. The light is thinning over the rooftops now, and somewhere a kettle is just beginning to sing. The next page will wait. When you come back to it, you will know which one is yours."

# The gate counts Unicode code points, not bytes; the text is ASCII,
# so len() is the gate's own count. Fail loudly rather than ever
# writing a file the gate would refuse.
assert 1 <= len(TEXT) <= 280, f"entry text is {len(TEXT)} characters"
assert TEXT.strip(), "entry text must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
