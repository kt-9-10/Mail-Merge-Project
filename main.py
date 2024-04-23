with open("./Input/Letters/starting_letter.txt") as starting_letter:
    content = starting_letter.read()

with open("./Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        stripped_name = name.rstrip("\n")
        replaced_content = content.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(replaced_content)
