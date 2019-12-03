from random import randint

sentence="Prezes TVP udzielił wywiadu Jackowi i Michałowi Karnowskim, w którym odniósł się m.in." \
         " do sprawy Mariana Banasia. - W sumie to TVP go pogrążyła. Słowa, które u nas wypowiedział" \
         " w Gościu Wiadomości, były dlań dużym problemem, przedmiotem ataku opozycji - powiedział."
def sentenceGenerator(sentence, n=5):
    sentence = sentence.replace(",","").replace("- ","")
    words = sentence.split(" ")
    resultSentence = ""
    #generowanie nowego randomowego zdania o określonej liczbie słów
    for i in range(n):
        resultSentence += words[randint(0,len(words)-1)] + " "
    resultSentence = resultSentence[0:len(resultSentence)-1]+"."
    return resultSentence
print("auto-sentence: ", sentenceGenerator(sentence))