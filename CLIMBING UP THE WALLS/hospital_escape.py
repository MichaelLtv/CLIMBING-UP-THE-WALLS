#-------------------------------------------------------------------------------
# Name:        hospital_escape.py
# Purpose:      Text-based game. Escape the bloodstained hospital.
#
# Author:      Lam.M
#
# Created:     12/01/2016
# Copyright:   (c) Michael 2016
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import pyglet

#Define all the rooms
room_list = []
#Hallway
room = ["You are in a dimly lit hallway. \nThere is a door to the west and a locked door to the east that leads out of the hospital.", None, None, None, 1, "A trail of blood leads to the sickroom... 'What happened here?'", "'Miller, I have been making these tapes for years. \nI don't know what will happen to your memory when you wake up so you need to trust me.\n Everything you need to know will be in these tapes.'"]
room_list.append(room)
#Sickroom
room = ["You are in a sickroom. Streaks of blood run straight across the bedsheets, and the room has been trashed. \nThere is a door to the north and a door to the east.", 2, 0, None, None, "The blood in the room seems quite fresh...", "'Hello Miller, I'm Dr. Mendel. \nYou will be the first test subject for our memory loss trial. \nSo what is it that you want to so badly forget?'"]
room_list.append(room)
#Nursery
room = ["You are in a nursery. On the wall, 'SEE NO EVIL' is written in blood. \nThere is a door to the north, a door to the east, and a door to the south.", 6, 3, 1, None, "On the floor, a trail of blood stretches toward the east and north.", None]
room_list.append(room)
#Delivery Room
room = ["You are in a delivery room. On the wall, 'HEAR NO EVIL' is written in blood. \nThere is a locked door to the east and a door to the west.", None, None, None, 2, "A trail of blood continues to stretch to the east... 'Why?'", "'Dr. Mendel again, Miller seems to be responding well to the treatment. \nHe seems to have forgotten some key moments from the war. \nBecause the drug seems to be working well, we have a new test subject coming in tomorrow.'"]
room_list.append(room)
#Dispensary
room = ["You are in a dispensary. The shelves have been cleared out, and the ground is littered with syringes. \nThere is a door to the east and a door to the west.", None, 5, None, 3, "The lights are too dim to make out anything in detail.", None]
room_list.append(room)
#Padded Cell
room = ["It is pitch black and you have no vision. \nYou remember that there is a door to the west.", None, None, None, 4, "'I really shouldn't stay here without a light...'", None]
room_list.append(room)
#Office
room = ["You are in an office. On the wall, 'SPEAK NO EVIL' is written in blood. \nThere is a closet to the west, a door to the east, and a door to the south.", None, 7, 2, 9, "You pick up a letter from the desk. \nIt reads, \n'If you're reading this, it too late. Miller you might not remember anything, but that's for your own good. \nHe doesn't know you're here. Miller you're our only hope. \nI tried my best to lock him away but he has the key. Take this and complete the mission. \nI'm counting on you - ' \nThe rest of the letter seems to have been torn off. 'Who wrote this, and how does he know my name?'", "'Hello Max, I'm Dr. Mendel. \n You will be the second test subject for our memory loss trial. \nI assume you want to forget everything about the murder you committed 20 years ago?'"]
room_list.append(room)
#Ward
room = ["You are in a ward. \nThere is a locked door to the east and a door to the west.", None, None, None, 6, None, None]
room_list.append(room)
#Operating Room
room = ["You are in an operating room. There is blood all over the ground. \nTo the north, there is a table. There is a door to the west.", 10, None, None, 7, "All the equipment is still on...", "'This is Dr. Mendel. I have made a huge mistake. \nThe full dosage of the drug has caused Miller to fall into a coma. \nI'm not sure what will become of his memory when he wakes up.'"]
room_list.append(room)
#Closet
room = ["You open the closet and find two door keys. You step back to the center of the room. \nYou are in an office. \nThere is a closet to the west, a door to the east, and a door to the south.", None, 7, 2, 9, "You pick up a letter from the desk. \nIt reads, \n'If you're reading this, it's too late. Miller you might not remember anything, but that's for your own good. \nHe doesn't know you're here. Miller you're our only hope. \nI tried my best to lock him away but he has the key. Take this and complete the mission. \nI'm counting on you - ' \nThe rest of the letter seems to have been torn off. 'Who wrote this, and how does he know my name?'", "'Hello Max, I'm Dr. Mendel. \n You will be the second test subject for our memory loss trial. \nI assume you want to forget everything about the murder you committed 20 years ago?'"]
room_list.append(room)
#Table
room = ["You pick up a flashlight from the table. You step back to the center of the room. \nYou are in an operating room. There is blood all over the ground. \nThere is a table to the north and a door to the west.", 10, None, None, 7, "All the equipment is still on...",  "'This is Dr. Mendel. I have made a huge mistake. \nThe full dosage of the drug has caused Miller to fall into a coma. \nI'm not sure what will become of his memory when he wakes up.'"]
room_list.append(room)
#Outside
room = ["You escaped the hospital! \nYou run away as fast as you can, never looking back at that cursed place. \n'I'm safe now,' you think to yourself. But in the corner of your eye, a shadowy figure appears admist the trees."]
room_list.append(room)

