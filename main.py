import os

TEXT = "You have read a hundred voices today, each one asking to be chosen. The light is thinning over the rooftops now, and somewhere a kettle is just beginning to sing. The next page will wait. When you come back to it, you will know which one is yours."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
