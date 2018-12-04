#Jacob West, Aaron Newman, Anthony Davis, Jared Miller
#CST205 
#Strategy Game

# Game launches automatically when you click "Load Program"

# Defined data types based on assigned values
basementUnlocked = false
basementBoardBroken = false
haveHammer = false
kickAttempt = 0
haveBasementKey = false
flag1 = false
finalKey = false
atticFlag = false
hammerStrikes = 0
flashlight = false
crowbar = false
charname = ""

def game():

  #Initialize global variables on game start
  global basementUnlocked, basementBoardBroken, haveHammer, kickAttempt, haveBasementKey
  global flag1, finalKey, atticFlag, flashlight, crowbar, charname
  
  #Misc gf1 flags, names are self-explanatory
  basementUnlocked = false
  basementBoardBroken = false
  haveHammer = false
  
  # How many times a player attempts to kick the basement door
  kickAttempt = 0
  
  #test flag
  haveBasementKey = false
  
  # How many times a player strikes the basement door board
  # with a hammer
  hammerStrikes = 0
  
  #Flashlight must be found to see in the basement
  flashlight = false
  
  #Crowbar must be used to open the floor board
  crowbar = false

  #This is the flag for the attic, you need this to get to
  #the basement.
  flag1 = false
  
  #This is the flag for the basement, you need this and 
  #flag1 to be true to unlock the secret room in the main room.
  finalKey = false
  
  #atticFlag is so when we open the attic, it doesn't need to
  #be reopened. This avoids having to do the puzzle each time.
  atticFlag = false
  
  #start in the main room
  welcome()
  
  charname = requestString("Enter your name:")
  
  mainRoom()
  
  printNow("Leaving Game")
  
def welcome():
  welcomemes = ""
  welcomemes = welcomemes + "Welcome to Team 3's Strategy Game!\n"
  welcomemes = welcomemes + "This is a strategy game where you will need to navigate through the rooms of a house.\n"
  welcomemes = welcomemes + "You will need to interact with the different puzzles in each room to progress.\n"
  welcomemes = welcomemes + "You might even find something secret!\n"
  welcomemes = welcomemes + "You can quit the game at any time simply by typing \"quit\" at any time.\n"
  welcomemes = welcomemes + "You can also display this message again by typing \"help\" at any time.\n"
  welcomemes = welcomemes + "Now go break a leg!"
  showInformation(welcomemes)
  
def mainRoom():
  global flag1, finalKey, atticFlag
  
  str = ""
  
  #Secret Final Room
  if (finalKey == true):
    printNow("Welcome to the main room. A secret door has opened.\n")
    printNow("Would you like to enter? (y) or (n)")
    while(str != 'y' and str != 'n' and str != "quit" and str != "help"):
      str = requestString("Choose y or n")
    if str == 'y':
      finalRoom()
    if str == 'n':
      printNow("Would you like to go to Room 1 or 2?")
      while(str != '1' and str != '2' and str != "quit" and str != "help"):
        str = requestString("Choose 1 or 2")
      if str == '1':
        gf1()
      if str == '2':
        gf2()
      if str == "quit":
        quit
      if str == "help":
        welcome()
        mainRoom()
    if str == "quit":
      quit  
    if str == "help":
      welcome()
      mainRoom()
  
  #Room 1 and 2 Navigation        
  if (flag1 == false or finalKey == false):
    printNow("Welcome to the main room.")
    printNow("Would you like to go to Room 1 or 2?")
    while(str != '1' and str != '2' and str != "quit" and str != "help"):
      str = requestString("Choose 1 or 2")
   
    #Room 1
    if str == '1':
      gf1()
    
    #Room 2
    if str == '2':
      gf2()
    
    #Quit
    if str == "quit":
      quit
    
    #Help
    if str == "help":
      welcome()
      mainRoom()

