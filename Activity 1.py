string_word = input("Please enter a word in all caps: ")

for i in string_word:

    if (i == "A"):

        print(f"\nThe letter A has been found in {string_word}")
        break
    else:
        print(f"\nThe letter A has not been found in {string_word}")

print("\nThank you for using this programe!")