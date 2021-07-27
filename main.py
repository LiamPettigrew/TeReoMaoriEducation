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
        print("Me horoi ngā kākahu - You should wash your clothes")
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
        print(" > Kei te whiti te rā? - Is the sun shining?")
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
        print("Sorry, that is not a valid document level.")
        print("Make sure you are typing only the number of the level.")
        docs()
    docs()
    
  elif cont2 == "Quiz" or cont2 == "quiz":
    """
    Phase Five - v1.0
    Authorised by Liam Pettigrew
    6th July 2021

    This is the quiz function, where the titles for the quizzes are displayed. The user
    is also asked which level they wish to view, and it then runs the level.
    """
    # (Commit 6) a proper function has been added for the quiz.
    # (Commit 7) the answers for the questions have been commented, but they do not respond.
    def quiz():
      print("All quiz levels:")
      print("Level 1 - Maori Greetings + Farewells")
      print("Level 2 - Maori Objects")
      print("Level 3 - Maori Places/Geography")
      print("Level 4 - Maori Proverbs")
      print("Level 5 - Maori Sentences - Commands")
      print("Level 6 - Maori Sentences - Questions")
      print()
      print(" - To play the level of your choice, please type: [Number]...")
      quizlevel = int(input())
      """
      Phase Seven - v1.0
      Authorised by Liam Pettigrew
      27th July 2021

      All questions for the quiz function are listed here, including their answers.
      The questions and answers have been found from reliable sources (the same sources the
      information from the documents was gathered from).
      """
      if quizlevel == 1:
        print("Maori Greetings + Farewells quiz has begun.")
        print()
        print("QUESTION 1")
        print("How do you say 'Hello' is Te Reo Maori?")
        # Kia Ora
        print()
        print("QUESTION 2")
        print("How do you formally say 'Hello' in Te Reo Maori?")
        # Tēnā koe
        print()
        print("QUESTION 3")
        print("How do you say 'Hello' to three or more people in Te Reo Maori?")
        # Kia ora kōrua
        print()
        print("QUESTION 4")
        print("How would you ask 'How is it going' to someone in Te Reo Maori?")
        # Kei te pēhea koe?
        print()
        print("QUESTION 5")
        print("How would you respond to someone by saying 'Really good' in Te Reo Maori?")
        # Tino pai
        print()
        print("QUESTION 6")
        print("How do you welcome someone in Te Reo Maori?")
        # Nau mai, haere mai
        print()
        print("QUESTION 7")
        print("How do you say 'Goodbye' in Te Reo Maori?")
        # Haere rā
      elif quizlevel == 2:
        print("Maori Objects quiz has begun.")
        print()
        print("QUESTION 1")
        print("What do you call a 'Pen' in Te Reo Maori?")
        # pene
        print()
        print("QUESTION 2")
        print("What do you call a 'Pencil' in Te Reo Maori?")
        # pene rākau
        print()
        print("QUESTION 3")
        print("What do you call 'Paper' in Te Reo Maori?")
        # pepa
        print()
        print("QUESTION 4")
        print("What do you call a 'Book' in Te Reo Maori?")
        # pukapuka
        print()
        print("QUESTION 5")
        print("What do you call a 'Window' in Te Reo Maori?")
        # matapihi
        print()
        print("QUESTION 6")
        print("What do you call a 'Door' in Te Reo Maori?")
        # kūaha
        print()
        print("QUESTION 7")
        print("What do you call a 'Chair' in Te Reo Maori?")
        # tūru
      elif quizlevel == 3:
        print("Maori Places/Geography quiz has begun.")
        print()
        print("QUESTION 1")
        print("What does 'Maunga' mean in English? - E.g. Mount Maunganui")
        # Mountain
        print()
        print("QUESTION 2")
        print("What does 'Roto' mean in English? - E.g. Rotorua")
        # Lake
        print()
        print("QUESTION 3")
        print("What does 'Awa' mean in English? - E.g. Te Awa")
        # River / Valley
        print()
        print("QUESTION 4")
        print("What does 'Whanga' mean in English? - E.g. Whanganui")
        # Bay
        print()
        print("QUESTION 5")
        print("What do you call a 'Hill' in Te Reo Maori?")
        # Puke
        print()
        print("QUESTION 6")
        print("What do you call the 'Sea' in Te Reo Maori")
        # Moana
        print("QUESTION 7")
        print("What do you call an 'Island' in Te Reo Maori?")
        # Motu
      elif quizlevel == 4:
        print("Maori Proverbs quiz has begun.")
        print()
        print("QUESTION 1")
        print("How do you say 'Be a leader not a follower' in Te Reo Maori?")
        # Haere taka mua, taka muri; kaua e whai
        print()
        print("QUESTION 2")
        print("How do you say 'Calm after the storm' in Te Reo Maori?")
        # He maonga āwhā
        print()
        print("QUESTION 3")
        print("How do you say 'It is the thought that counts' in Te Reo Maori?")
        # Ahakoa he iti kete, he iti nā te aroha
        print()
        print("QUESTION 4")
        print("How do you say 'Better times are coming' in Te Reo Maori?")
        # He rā ki tua
        print()
        print("QUESTION 5")
        print("How do you say 'What is done is done' in Te Reo Maori?")
        # E kore a muri e hokia
        print()
        print("QUESTION 6")
        print("What does 'Aroha mai, aroha atu' mean in English?")
        # Love received demands love returned
        print()
        print("QUESTION 7")
        print("What does 'E kore e mimiti te aroha mōu' mean in English?")
        # My love for you will never wane
      elif quizlevel == 5:
        print("Maori Sentences - Commands quiz has begun.")
        print()
        print("QUESTION 1")
        print("How do you tell someone to 'Stand' in Teo Reo Maori?")
        # E tū
        print()
        print("QUESTION 2")
        print("How do you tell someone to 'Sit' in Te Reo Maori?")
        # E noho
        print()
        print("QUESTION 3")
        print("How do you tell someone 'You should go home' in Te Reo Maori?")
        # Me haere koe ki te kāinga
        print()
        print("QUESTION 4")
        print("How do you tell someone 'You should wash the clothes' in Te Reo Maori?")
        # Me horoi ngā kākahu
        print()
        print("QUESTION 5")
        print("How do you demand someone to 'Wash the clothes' in Te Reo Maori?")
        # Horoia ngā kākahu
        print()
        print("QUESTION 6")
        print("How do you tell someone 'Let's go to the shop' in Te Reo Maori?")
        # Ka haere tāua ki te toa
        print("QUESTION 7")
        print("What does 'Haere mai' mean in English?")
        # Come here
      elif quizlevel == 6:
        print("Maori Sentences - Questions quiz has begun.")
        print()
        print("QUESTION 1")
        print("How do you say 'Yes' and 'No' in Te Reo Maori?")
        # Āe + Kāo
        print()
        print("QUESTION 2")
        print("How would you say 'The sun is shining' as a question in Te Reo Maori?")
        # Kei te whiti te rā?
        print()
        print("QUESTION 3")
        print("How do you say 'When did you return?' in Te Reo Maori?")
        # Nōnahea koe i hoki mai ai?
        print()
        print("QUESTION 4")
        print("How do you say 'Where are you from?' in Te Reo Maori?")
        # Nō hea koe?
        print()
        print("QUESTION 5")
        print("How do you say 'To where is he going?' in Te Reo Maori?")
        # Ka haere ia ki hea?
        print()
        print("QUESTION 6")
        print("How do you say 'What's this?' in Te Reo Maori?")
        # He aha tēnei?
        print()
        print("QUESTION 7")
        print("How do you ask 'Who are you?' in Te Reo Maori?")
        # Ko wai koe?
      elif quizlevel != range(1,10):
        print("Sorry, that is not a quiz valid level.")
        print("Make sure you are typing only the number of the level.")
        quiz()
      
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
Starting Welcome (Phase 1) - v1.0
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