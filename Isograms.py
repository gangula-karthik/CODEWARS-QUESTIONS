def is_isogram(string):
    return sorted(list(set(string.lower()))) == sorted(list(string.lower()))
