from constants import UNDER_20, TENS, ABOVE_100, MAX_SUPPORTED_NUMBER

def num_to_word(num: int) -> str:
    """
    Converts an integer into its English word representation.

    This function supports non-negative integers up to the maximum defined
    in constants.MAX_SUPPORTED_NUMBER.

    Args:
        num (int): The integer to convert.

    Returns:
        str: The English word representation of the number.

    Raises:
        TypeError: If the input 'num' is not an integer.
        ValueError: If the input 'num' is negative or exceeds the maximum
                    supported number.

    """
    if not isinstance(num, int):
        raise TypeError("Input must be an integer.")

    if num < 0:
        raise ValueError("Input must be a non-negative integer.")

    if num > MAX_SUPPORTED_NUMBER:
        raise ValueError(f"Input number {num} exceeds the maximum supported number of {MAX_SUPPORTED_NUMBER}.")

    if num < 20:
        return UNDER_20[num]

    if num < 100:
        if num % 10 == 0:
            return TENS[num // 10]
        return f"{TENS[num // 10]} {num_to_word(num % 10)}"

    pivot_keys = sorted(ABOVE_100.keys(), reverse=True)
    for pivot in pivot_keys:
        if num >= pivot:
            part1 = num // pivot
            remainder = num % pivot

            if remainder == 0:
                return f"{num_to_word(part1)} {ABOVE_100[pivot]}"
            else:
                return f"{num_to_word(part1)} {ABOVE_100[pivot]} {num_to_word(remainder)}"

    return "Error: Could not convert number."


if __name__ == "__main__":
    # Example usage and testing
    test_numbers = [0, 7, 19, 20, 42, 100, 101, 250, 999, 1000, 1001, 1234, 1000000, 1234567, 1000000000, 1234567890]

    print("--- Number to Word Conversion Examples ---")
    for number in test_numbers:
        try:
            print(f"{number:<12}: {num_to_word(number)}")
        except (TypeError, ValueError) as e:
            print(f"{number:<12}: Error - {e}")

    print("\n--- Testing Edge Cases ---")
    try:
        print(f"Negative 5   : {num_to_word(-5)}")
    except (TypeError, ValueError) as e:
        print(f"Negative 5   : Error - {e}")

    try:
        print(f"Float 1.5    : {num_to_word(1.5)}")
    except (TypeError, ValueError) as e:
        print(f"Float 1.5    : Error - {e}")

    # Test beyond MAX_SUPPORTED_NUMBER
    large_num = MAX_SUPPORTED_NUMBER + 100
    try:
        print(f"Large Number : {num_to_word(large_num)}")
    except (TypeError, ValueError) as e:
        print(f"Large Number : Error - {e}")