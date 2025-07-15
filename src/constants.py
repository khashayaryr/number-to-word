# Words for numbers zero to nineteen
UNDER_20 = (
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
)

# Words for multiples of ten
TENS = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")

# Words for powers of a hundred/thousand
ABOVE_100 = {
    100: "hundred",
    1000: "thousand",
    1_000_000: "million",
    1_000_000_000: "billion",
    1_000_000_000_000: "trillion",
}

# The maximum supported number, if applicable
MAX_SUPPORTED_NUMBER = 1_000_000_000_000_000
