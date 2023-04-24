def Pig_Latin(word):
    nguyen_am='aeiou'
    if word[0] in nguyen_am:
        return word + 'way'
    else:
        for i in range(1,len(word)):
            if word[i] in nguyen_am:
                return word[i:]+word[0:i]+'ay'
        return word+'ay'
text=input("nhap: ")
words=text.split()
pig_latin_words = [Pig_Latin(word) for word in words]
pig_latin_text = " ".join(pig_latin_words)
print("Dich sang Pig Latin: " + pig_latin_text)