# To reach the basement, you need the key found in the attic.
# You also need to break a board off the basement door with
# a hammer.      
def gf1():
  global basementUnlocked, basementBoardBroken, haveHammer, kickAttempt, hammerStrikes, charname

  # Construct entrance message depending on player progress
  roomMessage = "\nYou see "
  
  if basementUnlocked:
    roomMessage += "an unlocked door."
  elif not basementUnlocked:
    roomMessage += "a locked door."
  
  if not basementBoardBroken:
    roomMessage += " There's a board keeping it shut."
  
  # Print entrance message
  printNow(roomMessage)
    
  # Set to a number symbol; a blank string is not properly converted to an int
  str = "0"
  
  while str != "help" and str != "quit" and (int(str) < 1 or int(str) > 5):
    str = requestString("What will you do?\n1) Go back to the main room\n2) Unlock door\n3) Open door\n4) Break board\n5) Inspect hammer")

  # 1) Go back to the main room
  if str == "1":
    mainRoom()      
      
  # 2) Unlock door
  if str == "2":    
    if basementUnlocked:
      printNow("You already unlocked the door.")
    elif haveBasementKey and not basementUnlocked:
      printNow("Unlocked the basement door!")
      global basementUnlocked
      basementUnlocked = true
    else:
      printNow("You need a key in order to unlock the door.")
    gf1()
         
  # 3) Open door
  if str == "3": 
    if not basementUnlocked:
      printNow("The door is locked.")
      gf1()
    elif basementUnlocked and not basementBoardBroken:    
      printNow("That board is too strong. You'll have to break it.")
      gf1()
    elif basementUnlocked and basementBoardBroken:
      printNow("Entering the basement.")
      basement()    
        
  # 4) Break board
  # If the player attempts to kick the board too many times, GAME OVER
  if str == "4":
    # If you don't have the hammer:
    if not haveHammer:
      kickAttempt += 1
      
      if kickAttempt == 1:
        showInformation("You kicked the board. Stop doing that.")
        gf1()
        
      elif kickAttempt == 2:
        showInformation("Seriously " + charname + " you need to stop.")
        gf1()
   
      else:
        kickAttempt = 0
        showInformation("You broke your leg. Good job. Game Over.\n")
        str = "quit"
        quit
    
    elif basementBoardBroken:
      printNow("You already broke the board.")
      gf1()  
      
    else:
      hammerStrikes += 1
      if hammerStrikes == 1:
        showInformation("Wham! Hit it again!")
      elif hammerStrikes == 2:
        showInformation("There's a huge crack in it! Keep going!")
      elif hammerStrikes == 3:
        showInformation("Almost...!")
      else:
        showInformation("WHAM!!! The board is broken!")
        basementBoardBroken = true
      gf1()
    
  # 5) Inspect hammer
  if str == "5":
    if not haveHammer:
      showInformation("You picked up a hammer lying in the corner.")
      haveHammer = true
    elif basementBoardBroken:
      printNow("You don't see anything to break in here.")
    else:
      printNow("You're holding a hammer. Maybe you can break something with it.")
    gf1() 
  
  #Quit
  if str == "quit":
    quit
    
  #Help
  if str == "help":
    welcome()
    gf1()

