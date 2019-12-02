
import random
import sys
class methods():

    def for_letters(alpha, alpha_list):
        word_alpha = ""
        while alpha > 0:
            word_alpha += random.choice(alpha_list)
            alpha -= 1
        return word_alpha

    def for_numbers(num, num_list):
        word_num = ""
        while num > 0:
            word_num += str(random.choice(num_list))
            num -= 1
        return word_num

    def for_symbols(sym, sym_list):
        word_sym = ""
        while sym > 0:
            word_sym += str(random.choice(sym_list))
            sym -= 1
        return word_sym

    def to_shuffle(word):
        list1 = list(word)
        random.shuffle(list1)
        password = ""
        for item in list1:
            password += item
        return password

    def run_this_test(alpha_list, num_list, sym_list):

        while (True):
            print("WELCOME TO PASSWORD GENERATOR PROGRAM\n")
            length = int(input("What is the length of your password? "))
            alpha = int(input("How many letters should it consist of? "))
            num = int(input("How many numbers should it consist of? "))
            sym = int(input("How many symbols should it consist of? "))

            if (length == alpha + num + sym):
               word_al = methods.for_letters(alpha, alpha_list)
               word_num = methods.for_numbers(num, num_list)
               word_sym = methods.for_symbols(sym, sym_list)

               new_word = word_al + word_num + word_sym
               password = methods.to_shuffle(new_word)
               print(password)
               break

            elif (length < alpha + num + sym):
                print("The length of password required is too short for the given inputs.")
            else:
                print("Given inputs are not enough to generate required length of password.")
        else:
            sys.exit(1)


class main():
    """
    This program will generate password for the user
    """
    lowercase_letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    uppercase_letters = []
    for letter in lowercase_letters:
        uppercase_letters.append(letter.upper())

    all_letters = lowercase_letters + uppercase_letters
############################################### NUMBERS
    numbers = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]
 ############################################## SYMBOLS
    symbols = [
        '!', '@', '/', '<', '>', '_', '-', '+', '='
    ]
############################################## THIS RUNS THE PROGRAM
    print("This is the start of the program\n")
    print(methods.run_this_test(all_letters, numbers, symbols))
    print("This is the end of the program\n")



if __name__ == "__main__":
    main()