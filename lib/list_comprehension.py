def return_evens(sequence):
    """
    Returns a list of even numbers from the given sequence of integers.
    """
    return [n for n in sequence if n % 2 == 0]

def make_exclamation(sentences):
    """
    Returns a list of sentences with an exclamation mark appended to each.
    """
    return [sentence + "!" for sentence in sentences]
