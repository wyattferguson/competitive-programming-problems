def distance(strand_a="", strand_b=""):
    if not strand_a and not strand_b:
        return 0

    if not strand_a or not strand_b:
        raise ValueError(
            "Empty strand provided")

    if len(strand_a) != len(strand_b):
        raise ValueError(
            "Strands are not equal lengths")

    n = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            n += 1

    return n