def gf2():
  global flag1, finalKey, atticFlag
  str = ""
  
  #Flags for the puzzle in the room
  paintFlag = false
  bookFlag = false
  stringFlag = false
  
  printNow("Welcome to Room 2.")
  
  #This will happen only if you have not entered the room and done the puzzle
  if atticFlag == false:
    printNow("The door locks behind you as you enter the room.")
    while (paintFlag == false or bookFlag == false or stringFlag == false):
      printNow("You see a painting, a bookcase, and a string hanging from the ceiling.")
      printNow("Would you like to move the painting, grab a book, or pull the string?")
      str = ""
      
      #Condition for while loop to ensure the user enters either:
      #move, grab, pull, quit, or help
      while(str != "move" and str != "grab" and str != "pull" and str != "quit" and str != "help"):
        str = requestString("Type move, grab, or pull")
      
      #The user wants to move the painting
      #If they move the painting first before grabbing or pulling, nothing happens
      #This is the second step to unlock the attic
      if str == "move":
        if bookFlag == false:
          printNow("You move the painting, but it does nothing.")
          printNow("You hear a buzz in the distance.")
          printNow("Maybe you should try something different first.")
        else: 
          printNow("You move the painting, and it stops crooked.")
          printNow("You hear a click in the distance.")
          printNow("It reminds you of a good sound.")
          paintFlag = true
      
      #The user wants to grab the book
      #If they try to grab the book again after already doing it, it resets all progress.
      #This is the first step to unlock the attic        
      if str == "grab":
        if paintFlag == true:
          printNow("You grab a book, and the painting slides back.")
          printNow("You hear a buzz in the distance.")
          printNow("Maybe you should try something different first.")
          paintFlag = false
          bookFlag = false
        else:
          printNow("You grab a book, and it slides partially out of the bookcase.")
          printNow("You hear a click in the distance.")
          printNow("It reminds you of a good sound.")
          bookFlag = true
    
      #The user wants to pull the string
      #If they try to grab the string without doing step 1 and 2, it resets all progress
      #This is the final step to unlock the attic        
      if str == "pull":
        if bookFlag == false or paintFlag == false:
          printNow("You pull the string, but it does nothing.")
          printNow("You hear a buzz in the distance.")
          printNow("Maybe you should try something else first.")
          bookFlag = false
          paintFlag = false
        else:
          printNow("You pull the string, and a ladder comes down from the ceiling, leading to the attic.")
          printNow("The door you entered through unlocks.")
          stringFlag = true
          atticFlag = true
      
      #Quit  
      if str == "quit":
        break
      #Help
      if str == "help":
        welcome()
        gf2()
  
  #If the user has finished the puzzle and unlocked the attic ladder
  if atticFlag == true:
    #options to go to Main or Attic       
    printNow("Would you like to go back to the main room (1) or enter the attic (2)?")
    while(str != '1' and str != '2'  and str != "quit" and str != "help"):
      str = requestString("Choose 1 or 2")
    #Main Room
    if str == '1':
      mainRoom()
    #Attic
    if str == '2':
      attic()
    #Quit
    if str == "quit":
      quit
    #Help
    if str == "help":
      welcome()
      gf2()

def attic():
  global flag1, finalKey, atticFlag
  global haveBasementKey, haveHammer
  
  str = ""
  #options to go to room 2
  printNow("Welcome to the Attic.")
  
  printNow("As you enter the attic, a light comes on and you see a chest inside the room.")
  printNow("You notice that there is not a normal lock on the chest, but an indentation that reminds you of a tool.")

  if haveHammer == false or haveBasementKey == true:
  
    if haveBasementKey == true:
      printNow("You already have the key from the chest.")
    
    printNow("Would you like to go back to room 2 (1)?")
    flag1 = true
    print flag1
    while(str != '1' and str != "quit" and str != "help"):
      str = requestString("Choose 1 to go back")
    #Room 2
    if str == '1':
      gf2()
    #Quit
    if str == "quit":
      quit
    #Help
    if str == "help":
      welcome()
      attic()  
      
  if haveHammer == true:
    while(str != "y" and str != "n" and str != "quit" and str != "help"):
      str = requestString("Would you like to place the hammer on the indentation? (y/n)")
      
    if str == "y":
      haveBasementKey = true
      flag1 = true
      printNow("You place the hammer into the indentation, and the chest pops open.")
      printNow("You grab a key labeled \"basement\" from the chest, and go back to room 2.")
      gf2()      
      
    if str == "n":
      printNow("Would you like to go back to room 2 (1)?")
      while(str != '1' and str != "quit" and str != "help"):
        str = requestString("Choose 1 to go back")
      
      #Room 2
      if str == '1':
        gf2()
      
      #Quit
      if str == "quit":
        quit
      
      #Help
      if str == "help":
        welcome()
        attic()  
    
    #Quit  
    if str == "quit":
      quit
    
    #Help
    if str == "help":
      welcome()
      gf2()

