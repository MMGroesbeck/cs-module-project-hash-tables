import random

class WordStats:
    def __init__(self):
        self.start = False
        self.stop = False
        self.followers = []
    
    def add_follow(self, foll):
        self.followers.append(foll)

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()

# TODO: analyze which words can follow other words
# Your code here
word_chart = {}
starts = []
ends = []
for i in range(len(words)):
    word = words[i]
    enders = list('.?!')
    if word not in word_chart:
        word_chart[word] = WordStats()
        if (word[0].isupper()) or (word[0] == '"' and word[1].isupper()):
            word_chart[word].start = True
            starts.append(word)
        if (word[-1] in enders) or (word[-1] == '"' and word[-2] in enders) or (i == len(words) - 1):
            word_chart[word].stop = True
            ends.append(word)
    if i+1 < len(words):
        word_chart[word].add_follow(words[i+1])

# TODO: construct 5 random sentences
# Your code here
def nonsense():
    this_word = random.choice(starts)
    chain = [this_word]
    while not word_chart[this_word].stop:
        this_word = random.choice(word_chart[this_word].followers)
        chain.append(this_word)
    return " ".join(chain)

for i in range(5):
    print(nonsense())