# Module 3: string

## Purpose
The `string` module provides string constants. In the Typing Speed Test project, it supplies punctuation characters used when generating passages and cleaning text before comparing answers.

## Where it appears in the project
- Line 3: `import string`
- Lines 25–27: filters punctuation marks for use in the passage.
- Lines 45–49: removes punctuation and converts text to lowercase.

## Important tools
- `string.punctuation`: a string containing ASCII punctuation characters.
- `str.maketrans()`: creates a translation table.
- `str.translate()`: applies a translation table to a string.
- `.lower()`: converts alphabetic characters to lowercase.
- `.split()`: separates a string into a list of words (used by the project after cleaning).

## Project examples
Filter punctuation:
```python
PUNCTUATION_MARKS = [
    mark for mark in string.punctuation if mark in ".,!?;:"
]
```

Clean text:
```python
text = text.translate(str.maketrans("", "", string.punctuation))
return text.lower()
```
The list comprehension keeps only the selected punctuation characters. The translation table deletes punctuation, and `lower()` makes capitalization consistent.

## Three practical examples
See `string_examples.py`:
1. Filter punctuation marks to match the project.
2. Remove punctuation from a sentence.
3. Normalize capitalization and split text into words for comparison.

## Why clean text?
For example, `Hello, World!` becomes `hello world`. This means punctuation and capitalization differences do not affect the project's word comparison.

## Limitation of the project's comparison
Cleaning text does not correct spelling or ignore word order. The accuracy function still checks whether each word matches the target word at the same position.
