#!/usr/bin/env python3.6
from operator import itemgetter


def handle_list_of_tuples(tuples: list) -> list:
    """
    Sorts list of tuples by name / age / height / weight
    :param tuples: list of tuples
    :return: sorted list of tuples
    """
    sorted_list = sorted(tuples, key=itemgetter(1, 2, 3), reverse=True)
    return sorted(sorted_list, key=itemgetter(0))
