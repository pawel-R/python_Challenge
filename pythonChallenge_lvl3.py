
text = open("lvl3.txt").read()


for k, v in enumerate(text):
    if (text[k - 4].islower() == True and
        text[k - 3].isupper() == True and
        text[k - 2].isupper() == True and
        text[k - 1].isupper() == True and
        v.islower() == True and
        text[k + 1].isupper() == True and
        text[k + 2].isupper() == True and
        text[k + 3].isupper() == True and
        text[k + 4].islower() == True):

        print(v, end="")






