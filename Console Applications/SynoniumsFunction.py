def getSynonym(count):
    word_pair = ""
    if isinstance(count,int):
        synonyms = dict()
        for word in range(int(count)):
            word = input("First Pair ex word1-word2 -: ")
            if "-" in word:
               word_pair = word.split("-")
               synonyms[word_pair[0]] = word_pair[1]
            else:
                print('Incorrect value Try Again')
                continue
        return synonyms
    else:
        print('Type correct Value ex. int type  0 - 9 ')




while True:
    words_count = input("Set count of word pair: ")

    syn = getSynonym(words_count)
    print('for exit press e')
    syn_word = input('Write word: ')
    if syn_word == 'e':
        break
    else:
         for i in syn.keys():
            if i == syn_word:
               print('the synonium of word is syn'.format(word=syn_word,syn=syn[i]))
    break


