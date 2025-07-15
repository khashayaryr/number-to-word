from constants import *

def num_to_word(num):
    if num < 20:
        return under_20[num]

    if num < 100:
        if num % 10 == 0:
            return tens[num // 10]

        return f"{tens[num // 10]} {num_to_word(num % 10)}"

    pivot = max([key for key in above_100 if num >= key])
    p1 = num // pivot

    if num % pivot == 0:
        return f"{num_to_word(p1)} {above_100[pivot]}"

    return f"{num_to_word(p1)} {above_100[pivot]} {num_to_word(num % pivot)}"
