import sys

def main():

  """
  Phase 4 - v1.0
  Authorised by Liam Pettigrew
  2nd July 2021

  The user can now loop the documents if they wish to view another documents. They can
  also view the quizzes (quiz function not complete as of commit 6).
  Different functions/definitions have also been added for the quiz and the
  documents in order to loop them.
  """
  def docend():
    print("===============================================================================================")
    print()
    print("That is the end of the document. How do you wish to continue the program?")
    print(" - To view the quizzes, please type: Quiz")
    print(" - To read another document, please type: Documents")
    print(" - To conclude the program, please type: End")
    print()
    continuechoice = str(input())
    if continuechoice == "Quiz" or continuechoice == "quiz":
      print("Placeholder")
      # Will be fixed and loop back to quiz, once quiz function is completed.
    elif continuechoice == "Documents" or continuechoice == "documents":
      print("You are now about to view the documents again.")
      print()
      docs()
    elif continuechoice == "End" or continuechoice == "end":
      sys.exit(print("The program will now self-destruct"))
    else:
      print("Sorry, " + continuechoice + " is not a valid answer.")
      docend()

  """
  Phase 2 - v2.0
  Authorised by Liam Pettigrew
  18th June 2021

  The user is asked if they wish to either view the education documents, or continue to the quiz levels.
  """
  print("How do you wish to continue?")
  print(" - To view the Te Reo Maaori education documents, please type: Documents")
  print(" - To view the levels of the quiz, please type: Quiz")
  cont2 = str(input())
  if cont2 == "Documents" or cont2 == "documents":
    # (Commit 6) a proper function has been added for the documents
    def docs():
      print("All documents containing the Te Reo Maaori information correlating to the quiz levels:")
      # (Commit 4) Document names have been put in.
      print("Document 1 - Maori Greetings + Farewells")
      print("Document 2 - Maori Objects")
      print("Document 3 - Maori Places/Geography")
      print("Document 4 - Maori Proverbs")
      print("Document 5 - Maori Sentences - Commands")
      print("Document 6 - Maori Sentences - Questions")
      print()
      print("Which level do you wish to play?")
      print(" - To view the document of your choice, please type: [Number]...")

      """
      Phase 3 - v1.0
      Authorised by Liam Pettigrew
      18th June 2021

      The user is displayed a list of 6 documents that they can view. Each document contains information
     about the Te Reo Maori language, which will correlate to the 6 quiz levels. The user is then asked
      which document they wish to view, and then it prints the information.

     The sources that the information was gathered from is in the plan document (Microsoft Word)
      """

      # (Commit 4) Documents function now responds. The information has been put in as of commit 5.
      # Note: Information on documents may be improved in a later version to better suit the quiz information.
      documentlevel = int(input())
      if documentlevel == 1:
        print("===============================================================================================")
        print()
        print("Information for Maori Greetings + Farewells:")
        print("Learning basic Māori greetings is a great place to start.")
        print()
        print()
        print("GREETINGS + RESPONSES:")
        print()
        print("Kia ora - Hello")
        print("Morena - Good morning")
        print("Tēnā koe - Hello (more formal than kia ora)")
        print("Kia ora kōrua - Hello (directed at two people)")
        print("Tēnā koutou - Greetings to you (directed at three or more people)")
        print("Kia ora tātou - Hello everyone")
        print("Nau mai, haere mai - Welcome")
        print("Kei te pēhea koe? - How is it going?")
        print(" (Kei te pai - Good)")
        print(" (Tino pai - Really good)")
        print()
        print("FAREWELLS:")
        print()
        print("Ka kite anō - See you later")
        print("Haere rā - Goodbye")
        docend()
      elif documentlevel == 2:
        print("===============================================================================================")
        print("Information for Maori Objects:")
        print()
        print()
        print("COMMON MAORI OBJECTS:")
        print()
        print("kāpata - Cupboard")
        print("karaka - Clock")
        print("kūaha - Door")
        print("kutikuti - Scissors")
        print("makatiti - Stapler")
        print("matapihi - Window")
        print("papamā - Whiteboard")
        print("papatuhituhi - Blackboard")
        print("peita - Paint")
        print("pēke - Bag")
        print("pene - Pen")
        print("pene hinu - Crayon")
        print("pene rākau - Pencil")
        print("pepa - Paper")
        print("pikitia - Picture")
        print("pukapuka - Book")
        print("raiti - Light")
        print("rapa - Rubber")
        print("rorohiko - Computer")
        print("rūri - Ruler")
        print("tēpu - table")
        print("tūru - Chair")
        docend()
      elif documentlevel == 3:
        print("===============================================================================================")
        print("Information for Maori Places/Geography:")
        print()
        print("COMMON MAORI LAND AREAS:")
        print()
        print("Ara - Path / Road")
        print("Awa - River / Valley")
        print("Maunga - Mountain")
        print("Moana - Sea / Large lake")
        print("Motu - Island")
        print("Papa - Flat, open area")
        print("Puke - Hill")
        print("Puna - Water Spring")
        print("Roto - Lake")
        print("Whanga - Bay / Stretch of water")
        docend()
      elif documentlevel == 4:
        print("===============================================================================================")
        print("Information for Maori Proverbs:")
        print()
        print("COMMON MAORI SAYINGS AND PRONOUNS:")
        print()
        print("A small thing given with love                             E iti noa ana nā te aroha")
        print("Love received demands love returned                       Aroha mai, aroha atu")
        print("Although it is small it is a treasure                     He hono tangata e kore e motu; ka pa he taura waka e motu")
        print("It is the thought that counts                             Ahakoa he iti kete, he iti nā te aroha")
        print("Goodwill towards others is a precious treasure            He taonga rongonui te aroha ki te tangata")
        print("Let us keep close together, not far apart                 Waiho i te toipoto, kaua i te toiroa")
        print("My love for you will never wane                           E kore e mimiti te aroha mōu")
        print("Words can't express how much I love you                   E kore e ea i te kupu taku aroha mōu")
        print("My love for you knows no bounds                           Ka nui taku aroha ki a koe")
        print("Calm after the storm                                      He maonga āwhā")
        print("Be a leader not a follower                                Haere taka mua, taka muri; kaua e whai")
        print("What is done is done                                      E kore a muri e hokia")
        print("Better times are coming                                   He rā ki tua")
        print("Forgetfulness is an enduring possession                   He taonga tonu te wareware")
        print("He who does not seek will not find                        Ko ia kāhore nei i rapu, tē kitea")
        docend()
      elif documentlevel == 5:
        print("===============================================================================================")
        print("Information for Maori Sentences - Commands:")
        print()
        print("MAORI COMMANDS - SIMPLE ACTIVE FORM:")
        print()
        print("Haere mai - Come here")
        print("E noho - Sit")
        print("E tū - Stand")
        print()
        print("SIMPLE PASSIVE FORM (EXAMPLES):")
        print()
        print("Patua te pōro - Hit the ball")
        print("Horoia ngā kākahu - Wash the clothes")
        print("Whakakoia te māripi - Sharpen the knife")
        print()
        print("SIMPLE PASSIVE FORMS INCLUDING 'SHOULD' (EXAMPLES):")
        print()
        print("Me haere koe ki te kāinga - You should go home")
        print("Me whakarongo koe ki tōu whaea - You should listen to your aunty")
        print("Me horoi ngā kākahu! - You should wash your clothes")
        print()
        print("SIMPLE PASSOVE FORM INCLUDING 'LETS' (EXAMPLES):")
        print()
        print("Ka haere tāua ki te toa - Let's go to the shop")
        print("Ka waiata tātou - Let's sing")
        docend()
      elif documentlevel == 6:
        print("===============================================================================================")
        print("Information for Maori Sentences - Questions:")
        print()
        print("STATEMENTS VS QUESTIONS:")
        print()
        print("Kei te whiti te rā - The sun is shining.")
        print(" > Kei te whiti te rā? - Kei te whiti te rā?")
        print()
        print("Kei roto te kai i te umu - The food is in the oven")
        print(" > Kei roto te kai i te umu? - Is the food in the oven?")
        print()
        print("He waka tōna - She has a waka")
        print(" > He waka tōna? - Does she have a waka?")
        print()
        print("He inu māu - A drink for you")
        print(" > He inu māu? - Would you like a drink?")
        print()
        print("Responses:")
        print("Āe - Yes")
        print("Kāo - No")
        print()
        print()
        print("Who - Wai:")
        print("Ko wai koe?                                                  Who are you?")
        print("Ko wai te ingoa o tērā wahine?                               What's the name of that woman?")
        print("I hoatu koe i te koha ki a wai?                              To whom did you give the koha?")
        print()
        print("What - Aha:")
        print("He aha tēnei?                                                What's this?")
        print("E kimi ana ia ki te aha?                                     What's he searching for?")
        print("Kei te aha ia?                                               What is she doing?")
        print("Hei aha tēnei?                                               For what purpose is this?")
        print()
        print("Where - Hea:")
        print("Kei hea tōku waka?                                           Where is my waka?")
        print("Ka haere ia ki hea?                                          To where is he going?")
        print("Kua hoki mai koe i hea?                                      From where have you returned?")
        print("Nō hea koe?                                                  Where are you from?")
        print()
        print("When - āhea/nōnahea:")
        print("Āhea te kēmu?                                                When's the game?")
        print("Nōnahea koe i hoki mai ai?                                   When did you return?")
        docend()
      elif documentlevel != range(1,10):
        print("Sorry, that is not a valid level.")
        print("Make sure you are typing only the number of the level.")
        docs()
    docs()
    
  elif cont2 == "Quiz" or cont2 == "quiz":
    # (Commit 6) a proper function has been added for the quiz.
    def quiz():
      print("All quiz levels:")
      print("Level 1 - ") # Level title goes here (the same as the document title)
      print("Level 2 - ") # Level title goes here (the same as the document title)
      print("Level 3 - ") # Level title goes here (the same as the document title)
      print("Level 4 - ") # Level title goes here (the same as the document title)
      print("Level 5 - ") # Level title goes here (the same as the document title)
      print("Level 6 - ") # Level title goes here (the same as the document title)
      print()
      print(" - To play the level of your choice, please type: [Number]...")
    quiz()
  elif cont2 != "Documents" or cont2 != "documents" or cont2 != "quiz" or cont != "Quiz":
    print("Sorry " + cont2 + " is not a valid answer. Please try again... ")
    print()
    main()

# (Commit 3) Version 2 of instructions function - lets you continue after reading the instructions
def ins():
  print("Have you read all of the instructions?")
  print(" - If so, please continue the program by typing: Yes")
  print(" - If not, please break the program by typing: No")
  instructionscontinue = input
  if str(instructionscontinue()) == "yes" or str(instructionscontinue()) == "Yes":
    print("The program will now continue.")
    print()
    main()
    intro = True
  elif str(instructionscontinue()) == "No" or str(instructionscontinue()) == "no":
    sys.exit(print("The program will now self-destruct"))
  else:
    print("Sorry, " + str(instructionscontinue()) + " is not a valid answer.")
  
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
    print()
    ins()
    intro = True
  elif cont == "Continue" or cont == "continue":
    intro = True
    main()
  elif cont != "instructions" and cont != "Instructions" and cont != "continue" and cont != "Continue":
    print("Sorry " + str(cont()) + " is not a valid answer. Please try again... ")
    print()