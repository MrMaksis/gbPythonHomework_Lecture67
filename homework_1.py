def count_vowels(word):
    vowels = "аоуэыиеёяю"
    return sum([1 for letter in word.lower() if letter in vowels])

poem = input("Введите стихотворение: ")
phrases = poem.split()

vowel_counts = [count_vowels(phrase.replace('-', '')) for phrase in phrases]

if len(set(vowel_counts)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")