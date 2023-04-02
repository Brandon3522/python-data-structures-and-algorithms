# Dict testing
my_dict = {
    'US': 'Dollar',
    'Europe': 'Euro',
    'Great Britain': 'Pound',
    'China': 'Yuan',
    'India': 'Rupee'
}

for value, key in my_dict.items():
    print(f'Value: {value}, Key: {key}')

print()

country_us = my_dict.get('US', None)
print(f'{country_us}')

print(my_dict.items())
print('###########################################')

# Counting word frequencies
# freq = {}
# for piece in open('word_counting.txt').read().lower().split():
#     # print(f'{piece}')
#     word = ''.join(c for c in piece if c.isalpha()) # find alphabetic words
#     # print(f'{word}')
#     if word: # At least one alphabetic character
#         freq[word] = freq.get(word, 0) + 1
# max_word = ''
# max_count = 0
# for word, count in freq.items():
#     if count > max_count:
#         max_word = word
#         max_count = count
# print(f'The most frequent word is: {max_word}')
# print(f'The max word count is: {max_count}')
# print()

freq1 = {}
for word in open('word_counting.txt').read().lower().split():
    alphabetic_word = ''.join(char for char in word if char.isalpha())
    # print(f'Words: {alphabetic_word}')
    if alphabetic_word:
        freq1[alphabetic_word] = freq1.get(alphabetic_word, 0) + 1
# print(f'{freq.items()}')

# Find the word with highest count
max_word = ''
max_count = 0
for word, count in freq1.items():
    if count > max_count:
        max_word = word
        max_count = count
print(f'Max word: {max_word}')
print(f'Max count: {max_count}')

























freq2 = {}
for word in open('word_counting.txt').read().lower().split():
    alphabetic_word = ''.join(char for char in word if char.isalpha())
    if alphabetic_word:
        freq2[alphabetic_word] = freq2.get(alphabetic_word, 0) + 1

# Get max
max_word1 = ''
max_count1 = 0

for word, count in freq2.items():
    if count > max_count1:
        max_count1 = count
        max_word1 = word
print(f'Max word: {max_word1}, Max count: {max_count1}')






























