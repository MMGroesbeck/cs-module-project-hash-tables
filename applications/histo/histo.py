# Your code here
def histo(filename):
    with open(filename) as txt:
        text = txt.read()

    words_chart = {}

    ignore = list('":;,.-+=/\|[]}{()*^&')

    no_ignored = True
    max_len = 0
    mark = "#"

    for word in text.split():
        wrd = ""
        for char in word:
            if char not in ignore:
                wrd = wrd + char.casefold()
            else:
                no_ignored = False
        if wrd in words_chart:
            words_chart[wrd] += 1
        else:
            words_chart[wrd] = 1
        if len(wrd) > max_len:
            max_len = len(wrd)
    
    if no_ignored:
        return
    
    # Build list of (word, count) tuples
    word_tups = [(word[0], word[1]) for word in words_chart.items()]
    # Sort by alpha (secondary), then count (primary)
    for i in [(0, False), (1, True)]:
        word_tups = sorted(word_tups, key=lambda item: item[i[0]], reverse=i[1])

    for word_tup in word_tups:
        # print(word_tup[0], "#"*word_tup[1])
        print(f"{word_tup[0]:{max_len+2}}{mark*word_tup[1]}")

histo("robin.txt")