##################
#Basement Function
##################
def basement():
  global flag1, finalKey, atticFlag, basementUnlocked, flashlight, crowbar
  str = ""
  
  shovelBroken = false
  
  #Basement introduction
  printNow("\n~~Welcome to the Basement~~\n")
  
  #If user has already entered and obtained the key
  if finalKey == true:
    printNow("You see a broken floorboard and some useless old junk")
    printNow("Who just hangs out in a dark basement? Now go find that hidden door!!")
    printNow("Return to the Main Room.")
    gf1()

  #While the user hasn't obtained the flashlight and therefore the key
  #Pick up the flashlight and find the hidden key
  #The user has to pick up the flashlight before progressing
  while flashlight == false:
    printNow("It sure is dark down here... The light switch doesn't appear to be working.")
    printNow("As your eyes adjust, you notice a flashlight on the washing machine")
    str = requestString("Pick up flashlight? (y/n)\n")
    
    #Once user selects 'y' flashlight flag is changed to True
    if str == 'y' or str == "yes":
      printNow("\nAhhh...That's better. Now lets see what's down here.")
      printNow("You start walking around to explore the room, when you notice a hollow floor board")
      printNow("You can't lift it with you hands...There must be something to pry the board up with")
      flashlight = true
    elif str == 'n' or str == "no":
      printNow("\nYou're blind without a light.\n")
    #Quit
    elif str == "quit":
      break
    #Help
    elif str == "help":
      welcome()
      
  #User must use the crowbar to find the hidden box
  if flashlight == true:
    while crowbar == false:
      
      #Option 3 is crowbar
      #User can play with the other 2 options to see what happens
      while str != '3':
        str = requestString("In the corner of the room there's a baseball bat(1), an old shovel(2), and a crowbar(3)\nPick one:")
        if str == '1':
          printNow("\nNice bat...Plan on breaking something??\nPick again.\n")
        elif str == '2':
          if shovelBroken == false:
            printNow("You place the shovel under the floorboard and try to pry it open")
            printNow("OOPS!!! The shovel broke...\nPick again.\n")
            shovelBroken = true
          else:
            printNow("The shovel is broken.")
        #Quit
        elif str == "quit":
          break
        #Help
        elif str == "help":
          welcome()
      
      #If they use the crowbar, they find the hidden box with the key
      #User is then prompted exit back to ground floor 1
      if str == '3':
        printNow("The crowbar worked!!!\nThere seems to be a box under the board.")
        printNow("\nOpening the box...YOU HAVE FOUND THE KEY TO THE HIDDEN ROOM!!.\nReturn to the main room to enter the Hidden Room.")
        crowbar = true
        finalKey = true
        while str != '1':
          str = requestString("\nExit the basement and return to Room 1 (1)")
          if str == "quit":
            break
          if str == "help":
            welcome()
        if str == '1':
          gf1()
      #Break out of main while loop once finalKey (Hidden Key) is found
      break
  if str == "quit":
    quit
  printNow("\n~~Exiting the basement~~") 

def finalRoom():
  global flag1, finalKey, atticFlag, charname
  
  str = ""
  printNow("\nWelcome to the Secret Final Room. \nCONGRATULATIONS, " + charname.upper() + " YOU HAVE WON!")
  
  #return to the main room
  printNow("Press 1 to go back to main room(1)?")
  while(str != '1'  and str != "quit" and str != "help"):
    str = requestString("Choose 1 to go back")
  #Main Room
  if str == '1':
    mainRoom()
  #Quit
  if str == "quit":
    quit
  #Help
  if str == "help":
    welcome()
    finalRoom()  

#Game runs automatically
game()