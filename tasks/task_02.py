#!/usr/bin/env python3.6
import re


def handle_string(value: str) -> str:
    """
    Counts number of letters and digits in string
    :param value: string for counting digits and letters
    :return: string with detailed data about quantity of digits and letters
    """
    return (
        f'Letters - {len(re.findall(r"[a-zA-Z]", value))}\n'
        f'Digits - {len(re.findall(r"[0-9]", value))}'
    )
