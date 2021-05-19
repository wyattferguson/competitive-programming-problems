def convert(number=0):
    msg = "Pling" if number % 3 == 0 else ""
    msg += "Plang" if number % 5 == 0 else ""
    msg += "Plong" if number % 7 == 0 else ""

    return msg if msg else str(number)
