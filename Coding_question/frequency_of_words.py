sentence = "python is easy and python is powerful"

words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
