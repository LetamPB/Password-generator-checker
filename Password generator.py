# creating a password generator#
import random
import re

user_choice = input(
    "This is a password generator and/or checker \n To choose generator enter 'G'\n To choose checker enter 'C' ").upper()

if user_choice == "G":
    file_path = input(
        "Enter a file path for the password to be stored\n It's optional: ")
    extra_details = input(
        "Enter anything else you would like to be associated with storing the password \n for example: This is my youTube password ")
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "#*&^%$£!?/"

    ans = lower_case + upper_case + numbers + symbols
    length = 12
    password = "".join(random.sample(ans, length))
    if not (file_path == ""):
        with open(file_path, "a") as file:
            file.write("\n"+extra_details + " "+password)
    print("Generated password  is ", password)

elif user_choice == "C":
    original_password = input("Enter the password to be checked ")
    if len(original_password) < 12:
        raise ValueError("Your password must be at least 12 characters")
    lower_case_requirement = re.search("[a-z]", original_password)
    if not lower_case_requirement:
        raise ValueError(
            "Your password must have at least 1 lowercase alphabet character")

    upper_case_requirement = re.search("[A-Z]", original_password)
    if not upper_case_requirement:
        raise ValueError(
            "Your password must have at least 1 upper case alphabet character")

    digit_requirement = re.search("[0-9]", original_password)
    if not digit_requirement:
        raise ValueError("Your password must have at least one digit")

    special_character_requirement = re.search(
        "[#*&^%$£!?/-]", original_password)
    if not special_character_requirement:
        raise ValueError(
            "Your password must have at least one special character in this box:[#*&^%$£!?/-]")

    else:
        print("Your password meets all criteria")
else:
    print("Invalid entry, G or C only")
