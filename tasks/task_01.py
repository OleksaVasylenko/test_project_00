#!/usr/bin/env python3.6


def handle_numbers(start: int, end: int, div: int) -> str:
    """
    Counts integers in range from start to end if they are divisible by div
    :param start: starting integer of range
    :param end: ending integer of range
    :param div: number for dividing the items of range
    :return: string with detailed data about occurrences
    """
    if div == 0:
        return '0, because no numbers are divisible by 0'
    if start > end:
        start, end = end, start

    quotients = [str(n) for n in range(start, end+1) if (n / div).is_integer()]

    length = len(quotients)
    str_quotients = ", ".join(quotients) if length else 'none in given range'
    word = "are" if length > 1 else "is"

    return f'{length}, because {str_quotients} {word} divisible by {div}'
