#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
name_list = []

with open("Day 24/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()
for name in names:
    name = name.strip()
    name_list.append(name)

with open("Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as contents:
    content = contents.readlines()
    for name in name_list:
        for line in content:
            line = line.replace("[name]", name)
            with open(f"Day 24\Mail Merge Project Start\Output\ReadyToSend\{name}.txt", "a") as new_file:
                new_file.write(line)
    
    


