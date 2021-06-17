
def main():
  # Code will continue here
  print("test")

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