# This is the second project, which is basically a word frequency counter.
# Since, we will be working with strings here quite a lot, it is better to import the string module.
import string

prompt = "The quick brown fox jumps over the lazy dog. The dog barks, but the fox runs away quickly. A quick fox and a lazy dog rarely become friends, yet the dog and the fox somehow learned to share the same yard. The yard was quiet, the fox was clever, and the dog was patient."

# The first step is to convert everything to lowercase.
lower_case_prompt = prompt.lower()

# The second step would be to remove all the punctuations.
tab = str.maketrans("", "", string.punctuation)
prompt_without_punctuation = lower_case_prompt.translate(tab)
print(prompt_without_punctuation)

# Manual method of removing the punctuations.
# unpunctuated_prompt = ""
# for char in lower_case_prompt:
#     if char not in string.punctuation:
#         unpunctuated_prompt += char

# print(unpunctuated_prompt)
# print(prompt_without_punctuation == unpunctuated_prompt)

list_of_words = prompt_without_punctuation.split()
print('Your list of words are :', list_of_words)
print('The total wordcount of your list is :',len(list_of_words))

# The next step would be to initialize an empty dictionary.
frequency_counter = {}
# for word in list_of_words:
#     if word in frequency_counter:
#         frequency_counter[word] += 1
#     else:
#         frequency_counter[word] = 1

# print(frequency_counter['the'])

# This can be done using the get method as well.
for word in list_of_words:
    frequency_counter[word] = frequency_counter.get(word, 0) + 1

# The number of unique words can be found out using the number of unique keys.
# And, the number of unique keys can simply be found out using the 'len' function.
print(f'The number of unique words in the prompt are {len(frequency_counter)}')

# Next, we need to sort the dictionary in descending order of word frequency.
sorted_word_list = sorted(frequency_counter.items(), key=lambda pair: pair[1], reverse=True)
print(sorted_word_list)

# Next, we need to find the most frequent word from that sorted list.
# Ideally, since the list is already sorted, it is going to be the first word (having the highest frequency).
most_frequent_word = sorted_word_list[0]
print(f'The most frequent word is "{most_frequent_word[0]}" with a count of {most_frequent_word[1]}.')

# Next, we need all the words with a count of more than 1 and equal to 1.
# This can be done using a simple iteration in which we check the value against each key and update the corresponding variable accordingly.
words_with_count_exactly_one = 0
words_with_count_more_than_one = 0

for word in frequency_counter:
    if frequency_counter[word] > 1:
        words_with_count_more_than_one += 1
    
    elif frequency_counter[word] == 1:
        words_with_count_exactly_one += 1

print(f'There are {words_with_count_more_than_one} words which have a frequency of more than 1 and {words_with_count_exactly_one} words which have a frequency of exactly 1.')