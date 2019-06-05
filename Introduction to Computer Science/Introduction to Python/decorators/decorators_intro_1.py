def shout(word = "да"):
    return word.capitalize() + "!"

print(shout())

scream = shout


print(scream())