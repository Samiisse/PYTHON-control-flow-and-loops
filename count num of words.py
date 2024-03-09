#Given a list of words, count the number of words with more than five characters

def count_words_more_than_five_chars(word_list):
    count = 0
    for word in word_list:
        if len(word) > 5:
            count += 1
    return count

word_list = ["apple", "banana", "orange", "grape", "pineapple", "kiwi", "watermelon"]
result = count_words_more_than_five_chars(word_list)
print(f"Number of words with more than 5 characters is {result}: ")