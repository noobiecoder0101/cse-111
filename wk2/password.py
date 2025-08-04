LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
#noticed an issue with the special characters list and fixed it 
SPECIAL = list("!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~")

def word_is_inside_file (word, filename, case_sensitivity=False):
    if case_sensitivity == False:
        word = word.lower()
    with open(filename,"r", encoding="utf-8") as file:
        for line in file:
            polished_line = line.strip()
            if case_sensitivity == False:
                polished_line = polished_line.lower()
            if word == polished_line:
                return True
        return False

def word_has_character_in_it(word, character_list):
    for characters in word:
        if characters in character_list:
            return True
    return False
def word_complexity (word):
    complexity = 0
    if word_has_character_in_it(word, LOWER):
        complexity = complexity + 1
    if word_has_character_in_it(word, UPPER):
        complexity = complexity + 1
    if word_has_character_in_it(word, DIGITS):
        complexity = complexity + 1
    if word_has_character_in_it(word, SPECIAL):
        complexity = complexity + 1
    return complexity
def password_strength_calc(word, password_min_length=10, password_best_length=16 ):
    password_length = len(word)
    if password_length <= password_min_length:
        print(f"your password ({word}) is too short")
    elif password_length >= password_best_length:
        print(f"your password ({word}) is long -- Wonderful!")
    else:
        print(f"your password({word}) is ok in length.")
# def main(password):
#     while password != "q":
#         password = str(input("please input your password OR press 'q' to quit: ").lower())
def main():
    word = ""
    while word != "q":
        word = input("please input your password OR press 'q' to quit: ")
        #inputed a goodbye message for creativity
        if word.lower() == "q":
            print("I hope your password has been strengthened")
            break
        if word_is_inside_file(word, "toppasswords.txt", case_sensitivity = False):
            print("this password is in the list of most used passwords " )
            continue
        complexity_score = word_complexity(word)
        print(f"your complexity score is {complexity_score} out of 4")
        password_strength_calc(word)
        

if __name__ == "__main__":
    main()






