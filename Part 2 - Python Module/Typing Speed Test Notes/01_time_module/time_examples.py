"""Three practical examples for Python's time module."""
import time


def example_1_measure_input():
    """Measure the time a user takes to type a short phrase."""
    print("\nEXAMPLE 1: Measure typing duration")
    input("Press Enter to start...")
    start = time.perf_counter()
    answer = input("Type: Python is fun: ")
    end = time.perf_counter()
    print("You typed:", answer)
    print(f"Elapsed time: {end - start:.2f} seconds")


def example_2_calculate_wpm():
    """Convert seconds to minutes and calculate words per minute."""
    print("\nEXAMPLE 2: Calculate WPM")
    words_typed = 40
    elapsed_seconds = 80
    minutes = elapsed_seconds / 60
    wpm = words_typed / minutes if minutes > 0 else 0
    print(f"Words typed: {words_typed}")
    print(f"Elapsed time: {elapsed_seconds} seconds")
    print(f"Typing speed: {wpm:.2f} WPM")


def example_3_reusable_timer():
    """Use a helper function to measure another short activity."""
    print("\nEXAMPLE 3: Reusable timer")

    def wait_for_user():
        input("Press Enter when you finish the activity...")

    start = time.perf_counter()
    wait_for_user()
    duration = time.perf_counter() - start
    print(f"Activity duration: {duration:.2f} seconds")


if __name__ == "__main__":
    example_1_measure_input()
    example_2_calculate_wpm()
    example_3_reusable_timer()
