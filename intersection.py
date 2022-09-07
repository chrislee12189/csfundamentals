x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple", "banana"}

for word1 in x:
    for word2 in y:
        if word1 == word2:
            print(word1)

