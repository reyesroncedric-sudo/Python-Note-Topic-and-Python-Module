# Module 1: time

## Purpose
The `time` module provides time-related functions. In the Typing Speed Test project, it measures how long the user takes to type the displayed passage.

## Where it appears in the project
- Line 1: `import time`
- Lines 83–90: records the start time, accepts the typed passage, records the end time, and calculates elapsed seconds.
- Lines 97–103: converts elapsed seconds to minutes before calculating WPM.

## Main function: `time.perf_counter()`
`time.perf_counter()` returns a high-resolution counter suitable for measuring elapsed duration. It is not a clock time such as 10:30 AM; subtract two readings to get the duration.

## Project example
```python
start_time = time.perf_counter()
typed_text = input("> ")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
```
The first call records the start, the second call happens after the user presses Enter, and subtracting the values gives the time spent typing.

## Three practical examples
See `time_examples.py`:
1. Measure how long a user takes to enter a phrase.
2. Convert elapsed seconds into minutes and calculate WPM.
3. Reuse a timer helper function to measure another activity.

## WPM formula
`WPM = number_of_words_typed / elapsed_time_in_minutes`

Example: 40 words typed in 80 seconds means 80 / 60 = 1.333 minutes, so WPM is approximately 30.

## Key points
- Use `perf_counter()` for elapsed-time measurement.
- Convert seconds to minutes before calculating WPM.
- Check that elapsed minutes are greater than zero before dividing.
