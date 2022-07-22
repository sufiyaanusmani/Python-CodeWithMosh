from operator import imod
from pprint import pprint

sentence = "This is a common interview question"

frequency = {}

for ch in sentence:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print(sorted(frequency.items(), key=lambda kv:kv[1], reverse=True))
