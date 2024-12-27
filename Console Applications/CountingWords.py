words_list = []
counts = [0,0,0]
for i in range(3):
    print('Write  ',i+1,' word: ',end=" ")
    word = input()
    words_list.append(word)

text = input('word from text ')
while text!= 'end':
    for index in range(3):
        if words_list[index]== text:
            counts[index] +=1
    text = input('word from text ')

print('\nCounting words in text ')
for i in range(3):
    print(words_list[i],':',counts[i])