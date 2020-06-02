sentence = 'fnweiofnwenwef'#input('Enter your sentence: ')
#sorted_sentence = sorted(sentence)  #sorted de sap xep lai bang chu cai
count_dictionary = {}
for char in sentence:
    if char in count_dictionary:
        count_dictionary[char] = count_dictionary[char] + 1
    else:
        count_dictionary[char] = 1
key_values_list = sorted(count_dictionary.items())

for key_values in key_values_list:
    print(key_values[0], key_values[1])