def invalid(str):
    '''
    Prints invalid input message with the player's invalid command.
    :param str: - Players invalid command
    :return: Invalid input message
    '''
    print "Invalid input. You entered '" + str + "'. The available commands are within the parantheses."
    print ""

current_room = 0
moves = 0
actions = ["n", "e", "s", "w", "north", "east", "south", "west", "inspect", "collect", "play"]
inventory = []
tape_count = 0
tape_list = []

music = pyglet.media.load("1-09 Climbing Up the Walls.mp3", streaming=False)
music.play()

#Print the opening of the game
print "CLIMBING UP THE WALLS"
print "Episode I: The Bloodstained Hospital"
print """

"""
print "You wake up in an abandoned hospital and your head hurts. \nAs you look around, you see bloodstains all over the walls. \nYou need to get out of here! But how? \nYou look at a nearby map and find where you are."
print ""

#All game logic
while True:
    print room_list[current_room][0]
    print """
    """
    #If the user escapes the hospital, end the game
    if current_room == 11:
        break
    #Prompt the user for a direction
    user = raw_input("What should you do? [n/e/s/w/inspect/collect/play] Enter 'quit' to quit the game: \n")
    user.lower()
    #Add one each time the user performs an action
    moves += 1
    #Print statement when the user has moved 11 times
    if moves == 11:
        print "Through the walls, you hear a muffled gunshot, startling you. \n'What was that?!' \nSlowly, you regain your composure."
    #Change the room descriptions if the user has found the two door keys
    if current_room == 9:
        #Change the closet description so that the closet is empty and the user remains in the office
        room_list[9][0] = "You open the closet and it is empty. You step back to the center of the room. \nYou are in an office. \nThere is a closet to the west, a door to the east, and a door to the south."

        #Change the ward description so that the user unlocks the east door and can access the room to the east
        room_list[7][0] = "You are in a ward. \nThere is a locked door to the east and a door to the west. \nYou unlock the door to the east."
        room_list[7][2] = 8

        #Change the delivery room description so that the user unlocks the east door and can access the room to the east
        room_list[3][0] = "You are in a delivery room. \nThere is a locked door to the east and a door to the west. \nYou unlock the door to the east."
        room_list[3][2] = 4

        #Change the hallway description so that the user finds out the two keys are too small to work on the lock
        room_list[0][0] = "You are in a dimly lit hallway. \nThere is a door to the west and a locked door to the east that leads out of the hospital. \nYou try to use the two keys on the lock, but they are too small."

    #Change the room description if the user has found the flashlight
    elif current_room == 10:
        #Change the table description so that the table is empty and the user remains in the operating room
        room_list[10][0] = "You search the table, but it's empty. You step back to the center of the room. \nYou are in an operating room. There is blood all over the ground. \nThere is a table to the north and a door to the west."

        #Change the padded cell description so that the user can now see with the flashlight and finds the large key
        room_list[5][0] = "It is pitch black. \nYou use the flashlight and see that you are in a padded cell. A dead body is splayed out on the floor, blood seeping from what must be a gunshot wound. He is holding a large key. \nWalls that were once pristine white are now drenched in crimson. \nYou pry the large key from the dead man's hands. \nThere is a door to the west."
        room_list[5][5:] = ["You grab the gun and check the ammunition. The magazine is full, and you cannot find any shell casings on the ground. \nThe gun was never even fired. \nSo then where did that gunshot come from? And who killed this man?", "'Dr. Mendel here. \nMax has not responded well to the treatment, and is showing violent and psychotic behaviour. \nLast week, he tried to attack a nurse, and since then we have moved him to a padded cell.'"]

    #Change the room description if the user has found the large key
    elif room_list[5][0] == "It is pitch black. \nYou use the flashlight and see that you are in a padded cell. A dead body is splayed out on the floor, blood seeping from what must be a gunshot wound. He is holding a large key. \nWalls that were once pristine white are now drenched in crimson. \nYou pry the large key from the dead man's hands. \nThere is a door to the west." and current_room == 5:
        #Change the padded cell descripiction so that the user does not find the large key
        room_list[5][0] = "It is pitch black. \nYou use the flashlight and see that you are in a padded cell. A dead body is splayed out on the floor, blood seeping from what must be a gunshot wound. \nWalls that were once pristine white are now drenched in crimson. \nThere is a door to the west."

        #Change the hallway description so that the user unlocks the east door and can exit the hospital. A new tape and inspect is available.
        room_list[0] = ["You are in a dimly lit hallway. \nThere is a door to the west and a locked door to the east that leads out of the hospital. \nYou unlock the door to the east with the large key.", None, 11, None, 1, "On the exit door, 'MILLER' is written in blood. \nYou try to remember, \n'Was that there before?'", "'MILLER... WE SHOULDN'T TRY TO FORGET...'"]

    #Quit command for the user
    if user == "quit":
        confirm = raw_input("Are you sure you want to quit? [y/n]: \n")
        confirm.lower()
        if confirm == "yes" or confirm == "y":
            print """

"""
            print "Thanks for playing!"
            quit()
        elif confirm == "no" or confirm == "n":
            print "The game will resume."
            print ""
        else:
            invalid(confirm)
    #Perform if the user moves, inspects, or collects
    else:
        #Handles invalid inputs
        if user not in actions:
            invalid(user)
        #Handles inspections
        elif user == "inspect":
            if room_list[current_room][5] is None:
                print "Nothing to see here..."
                print ""
            else:
                print room_list[current_room][5]
                print ""
        #Handles collecting tapes
        elif user == "collect":
            if room_list[current_room][6] is None:
                print "Can't find anything..."
                print ""
            elif room_list[current_room][6] not in inventory:
                    inventory.append(room_list[current_room][6])
                    tape_count += 1
                    tape_list.append(str(tape_count))
                    print "You have found a tape. It plays: "
                    print room_list[current_room][6]
                    print ""
            else:
                print "You already found a tape here."
                print ""
        #Handles the playback of tapes
        elif user == "play":
            if tape_count == 0:
                print "You do not have any tapes."
                print ""
            else:
                print "You have", tape_count, "tape(s)."
                play_tape = raw_input("Which tape do you want to play?" + str(tape_list).replace(", ", "/").replace("'", "") + "\n")
                if play_tape not in tape_list:
                    print "Please pick a valid number between 1 and", str(tape_count) + "."
                    print ""
                else:
                    print inventory[int(play_tape)-1]
                    print ""
        #Handles all movement
        else:
            next_room = room_list[current_room][actions.index(user[0])+1]
            if next_room is None:
                print "You can't go that way."
                print ""
            else:
                current_room = next_room

print "THE END."
