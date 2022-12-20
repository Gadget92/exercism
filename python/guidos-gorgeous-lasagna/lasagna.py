"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate preparation time in minutes.

    :param number_of_layers: int - number of lagna layers.
    :return: int - preparation time in minutes.

    Function that takes the number of layers you want to add to the lasagna as an
    argument and returns how many minutes you would spend making them
    """

    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int)-> int:
    """Return elapsed cooking time.

    This function takes two numbers representing the number of layers and
    the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
