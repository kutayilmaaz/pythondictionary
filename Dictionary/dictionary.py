import shelve

english_dic = "english_dictionary.db"

english = shelve.open(english_dic)

print("Welcome, type q for exit.")

while True:      
 word = input("Type the word: ").lower()
 if word == "q":
        break
 elif word in english:
     print(word, ":", english[word])
 else:
     add = input("Word is not defined. Type meaning of this word: ").lower()
     english[word] = add
     print(word, " is defined as ", add )

english.close()