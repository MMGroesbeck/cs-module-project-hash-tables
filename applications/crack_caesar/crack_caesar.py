# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
char_chart = {}
letters = "ETAOHNRISDLWUGFBMYCPKVQJXZ"
with open("ciphertext.txt") as txt:
    ciphered = txt.read()

# Count frequency of each letter in ciphertext:
for char in ciphered:
    if char in char_chart:
        char_chart[char] += 1
    elif char in letters:
        char_chart[char] = 1

# Sort characters in ciphertext by frequency descending:
chars_found = char_chart.keys()
freq_tuples = []
for char in chars_found:
    freq_tuples.append((char, char_chart[char]))
freq_tuples = sorted(freq_tuples, key=lambda char: char[1], reverse=True)

# Combine sorted list with letter frequency order into decoding dictionary:
decoder = {}
for i in range(26):
    decoder[freq_tuples[i][0]] = letters[i]

# Decode ciphertext:
decoded = ""
for char in ciphered:
    if char in decoder:
        decoded = decoded + decoder[char]
    else:
        decoded = decoded + char

print(decoded)