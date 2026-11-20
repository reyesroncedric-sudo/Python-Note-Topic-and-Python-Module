# Typing Speed Test Project

## Purpose
The program generates a random passage, asks the user to type it, measures elapsed time, and displays typing speed and accuracy.

## Modules
- `time`: measures the duration of the typing attempt using `time.perf_counter()`.
- `random`: selects words and punctuation for a generated passage.
- `string`: provides punctuation constants and helps clean text before comparison.

## Main functions
- `generate_text()`: selects random words and adds punctuation.
- `clean_text(text)`: removes punctuation and converts text to lowercase.
- `calculate_accuracy(target_text, typed_text)`: counts words matching at the same position and calculates a percentage.
- `run_test()`: displays the passage and measures the user's typing duration.
- `show_results(...)`: calculates WPM and prints the results and feedback.
- `main()`: repeats the test until the user chooses to stop.

## Main formulas
- Elapsed seconds = end counter - start counter
- Minutes = elapsed seconds / 60
- WPM = number of typed words / minutes
- Accuracy = correct words / total target words * 100

## Original source
`Typing_Speed_Test.py` is the supplied project file, copied into this folder for convenient reference.
