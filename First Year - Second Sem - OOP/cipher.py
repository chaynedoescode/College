#LAB ASSIGNMENT # 1 - Problem No. 3
#Programmed by: Montanez, Andrei Chayne D.
#Course, Year, and Section: BSCpE 1-3
#Instructor: Engineer Julius S. Cansino
#Date of Submission: March 9, 2024
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#accepting input
user_input = input("Please enter message to cipher: ")
key = input("Please enter key word: ")

#converting everything to uppercase
user_input_upper = user_input.upper()
key_upper = key.upper()

#converting to list to prepare each character conversion to number
user_input_list = list(user_input_upper)
key_list = list(key_upper)

#converting message to number
message_in_number = []
for character in user_input_list:
    index_number = alphabet.find(character)
    message_in_number.append(index_number)

#converting key to numbers
key_in_number = []
for character_key in key_upper:
    index_number = alphabet.find(character_key)
    key_in_number.append(index_number)

#making the key as long as the message
message_length = len(message_in_number)
key_message_length = []

for i in range(0, message_length):
    key_index = i % len(key_in_number)
    key_message_length.append(key_in_number[key_index])

#adding the key and message per index
added_list = []
for i in range(0,message_length):
    add = message_in_number[i] + key_message_length[i]
    added_list.append(add)

#checking if the indexes exceeds 25
final_list = []
for i in range(0,message_length):
    if added_list[i]>=26:
        new_add = added_list[i] - 26
    else:
        new_add = added_list[i]

    final_list.append(new_add)

#converting the final list of numbers to letters
convertion = []
for i in final_list:
    letter = alphabet[i]
    convertion.append(letter)

#joining the list to output a single string
convertion_joined = ''.join(convertion)

#display of everything
print(f"""Message:{user_input} {message_in_number}
Key:{key} {key_message_length}
Add: {added_list}
Mod: {final_list}
Ciphertext: {convertion_joined}""")
