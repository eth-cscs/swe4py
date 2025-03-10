def even_if_possitive(n: int) -> int:
    """
    """
    if n > 0:
        return 2

    if n < 0:
        return 1

    return 0


if __name__ == "__main__":
    # Needed if running without -m doctest
    import doctest
    doctest.testmod()
