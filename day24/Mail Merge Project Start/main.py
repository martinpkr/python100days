#TODO: Create a letter using starting_letter.txt



with open('./Input/Names/invited_names.txt', 'r') as f:
    names = f.readlines()
    replaced = ''
    for name in names:
        name.replace('\n','').strip()
        with open('./Input/Letters/starting_letter.txt', 'r') as letter:
            ready_to_send = letter.read().replace('[name]',name)
        with open(f"./Output/ReadyToSend/letter_for_{name}", 'w') as new_file:
            new_file.write(ready_to_send)
        # print(name)
        #




#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp