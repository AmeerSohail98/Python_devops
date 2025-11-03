Regex
1. Regular Expressions for Text Processing:

Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
The re module in Python is used for working with regular expressions.
Common metacharacters: . (any character), * (zero or more), + (one or more), ? (zero or one), [] (character class), | (OR), ^ (start of a line), $ (end of a line), etc.

    These examples keep things basic—regex can get more complex when combined!
    1. . (any character)
    Description: Matches any single character except a newline (\n). It's like a wildcard for one position.
    Example:

    Text: "Hello\nWorld\nPython\nRegex"
    Pattern: r'.' (just a dot)
    Code:
    pythonimport re
    text = "Hello\nWorld\nPython\nRegex"
    matches = re.findall(r'.', text)
    print(matches[:5], "...")  # First 5 matches for brevity

    Output: ['H', 'e', 'l', 'l', 'o'] ...
    (It matches every character, one by one, skipping newlines.)

    2. * (zero or more)
    Description: Matches zero or more repetitions of the preceding element (e.g., character or group). It's greedy by default, matching as much as possible.
    Example:

    Text: "aaabbbccc" (three 'a's followed by 'b's and 'c's)
    Pattern: r'a*' (zero or more 'a's)
    Code:
    pythonimport re
    text = "aaabbbccc"
    matches = re.findall(r'a*', text)
    print(matches)

    Output: ['aaa', '', '', '', '', '', '', '']
    (It matches the three 'a's at the start, then empty strings where no 'a's follow. The empties show zero matches are allowed.)

    3. + (one or more)
    Description: Matches one or more repetitions of the preceding element. Similar to *, but requires at least one.
    Example:

    Text: "aaabbbccc" (same as above)
    Pattern: r'a+' (one or more 'a's)
    Code:
    pythonimport re
    text = "aaabbbccc"
    matches = re.findall(r'a+', text)
    print(matches)

    Output: ['aaa']
    (It matches the three 'a's, but skips empties since at least one 'a' is required—no match elsewhere.)

    4. ? (zero or one)
    Description: Matches zero or one (optional) occurrence of the preceding element. Useful for handling variations like spelling.
    Example:

    Text: "color colour" (American vs. British English)
    Pattern: r'colou?r' ( 'u' is optional in "colour")
    Code:
    pythonimport re
    text = "color colour"
    matches = re.findall(r'colou?r', text)
    print(matches)

    Output: ['color', 'colour']
    (It matches both, treating the 'u' as optional.)

    5. [] (character class)
    Description: Matches any single character from a set inside the brackets. You can list chars (e.g., [abc] for a/b/c) or ranges (e.g., [a-z] for lowercase letters). Negate with ^ inside (e.g., [^0-9] for non-digits).
    Example:

    Text: "Hello123World456"
    Pattern: r'[a-zA-Z]' (any letter, uppercase or lowercase)
    Code:
    pythonimport re
    text = "Hello123World456"
    matches = re.findall(r'[a-zA-Z]', text)
    print(''.join(matches))  # Joined for readability

    Output: HelloWorld
    (It extracts all letters, ignoring numbers.)

    6.  (OR)
    Description: Acts as a logical OR between alternatives. Matches one of the patterns separated by .
    Example:

    Text: "cat dog bird"
    Pattern: r'cat|dog' (match "cat" OR "dog")
    Code:
    pythonimport re
    text = "cat dog bird"
    matches = re.findall(r'cat|dog', text)
    print(matches)

    Output: ['cat', 'dog']
    (It matches the first two words but skips "bird" since it's not listed.)

    7. ^ (start of a line)
    Description: Anchors the match to the start of a line (or the whole string if not multiline). Use with re.MULTILINE flag for multiple lines.
    Example:

    Text: "Hello\nWorld\nPython\nRegex" (multiline string)
    Pattern: r'^Hello' (must start a line with "Hello")
    Code:
    pythonimport re
    text = "Hello\nWorld\nPython\nRegex"
    matches = re.findall(r'^Hello', text, re.MULTILINE)
    print(matches)

    Output: ['Hello']
    (It only matches the first line starting with "Hello"; others don't.)

    8. $ (end of a line)
    Description: Anchors the match to the end of a line (or the whole string if not multiline). Pairs well with ^ for exact line matches.
    Example:

    Text: "Hello\nWorld\nPython\nRegex" (same multiline)
    Pattern: r'Python$' (must end a line with "Python")
    Code:
    pythonimport re
    text = "Hello\nWorld\nPython\nRegex"
    matches = re.findall(r'Python$', text, re.MULTILINE)
    print(matches)

    Output: ['Python']
    (It matches only the third line ending with "Python.")

    These are foundational building blocks—combine them for powerful searches (e.g., r'^[a-zA-Z]+$' for a whole line of letters only). Test in Python's REPL or tools like regex101.com for practice! If you have a specific string to match, share it for a custom example.

Examples of regex usage: matching emails, phone numbers, or extracting data from text.
re module functions include re.match(), re.search(), re.findall(), and re.sub() for pattern matching and replacement.