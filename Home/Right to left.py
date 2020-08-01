pharses = ("enough", "jokes")

sentence = ""

for i in range(len(pharses)):
    if i == len(pharses)-1:
        sentence += str(pharses[i])
    else:
        sentence += str(pharses[i]) + ","

newSentence = sentence.replace("right","left")
print(newSentence)
