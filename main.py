
def main():
  """
  Phase 2 - v1.0
  Authorised by Liam Pettigrew
  18th June 2021

  The user is asked if they wish to either view the education documents, or continue to the quiz levels.
  """
  print("How do you wish to continue?")
  print(" - To view the Te Reo Maaori education documents, please type: Documents")
  print(" - To view the levels of the quiz, please type: Quiz")
  cont2 = str(input())
  if cont2 == "Documents" or cont2 == "documents":
    print("All documents containing the Te Reo Maaori information correlating to the quiz levels:")
    print("Document 1 - ") # Document title goes here
    print("Document 2 - ") # Document title goes here
    print("Document 3 - ") # Document title goes here
    print("Document 4 - ") # Document title goes here
    print("Document 5 - ") # Document title goes here
    print("Document 6 - ") # Document title goes here
  elif cont2 == "Quiz" or cont2 == "quiz":
    print("All quiz levels:")
    print("Level 1 - ") # Level title goes here (the same as the document title)
    print("Level 2 - ") # Level title goes here (the same as the document title)
    print("Level 3 - ") # Level title goes here (the same as the document title)
    print("Level 4 - ") # Level title goes here (the same as the document title)
    print("Level 5 - ") # Level title goes here (the same as the document title)
    print("Level 6 - ") # Level title goes here (the same as the document title)
    print()
    print(" - To play the level of your choice, please type: [Number]...")
  elif cont2 != "Documents" or cont2 != "documents" or cont2 != "quiz" or cont != "Quiz":
    print("Sorry " + cont2 + " is not a valid answer. Please try again... ")
    print()
    main()

"""
Starting Welcome - v1.0
Authorised by Liam Pettigrew
17th June 2021

This is the start of the program, where the user is asked if they want to view the instructions.
"""
intro = False
while not intro:
  print("Welcome to the Te Reo Maaori Python Education Wizard!")
  print(" - For instructions, please type: Instructions... ")
  print(" - To continue the program, please type: Continue... ")
  cont = str(input())
  if cont == "Instructions" or cont == "instructions":
    print("...Instructions go here...")
  elif cont == "Continue" or cont == "continue":
    intro = True
    main()
  elif cont != "instructions" and cont != "Instructions" and cont != "continue" and cont != "Continue":
    print("Sorry " + str(cont()) + " is not a valid answer. Please try again... ")
    print()