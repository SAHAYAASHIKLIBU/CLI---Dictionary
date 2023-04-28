import requests
import json
from googletrans import Translator
import os


#The free api used here
url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

#Function for search the word
def searchDefinition(word):
    response=requests.get(url+word.lower())
    if response.status_code==200:
        data=json.loads(response.text)
        mean=data[0]["meanings"][0]["definitions"][0]["definition"]
        return mean
    else:
        return f"Not Found"
def translateWord(word):
    translated=Translator().translate(word,src="en",dest="ta").text
    return translated
def exampleSentence(word):
    response=requests.get(url+word.lower())
    if response.status_code==200:
        data=json.loads(response.text)
        try:
            return data[0]["meanings"][1]["definitions"][0]["example"]
        except (IndexError,KeyError):
            pass
        try:
            return data[0]["meanings"][2]["definitions"][0]["example"]
        except(IndexError,KeyError):
            pass
        return f"Example Not  found"
    else:
        return f"Not Found"

ch=1
print("|-------------------------------------------------------|")
print("|   Press 1 for show this screen                        |")
print("|   Press 2 for enter the word and find the definition  |")
print("|   Press 3 for translate the given word                |")
print("|   Press 4 for both definition and translate           |")
print("|   Press 5 for translation of the definition           |")
print("|   Press 6 for give example sentence if available      |")
print("|   press 7 for translate the sentence                  |")
print("|   Press 8 for write everything for future reference   |")
print("|   Press 9 for exit                                    |")
print("|-------------------------------------------------------|\n\n")
while ch!=9:
    try:
        ch=int(input("\n\n\t\tEnter your choice(Numbers only):"))
    except(ValueError):
        print("\n\nMust enter numbers")
    if ch==1:
        print("|-------------------------------------------------------|")
        print("|   Press 1 for show this screen                        |")
        print("|   Press 2 for enter the word and find the definition  |")
        print("|   Press 3 for translate the given word                |")
        print("|   Press 4 for both definition and translate           |")
        print("|   Press 5 for translation of the definition           |")
        print("|   Press 6 for give example sentence if available      |")
        print("|   press 7 for translate the sentence                  |")
        print("|   Press 8 for write everything for future reference   |")
        print("|   Press 9 for exit                                    |")
        print("|-------------------------------------------------------|\n\n")
    elif ch==2 :
        word=str(input("\n\nEnter the word:"))
        print(f"{word} : {searchDefinition(word)}\n")
    elif ch==3:
        word=str(input("\n\nEnter the word:"))
        print(f"{word} : {translateWord(word)}\n")
    elif ch==4:
        word=str(input("\n\nEnter the word:"))
        print(f"{word} : {searchDefinition(word)}\n")
        print(f"{word} : {translateWord(word)}\n")
    elif ch==5:
        word=str(input("\n\nEnter the word:"))
        ok= searchDefinition(word)
        print(f"{ok} : {translateWord(ok)}\n")
    elif ch==6:
        word=str(input("\n\nEnter the word:"))
        ok=exampleSentence(word)
        print(ok)
        print(translateWord(ok),"\n")
    elif ch==7:
        sentence=str(input("Enter the sentence:"))
        print(f"{sentence}:{translateWord(sentence)}")
    elif ch==8:
        word=str(input("\n\nEnter the word:"))
        defe=searchDefinition(word)
        exem=exampleSentence(word)
        fileName=str(input("Enter the file name with extenction(default ref.txt): "))
        if fileName=="":
            fileName="ref.txt"
        path=str(input("Enter the path(default current location):"))
        if path=="":
            path="./"
        if  fileName in os.listdir(path):
            with open(fileName,"a") as f:   
                f.write("\n-----------------------------------------------------------------------------------\n")
                f.write(f"{word}:{translateWord(word)}\n")
                f.write(f"{defe}:{translateWord(defe)}\n")
                f.write(f"{exem}:{translateWord(exem)}")
                f.close
        else:
             with open(fileName,"a") as f:   
                f.write("\n-----------------------------------------------------------------------------------\n")
                f.write(f"{word}:{translateWord(word)}\n")
                f.write(f"{defe}:{translateWord(defe)}\n")
                f.write(f"{exem}:{translateWord(exem)}")
                f.close
    elif ch==9:
        break
    else:
        print("\n\n***Invalid input***\n\n")

    
