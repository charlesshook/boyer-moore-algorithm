def preprocess_strong_suffix(shift, border_position, pattern):
    m = len(pattern)
    i = m
    j = m + 1
    border_position[i] = j

    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i

            j = border_position[j]

        i -= 1
        j -= 1
        border_position[i] = j

    return


def preprocess_partial_suffix(shift, border_position, pattern_length):
    j = border_position[0]

    for i in range(pattern_length + 1):
        if shift[i] == 0:
            shift[i] = j

        if i == j:
            j = border_position[j]

    return


def search(text, pattern):
    s = 0
    m = len(pattern)
    n = len(text)
    count = 0
    border_position = [0] * (m + 1)
    shift = [0] * (m + 1)

    preprocess_strong_suffix(shift, border_position, pattern)
    preprocess_partial_suffix(shift, border_position, m)

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            count += 1
            s += shift[0]
        else:
            s += shift[j + 1]

    return count
