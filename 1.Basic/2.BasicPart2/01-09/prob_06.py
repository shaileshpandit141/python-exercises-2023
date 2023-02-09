"""Q6. Write a Python program that prints long text, converts it to a list, and prints all the words and the
frequency of each word."""

string_words = """Write a Python program that prints long text, converts it to a list, and prints all the words and the
frequency of each word."""

word_list = string_words.split()
word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))