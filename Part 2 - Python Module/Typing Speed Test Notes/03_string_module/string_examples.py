"""Three practical examples for Python's string module."""
import string

ALLOWED_MARKS = ".,!?;:"


def example_1_filter_punctuation():
    """Keep only the punctuation marks selected by the project."""
    print("\nEXAMPLE 1: Filter punctuation")
    selected = [
        mark for mark in string.punctuation
        if mark in ALLOWED_MARKS
    ]
    print("All ASCII punctuation:", string.punctuation)
    print("Project punctuation:", "".join(selected))


def example_2_remove_punctuation():
    """Remove punctuation from a sentence."""
    print("\nEXAMPLE 2: Remove punctuation")
    sentence = "Hello, Python! Are you ready?"
    table = str.maketrans("", "", string.punctuation)
    cleaned = sentence.translate(table)
    print("Original:", sentence)
    print("Cleaned:", cleaned)


def example_3_normalize_and_split():
    """Normalize capitalization and split text into individual words."""
    print("\nEXAMPLE 3: Normalize and split")
    target = "Python Makes Typing Fun!"
    typed = "python makes typing fun"

    table = str.maketrans("", "", string.punctuation)
    target_words = target.translate(table).lower().split()
    typed_words = typed.translate(table).lower().split()

    print("Target words:", target_words)
    print("Typed words:", typed_words)
    print("Same words in the same order:", target_words == typed_words)


if __name__ == "__main__":
    example_1_filter_punctuation()
    example_2_remove_punctuation()
    example_3_normalize_and_split()
