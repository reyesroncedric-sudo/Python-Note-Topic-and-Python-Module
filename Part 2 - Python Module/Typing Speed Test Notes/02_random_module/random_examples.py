"""Three practical examples for Python's random module."""
import random

WORD_BANK = [
    "python", "computer", "keyboard", "practice", "learning",
    "program", "student", "challenge", "typing", "speed",
    "accuracy", "screen", "function", "variable", "project",
]
PUNCTUATION_MARKS = ".,!?;:"


def example_1_select_words():
    """Select eight unique words to make a practice passage."""
    print("\nEXAMPLE 1: Select unique words")
    words = random.sample(WORD_BANK, 8)
    print("Selected words:", words)
    print("Passage:", " ".join(words))


def example_2_choose_punctuation():
    """Choose one punctuation mark at random."""
    print("\nEXAMPLE 2: Choose punctuation")
    word = "practice"
    mark = random.choice(PUNCTUATION_MARKS)
    print("Before:", word)
    print("After:", word + mark)


def example_3_shuffle_words():
    """Shuffle a list to create a different practice order."""
    print("\nEXAMPLE 3: Shuffle practice words")
    words = ["type", "carefully", "check", "your", "accuracy"]
    print("Original:", words)
    random.shuffle(words)
    print("Shuffled:", words)


if __name__ == "__main__":
    example_1_select_words()
    example_2_choose_punctuation()
    example_3_shuffle_words()
