import time
import random
import string


# ============================================================
# TYPING SPEED TEST
# Modules used: time, random, string
# ============================================================

# ---------- SETTINGS ----------
WORD_BANK = [
    "python", "computer", "keyboard", "practice", "learning",
    "program", "student", "challenge", "typing", "speed",
    "accuracy", "screen", "function", "variable", "project",
    "school", "success", "creative", "internet", "developer",
    "simple", "quick", "answer", "write", "improve",
    "future", "technology", "skill", "excellent", "sentence",
    "careful", "correct", "focus", "knowledge", "information",
    "development", "exercise", "performance", "achievement"
]

NUMBER_OF_WORDS = 20

# Select familiar punctuation marks from string.punctuation.
PUNCTUATION_MARKS = [
    mark for mark in string.punctuation if mark in ".,!?;:"
]


# ---------- TEXT GENERATOR ----------
def generate_text():
    """Generate a new typing passage using random words and punctuation."""
    words = random.sample(WORD_BANK, NUMBER_OF_WORDS)

    # Add punctuation to some words to make the typing passage realistic.
    for index in range(3, len(words), 5):
        punctuation = random.choice(PUNCTUATION_MARKS)
        words[index] += punctuation

    passage = " ".join(words)
    return passage[0].upper() + passage[1:] + "."


# ---------- TEXT CHECKER ----------
def clean_text(text):
    """Remove punctuation and make text lowercase for fair comparison."""
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.lower()


def calculate_accuracy(target_text, typed_text):
    """Calculate the percentage of words typed correctly in the right order."""
    target_words = clean_text(target_text).split()
    typed_words = clean_text(typed_text).split()

    correct_words = 0

    for index in range(len(target_words)):
        if index < len(typed_words) and target_words[index] == typed_words[index]:
            correct_words += 1

    if len(target_words) == 0:
        return 0, 0

    accuracy = (correct_words / len(target_words)) * 100
    return accuracy, correct_words


# ---------- TYPING TEST ----------
def run_test():
    """Display a random passage and measure the user's typing time."""
    target_text = generate_text()

    print("\n" + "=" * 55)
    print("                 TYPING SPEED TEST")
    print("=" * 55)
    print("\nType the following passage as quickly and accurately as possible:\n")
    print(target_text)

    input("\nPress Enter when you are ready to begin...")

    print("\nStart typing below:")
    start_time = time.perf_counter()

    typed_text = input("> ")

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return target_text, typed_text, elapsed_time


# ---------- RESULTS ----------
def show_results(target_text, typed_text, elapsed_time):
    """Calculate and display the user's typing speed and accuracy."""
    typed_words = typed_text.split()
    minutes = elapsed_time / 60

    if minutes > 0:
        words_per_minute = len(typed_words) / minutes
    else:
        words_per_minute = 0

    accuracy, correct_words = calculate_accuracy(target_text, typed_text)

    print("\n" + "-" * 55)
    print("                    TEST RESULTS")
    print("-" * 55)
    print(f"Time taken:       {elapsed_time:.2f} seconds")
    print(f"Words typed:      {len(typed_words)}")
    print(f"Typing speed:     {words_per_minute:.2f} WPM")
    print(f"Correct words:    {correct_words}/{NUMBER_OF_WORDS}")
    print(f"Accuracy:         {accuracy:.2f}%")

    if accuracy >= 90:
        print("\nExcellent! You typed with great accuracy.")
    elif accuracy >= 70:
        print("\nGood job! Keep practicing to improve your accuracy.")
    else:
        print("\nKeep practicing. Accuracy improves with practice.")

    print("-" * 55)


# ---------- MAIN PROGRAM ----------
def main():
    """Run the typing test and allow the user to play again."""
    print("=" * 55)
    print("             WELCOME TO TYPING SPEED TEST")
    print("=" * 55)
    print("Measure your typing speed and see how accurate you are!")

    while True:
        target_text, typed_text, elapsed_time = run_test()
        show_results(target_text, typed_text, elapsed_time)

        play_again = input("\nWould you like to try again? (yes/no): ")
        if play_again.strip().lower() not in ("yes", "y"):
            print("\nThank you for using the Typing Speed Test!")
            print("Keep practicing and have a great day!")
            break


if __name__ == "__main__":
    main()
