
def canFormArray(arr, pieces):
    hld = []
    i = 0
    while i < len(arr):
        if pieces:
            for p in pieces[:]:
                if arr[i] in p:
                    hld.extend(p)
                    i += len(p)
                    pieces.remove(p)
                    break
            else:
                return False

    return True if hld == arr else False


if __name__ == "__main__":
    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]

    result = canFormArray(arr, pieces)
    if result:
        print("Good Match!")
    else:
        print("Bad Match :(")
