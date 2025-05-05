"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Katarina Zorvan
email: katarina.zorvan@gmail.com
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

number_of_texts = len(TEXTS)

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# user verification

username = input("User: ")
if username not in users:
    print("Unregistered user, terminating the program..")
    exit()
 
password = input("Password: ")

if username in users:
    if users[username] == password:
        print(f"{'-' * 50}\nWelcome to the app, {username}\nWe have {number_of_texts} texts to analyze\n{'-' * 50}")
    else:
        print("Wrong password, terminating the program..")
        exit()

# text choice and word count

choice_of_text = int(input(f"Enter a number between 1 and {number_of_texts} to select: "))
selected_text = TEXTS[choice_of_text - 1].replace(",", "").replace(".","")
words = selected_text.split()

print(f"{'-' * 50}\nThere are {len(words)} words in the selected text.")

# text analysis: titlecase, uppercase, lowercase, numbers

title_case_count = 0
upper_case_count = 0
lower_case_count = 0
numbers_in_text = []

for word in words:
    if word.isupper():
        upper_case_count += 1
    if word[0].isupper():
        title_case_count += 1
    if word.islower():
        lower_case_count += 1
    if word.isdigit():
        numbers_in_text.append(int(word))

print(f"There are {title_case_count - upper_case_count} titlecase words.")
print(f"There are {upper_case_count} uppercase words.")
print(f"There are {lower_case_count} lowercase words.")
print(f"There are {len(numbers_in_text)} numeric strings.")
print(f"The sum of all the numbers is {sum(numbers_in_text)}\n{'-' * 50}")

# counting characters and their occurance in a text

character_counter = {}

for word in words:
    # if not word.isdigit(): - I wouldn't count numbers as words/characters but the example did.
    length = len(word)
    if length in character_counter:
        character_counter[length] += 1
    else:
        character_counter[length] = 1

print(f"{"LEN|":8}{"OCCURENCES":17}|NR.\n{'-' * 50}")

for length in sorted(character_counter):
    print(f"{length:3}|{'*' * int(character_counter[length]):21}|{character_counter[length]}")