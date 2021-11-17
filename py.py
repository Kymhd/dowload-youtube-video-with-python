from random import shuffle
def liste_de_mot(text):
    print(text)
    shuffle(text)
    if len(text) < 10:
        print(text[:2])
    else:
        print(text[-3:])
    
text = input("liste de mots (mot1/mot2/mot3/mot4/mot5...: ").split("/")
liste_de_mot(text)