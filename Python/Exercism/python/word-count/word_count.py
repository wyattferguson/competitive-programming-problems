import re


def count_words(sentence):
    cleaned = sentence.lower()
    # remove everything but alphanumerics and apostrophes
    cleaned = re.sub(r"[^a-zA-Z0-9=']", ' ', cleaned)

    # remove apostrophe special cases
    for t in [" '", "' ", "''"]:
        cleaned = cleaned.replace(t, " ")
    if cleaned[-1] == "'":
        cleaned = cleaned[:-1]

    words = cleaned.split()
    word_cnt = {}
    for w in words:
        word_cnt[w] = words.count(w)
    return word_cnt


if __name__ == "__main__":
    sentence = "That's the password: 'PASSWORD 123'!, cried the Special Agent.\nSo I fled."
    cnt = count_words(sentence)
    for a, b in cnt.items():
        print(a, b)
