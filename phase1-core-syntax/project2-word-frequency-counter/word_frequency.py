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
for word in list_of_words:
    if word in frequency_counter:
        frequency_counter[word] += 1
    else:
        frequency_counter[word] = 1

print(frequency_counter['the'])


