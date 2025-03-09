import string

def remove_punctuations(input_string):
    return input_string.translate(str.maketrans("", "", string.punctuation))

input_string = "Hello, world! This is a test: with some punctuations."
result = remove_punctuations(input_string)
print(result)