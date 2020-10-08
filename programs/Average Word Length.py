word = input("Enter a word: ")
total = 0
num_word = 0
while word != "":
    word = input("Enter another word: ")
    leng_word = len(word)
    total += leng_word
    num_word += 1
average = total / num_word
print("The average of words you entered is: ",format(average, '.2f'))