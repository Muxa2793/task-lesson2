
# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква {word[-1]}')

# Вывести количество букв "а" в слове
word = 'Архангельск'
count = 0
for a in word.lower():
    if a == 'а':
        count += 1
print(f'а: {count}')

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аееиоуыэюя'
count = 0
for letter in word:
    if letter.lower() in vowels:
        count += 1
print(f'Гласных: {count}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split(' ')
print(len(sentence))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split(' ')
for word in sentence:
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sentence_merge = sentence.replace(' ', '')
print(sentence_merge)
sentence_list = sentence.split()
print(sentence_list)
avg_lengths_word = len(sentence_merge)/len(sentence_list)
print(avg_lengths_word)
