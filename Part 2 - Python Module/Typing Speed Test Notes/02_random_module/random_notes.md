# Module 2: random

## Purpose
The `random` module provides functions for pseudo-random selections. In the Typing Speed Test project, it selects words for a new passage and chooses punctuation marks.

## Where it appears in the project
- Line 2: `import random`
- Lines 31–42: `generate_text()` selects words and adds punctuation.
- Line 34: `random.sample()` selects the words.
- Line 38: `random.choice()` chooses a punctuation mark.

## Main functions
- `random.sample(sequence, k)`: returns `k` unique selected items from a population.
- `random.choice(sequence)`: returns one randomly selected item from a non-empty sequence.
- `random.shuffle(list)`: shuffles a list in place.

## Project example
```python
words = random.sample(WORD_BANK, NUMBER_OF_WORDS)

for index in range(3, len(words), 5):
    punctuation = random.choice(PUNCTUATION_MARKS)
    words[index] += punctuation
```
The project selects 20 unique words from `WORD_BANK`, then adds a randomly selected punctuation mark to some words.

## Three practical examples
See `random_examples.py`:
1. Select a unique group of words for a passage.
2. Choose a punctuation mark and attach it to a word.
3. Shuffle a practice-word list to change its order.

## Key distinction
`random.sample()` does not repeat the same selected list position in one draw. `random.choices()` allows repeated selections. The project uses `sample()` so a passage contains distinct selections.
