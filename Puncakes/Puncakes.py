# This is the method and ingredients for making the pancakes, as you can see it is mostly ifs and elses.
def starting(): # def here defines the function starting which containst the method and ingred...
    ingred = input("Gather these ingredients:\n\n1 1/2 cups milk\n1 egg\n2 teaspons vanilla extract\n2 cups self-raising flour\n1/4 teaspoon bicarbonate of soda\n1/3 cup caster sugar\n25g butter, melted\n\n Done? Type yes.\n")
    if ingred == "yes": # I used input instead of print because it does the two things I need to do. Prints the text and saves the user input as a variable.
        step1 = input("Whisk milk, egg and vanilla together in a jug. Sift flour and bicarbonate of soda\ninto a bowl. Stir in sugar. Make a well in centre. Add milk mixture. Whisk until just\ncombined.\n\n Done? Type yes.\n")
        if step1 == "yes":
            step2 = input ("Heat a large non-stick frying pan over medium heat. Brush pan with butter. Using\n1/4 cup mixture per pancake, cook 2 pancakes for 3 to 4 minutes or until bubbles\nappear on surface. Turn and cook for 3 minutes or until cooked through. Transfer\nto a plate. Cover loosely with foil to keep warm. Repeat with remaining mixture,\nbrushing pan with butter between batches. Serve.\n\n Done? Type yes.\n")
        else:
            starting()
            if step2 == "yes":
                joke = input ("Congratulations!\nHey would you like to hear a joke? Done? Type yes.\n")
            else:
                starting()
                if joke == "yes":
                    print ("Why was 6 afraid of 7?\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\nWell actually, numbers are not sentient and thus\nare incapable of feeling fear.")
    else:
        starting()
        
# This the introductory conversation.    
yes = input("Hi! Would you like to make pancakes? Done? Type yes.\n")
if yes == "yes":
    print ("Lets get started!")
    starting()
else:
    imReady = input("Okay, say 'Im ready' when you want to start\n")
    if imReady == "Im ready":
        print ("Lets get started!")
        starting()
