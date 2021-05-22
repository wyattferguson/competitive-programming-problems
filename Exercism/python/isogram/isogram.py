def is_isogram(string=None):
    string = string.replace(" ", "")
    string = string.replace("-", "")
    string = string.lower()

    for i in range(len(string)):
        if string[i] in string[i+1:]:
            return False
    return True
