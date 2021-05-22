def get_verse(verse):
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
            'eleventh', 'twelfth']

    lyrics = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "and a Partridge in a Pear Tree."
    ]

    song = [
        f"On the {days[verse - 1]} day of Christmas my true love gave to me: "]

    if verse == 1:
        song.append("a Partridge in a Pear Tree.")
    else:
        n = len(lyrics)
        song += [lyrics[index]
                 for index in range(n - verse, n)]

    return ''.join(song)


def recite(start_verse, end_verse):
    return [get_verse(i) for i in range(start_verse, end_verse + 1)]
