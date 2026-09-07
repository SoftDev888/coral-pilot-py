def running(values: list[int]) -> list[int]:
    """Each total up to and including that point."""
    found: list[int] = []
    total = 0
    for one in values:
        total += one
        found.append(total)
    return found


if __name__ == "__main__":
    print(running([3, 1, 4, 1, 5]))
