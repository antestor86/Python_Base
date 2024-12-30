word = input("Add string: ")
corrected_words = ''
counter = 0
for i in word:
  if i == ":":
      corrected_words+=";"
      counter += 1
  else:
      corrected_words += i

print(corrected_words)
print(counter)

