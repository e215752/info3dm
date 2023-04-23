import string

ensyu= ""

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentence = sentence.translate(str.maketrans('', '', string.punctuation)).split()

for i in range(0,len(sentence)):
    ensyu += str(len(sentence[i]))

print(ensyu)
