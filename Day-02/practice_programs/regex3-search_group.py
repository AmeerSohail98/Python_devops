import re 

text = "The quick (brown) fox and (red) bird"
pattern = r"\((.*?)\)"
start = 0

while True:
    search = re.search(pattern, text[start:])
    if not search:
        break
    print("Found:", search.group(1))
    start += search.end()  # Move forward in the string