def sort_sentence(sentence):
    words = sentence.split()
    words.sort()
    return " ".join(words)

sentence = "python is fun and easy to learn"
sorted_sentence = sort_sentence(sentence)
print(sorted_sentence)