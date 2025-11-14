
word = input("Введите слово: ")
def count_vowels(word):
    vowels = "aeiouyAEIOUY"
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count
count_consonants = len(word) - count_vowels(word)
print("Согласных:", count_consonants, "  Гласных:", count_vowels(word))

def count_vow(word):
    vowels = "aeiouyAEIOUY"
    for i in word:
        if i in vowels:
            print(i, "=", word.count(i))
        else:
            print("False")
print(count_vow(word))                




