import sys
import time

# (Commit 10) The entire code has been put under a "try" command so that a ValueError checker can be
# added to make the program more stable when a ValueError occurs.
try:

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
      # (Commit 10) Most of the "docend" function was removed as it was unnecesary. It now loops back
      # to main after the document has been completed, so the user has the option to go to the quiz levels
      # after reading the document(s).
      main()
  
    """
    Phase 2 - v2.0
    Authorised by Liam Pettigrew
    18th June 2021
  
    The user is asked if they wish to either view the education documents, or continue to the quiz levels.
    """
    print("How do you wish to continue?")
    time.sleep(1)
    print(" - To view the Te Reo Maaori education documents, please type: Documents")
    print(" - To view the levels of the quiz, please type: Quiz")
    cont2 = str(input()).lower()
    if cont2 == "Documents" or cont2 == "documents":
      # (Commit 6) a proper function has been added for the documents
      def docs():
        print()
        print("All documents containing the Te Reo Maaori information correlating to the quiz levels:")
        # (Commit 4) Document names have been put in.
        print("Document 1 - Maori Greetings + Farewells")
        print("Document 2 - Maori Objects")
        print("Document 3 - Maori Places/Geography")
        print("Document 4 - Maori Proverbs")
        print("Document 5 - Maori Sentences - Commands")
        print("Document 6 - Maori Sentences - Questions")
        print()
        print("Which document do you wish to view?")
        time.sleep(1)
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
      # (Commit 8) the multiple choices for all levels have been added, however it still does not function.
      def quiz():
        print("All quiz levels:")
        print("Level 1 - Maori Greetings + Farewells")
        print("Level 2 - Maori Objects")
        print("Level 3 - Maori Places/Geography")
        print("Level 4 - Maori Proverbs")
        print("Level 5 - Maori Sentences - Commands")
        print("Level 6 - Maori Sentences - Questions")
        print()
        time.sleep(1)
        print(" - To play the level of your choice, please type: [Number]...")
        quizlevel = int(input())
  
        # (COMMIT 7) All questions for the quiz function are listed here, including their answers.
        # The questions and answers have been found from reliable sources (the same sources the
        # information from the documents was gathered from).
  
        """
        Phase Six - v2.0
        Authorised by Liam Pettigrew

        Each question has four multiple-choice answers, one of which is correct.
        The program will wait for you to input your answer, and once you have done so,
        it will mark it as either correct or incorrect. The program will then
        continue on to the next question.
        """

        """
        Phase Seven - v1.0
        Authorised by Liam Pettigrew
        27th August 2021

        After completing a quiz, the program shows a list of correct answers for those that were incorrect.
        The user can also choose whether they would like to read an information document or play another
        quiz once the quiz has been completed.
        """
        # (COMMIT 9) The answer-checking functions have been added for all 7 questions of all 6 levels.
        if quizlevel == 1:
          Quiz1Correct = 0
          Quiz1Incorrect = 0
          print("Maori Greetings + Farewells quiz has begun.")
          print()
          q1q1play = False
          while not q1q1play:
            print("------------------------------------------")
            print()
            print("QUESTION 1")
            print("How do you say 'Hello' is Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            # (Commit 10) time.sleeps have been added to improve the program's aesthetics.
            time.sleep(0.2)
            print(" - A) Morena")
            time.sleep(0.2)
            print(" - B) Tino Pai")
            time.sleep(0.2)
            print(" - C) Kia Ora")
            time.sleep(0.2)
            print(" - D) Haere rā")
            time.sleep(0.2)
            print()
            # Kia Ora
            q1q1 = input("Enter: ")
            if q1q1 == "C" or q1q1 == "c":
              Quiz1Correct += 1
              # (Commit 10) Each question now has its own variable that will know if the
              # inputted answer is correct or incorrect.
              q1q1answer = 1
              q1q1play = True
            elif q1q1 == "A" or q1q1 == "a" or q1q1 == "B" or q1q1 == "b" or q1q1 == "D" or q1q1 == "d":
              Quiz1Incorrect += 1
              q1q1answer = 2
              q1q1play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q1q1play = False
            print()
            print("------------------------------------------")
          q1q2play = False
          while not q1q2play:
            print()
            print("QUESTION 2")
            print("How do you formally say 'Hello' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Ka kite anō")
            time.sleep(0.2)
            print(" - B) Tēnā koe")
            time.sleep(0.2)
            print(" - C) kia ora koutou")
            time.sleep(0.2)
            print(" - D) Morena")
            time.sleep(0.2)
            # Tēnā koe
            q1q2 = input("Enter: ")
            if q1q2 == "b" or q1q2 == "B":
              Quiz1Correct += 1
              q1q2answer = 1
              q1q2play = True
            elif q1q2 == "A" or q1q2 == "a" or q1q2 == "c" or q1q2 == "C" or q1q2 == "D" or q1q2 == "d":
              Quiz1Incorrect += 1
              q1q2answer = 2
              q1q2play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q1q2play = False
            print()
            print("------------------------------------------")
          q1q3play = False
          while not q1q3play:
            print("QUESTION 3")
            print("How do you say 'Hello' to three or more people in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Nau mai, haere mai")
            time.sleep(0.2)
            print(" - B) Haere rā")
            time.sleep(0.2)
            print(" - C) Tēnā koe")
            time.sleep(0.2)
            print(" - D) Tēnā koutou")
            time.sleep(0.2)
            # Tēnā koutou
            q1q3 = input("Enter: ")
            if q1q3 == "d" or q1q3 == "D":
              Quiz1Correct += 1
              q1q3answer = 1
              q1q3play = True
            elif q1q3 == "A" or q1q3 == "a" or q1q3 == "B" or q1q3 == "b" or q1q3 == "c" or q1q3 == "C":
              Quiz1Incorrect += 1
              q1q3answer = 2
              q1q3play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q1q3play = False
            print()
            print("------------------------------------------")
          q1q4play = False
          while not q1q4play:
            print("QUESTION 4")
            print("How would you ask 'How is it going' to someone in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Kei te pai")
            time.sleep(0.2)
            print(" - B) Kei te pēhea koe?")
            time.sleep(0.2)
            print(" - C) Morena")
            time.sleep(0.2)
            print(" - D) Tēnā koutou")
            time.sleep(0.2)
            # Kei te pēhea koe?
            q1q4 = input("Enter: ")
            if q1q4 == "b" or q1q4 == "B":
              Quiz1Correct += 1
              q1q4answer = 1
              q1q4play = True
            elif q1q4 == "A" or q1q4 == "a" or q1q4 == "c" or q1q4 == "C" or q1q4 == "D" or q1q4 == "d":
              Quiz1Incorrect += 1
              q1q4answer = 2
              q1q4play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q1q4play = False
            print()
            print("------------------------------------------")
          q1q5play = False
          while not q1q5play:
            print("QUESTION 5")
            print("How would you respond to someone by saying 'Really good' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Tino pai")
            time.sleep(0.2)
            print(" - B) Tēnā koutou")
            time.sleep(0.2)
            print(" - C) Kia ora kōrua")
            time.sleep(0.2)
            print(" - D) Kei te pai")
            time.sleep(0.2)
            # Tino pai
            q1q5 = input("Enter: ")
            if q1q5 == "a" or q1q5 == "A":
              Quiz1Correct += 1
              q1q5answer = 1
              q1q5play = True
            elif q1q5 == "C" or q1q5 == "c" or q1q5 == "B" or q1q5 == "b" or q1q5 == "D" or q1q5 == "d":
              Quiz1Incorrect += 1
              q1q5answer = 2
              q1q5play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q1q5play = False
            print()
            print("------------------------------------------")
          q1q6play = False
          while not q1q6play:
            print("QUESTION 6")
            print("How do you welcome someone in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Kia ora")
            time.sleep(0.2)
            print(" - B) Kei te pai")
            time.sleep(0.2)
            print(" - C) Nau mai, haere mai")
            time.sleep(0.2)
            print(" - D) Ka kite anō")
            time.sleep(0.2)
            # Nau mai, haere mai
            q1q6 = input("Enter: ")
            if q1q6 == "C" or q1q6 == "c":
              Quiz1Correct += 1
              q1q6answer = 1
              q1q6play = True
            elif q1q6 == "A" or q1q6 == "a" or q1q6 == "B" or q1q6 == "b" or q1q6 == "D" or q1q6 == "d":
              Quiz1Incorrect += 1
              q1q6answer = 2
              q1q6play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q1q6play = False
            print()
            print("------------------------------------------")
          q1q7play = False
          while not q1q7play:
            print("QUESTION 7")
            print("How do you say 'Goodbye' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Haere rā")
            time.sleep(0.2)
            print(" - B) Tēnā koe")
            time.sleep(0.2)
            print(" - C) Morena")
            time.sleep(0.2)
            print(" - D) Tino pai")
            time.sleep(0.2)
            # Haere rā
            q1q7 = input("Enter: ")
            if q1q7 == "a" or q1q7 == "A":
              Quiz1Correct += 1
              q1q7answer = 1
              q1q7play = True
            elif q1q7 == "C" or q1q7 == "c" or q1q7 == "B" or q1q7 == "b" or q1q7 == "D" or q1q7 == "d":
              Quiz1Incorrect += 1
              q1q7answer = 2
              q1q7play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q1q7play = False
            print()
            print("------------------------------------------")
          print("You got {}/7 questions correct.".format(Quiz1Correct))
          print()

          # (Commit 10) The program will now show which answers were correct and which
          # were incorrect (with correct answers) once the quiz has concluded.
  
          if q1q1answer == 1:
            print("Question 1: Correct")
          if q1q1answer == 2:
            print("Question 1: Incorrect (Correct answer: Kia Ora)")
          if q1q2answer == 1:
            print("Question 2: Correct")
          if q1q2answer == 2:
            print("Question 2: Incorrect (Correct answer: Tēnā koe)")
          if q1q3answer == 1:
            print("Question 3: Correct")
          if q1q3answer == 2:
            print("Question 3: Incorrect (Correct answer: Tēnā koutou)")
          if q1q4answer == 1:
            print("Question 4: Correct")
          if q1q4answer == 2:
            print("Question 4: Incorrect (Correct answer: Kei te pēhea koe?)")
          if q1q5answer == 1:
            print("Question 5: Correct")
          if q1q5answer == 2:
            print("Question 5: Incorrect (Correct answer: Tino pai)")
          if q1q6answer == 1:
            print("Question 6: Correct")
          if q1q6answer == 2:
            print("Question 6: Incorrect (Correct answer: Nau mai, haere mai)")
          if q1q7answer == 1:
            print("Question 7: Correct")
          if q1q7answer == 2:
            print("Question 7: Incorrect (Correct answer: Haere rā)")
          # (Commit 10) The user is then brought back to main()
          print()
          print("You have concluded Quiz 1.")
          main()
  
        elif quizlevel == 2:
          Quiz2Correct = 0
          Quiz2Incorrect = 0
          print("Maori Objects quiz has begun.")
          print()
          q2q1play = False
          while not q2q1play:
            print("QUESTION 1")
            print("What do you call a 'Pen' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) pene rākau")
            time.sleep(0.2)
            print(" - B) peita")
            time.sleep(0.2)
            print(" - C) mea")
            time.sleep(0.2)
            print(" - D) pene")
            time.sleep(0.2)
            # pene
            q2q1 = input("Enter: ")
            if q2q1 == "d" or q2q1 == "D":
              Quiz2Correct += 1
              q2q1answer = 1
              q2q1play = True
            elif q2q1 == "A" or q2q1 == "a" or q2q1 == "B" or q2q1 == "b" or q2q1 == "c" or q2q1 == "C":
              Quiz2Incorrect += 1
              q2q1answer = 2
              q2q1play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q2q1play = False
            print()
            print("------------------------------------------")
          q2q2play = False
          while not q2q2play:
            print("QUESTION 2")
            print("What do you call a 'Pencil' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) pikitia")
            time.sleep(0.2)
            print(" - B) pēke")
            time.sleep(0.2)
            print(" - C) pene rākau")
            time.sleep(0.2)
            print(" - D) papamā")
            time.sleep(0.2)
            # pene rākau
            q2q2 = input("Enter: ")
            if q2q2 == "c" or q2q2 == "C":
              Quiz2Correct += 1
              q2q2answer = 1
              q2q2play = True
            elif q2q2 == "a" or q2q2 == "A" or q2q2 == "B" or q2q2 == "b" or q2q2 == "D" or q2q2 == "d":
              Quiz2Incorrect += 1
              q2q2answer = 2
              q2q2play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q2q2play = False
            print()
            print("------------------------------------------")
          q2q3play = False
          while not q2q3play:
            print("QUESTION 3")
            print("What do you call 'Paper' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) pepa")
            time.sleep(0.2)
            print(" - B) tēpu")
            time.sleep(0.2)
            print(" - C) kāpata")
            time.sleep(0.2)
            print(" - D) makatiti")
            time.sleep(0.2)
            # pepa
            q2q3 = input("Enter: ")
            if q2q3 == "a" or q2q3 == "A":
              Quiz2Correct += 1
              q2q3answer = 1
              q2q3play = True
            elif q2q3 == "b" or q2q3 == "B" or q2q3 == "c" or q2q3 == "C" or q2q3 == "D" or q2q3 == "d":
              Quiz2Incorrect += 1
              q2q3answer = 2
              q2q3play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q2q3play = False
            print()
            print("------------------------------------------")
          q2q4play = False
          while not q2q4play:
            print("QUESTION 4")
            print("What do you call a 'Book' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) peita")
            time.sleep(0.2)
            print(" - B) pukapuka")
            time.sleep(0.2)
            print(" - C) pikitia")
            time.sleep(0.2)
            print(" - D) tūru")
            time.sleep(0.2)
            # pukapuka
            q2q4 = input("Enter: ")
            if q2q4 == "b" or q2q4 == "B":
              Quiz2Correct += 1
              q2q4answer = 1
              q2q4play = True
            elif q2q4 == "a" or q2q4 == "A" or q2q4 == "C" or q2q4 == "c" or q2q4 == "D" or q2q4 == "d":
              Quiz2Incorrect += 1
              q2q4answer = 2
              q2q4play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q2q4play = False
            print()
            print("------------------------------------------")
          q2q5play = False
          while not q2q5play:
            print("QUESTION 5")
            print("What do you call a 'Window' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) whāriki")
            time.sleep(0.2)
            print(" - B) kura")
            time.sleep(0.2)
            print(" - C) raiti")
            time.sleep(0.2)
            print(" - D) matapihi")
            time.sleep(0.2)
            # matapihi
            q2q5 = input("Enter: ")
            if q2q5 == "d" or q2q5 == "D":
              Quiz2Correct += 1
              q2q5answer = 1
              q2q5play = True
            elif q2q5 == "a" or q2q5 == "A" or q2q5 == "B" or q2q5 == "b" or q2q5 == "c" or q2q5 == "C":
              Quiz2Incorrect += 1
              q2q5answer = 2
              q2q5play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q2q5play = False
            print()
            print("------------------------------------------")
          q2q6play = False
          while not q2q6play:
            print("QUESTION 6")
            print("What do you call a 'Door' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) pikitia")
            time.sleep(0.2)
            print(" - B) kūaha")
            time.sleep(0.2)
            print(" - C) pēke")
            time.sleep(0.2)
            print(" - D) papatuhituhi")
            time.sleep(0.2)
            # kūaha
            q2q6 = input("Enter: ")
            if q2q6 == "b" or q2q6 == "B":
              Quiz2Correct += 1
              q2q6answer = 1
              q2q6play = True
            elif q2q6 == "a" or q2q6 == "A" or q2q6 == "c" or q2q6 == "C" or q2q6 == "D" or q2q6 == "d":
              Quiz2Incorrect += 1
              q2q6answer = 2
              q2q6play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q2q6play = False
            print()
            print("------------------------------------------")
          q2q7play = False
          while not q2q7play:
            print("QUESTION 7")
            print("What do you call a 'Chair' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) tūru")
            time.sleep(0.2)
            print(" - B) pepa")
            time.sleep(0.2)
            print(" - C) pēke")
            time.sleep(0.2)
            print(" - D) kutikuti")
            time.sleep(0.2)
            # tūru
            q2q7 = input("Enter: ")
            if q2q7 == "a" or q2q7 == "A":
              Quiz2Correct += 1
              q2q7answer = 1
              q2q7play = True
            elif q2q7 == "c" or q2q7 == "C" or q2q7 == "B" or q2q7 == "b" or q2q7 == "D" or q2q7 == "d":
              Quiz2Incorrect += 1
              q2q7answer = 2
              q2q7play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q2q7play = False
            print()
            print("------------------------------------------")
          print("You got {}/7 questions correct.".format(Quiz2Correct))
          print()

          # (Commit 10) The program will now show which answers were correct and which
          # were incorrect (with correct answers) once the quiz has concluded.
          
          if q2q1answer == 1:
            print("Question 1: Correct")
          if q2q1answer == 2:
            print("Question 1: Incorrect (Correct answer: pene)")
          if q2q2answer == 1:
            print("Question 2: Correct")
          if q2q2answer == 2:
            print("Question 2: Incorrect (Correct answer: pene rākau)")
          if q2q3answer == 1:
            print("Question 3: Correct")
          if q2q3answer == 2:
            print("Question 3: Incorrect (Correct answer: Tēnā koutou)")
          if q2q4answer == 1:
            print("Question 4: Correct")
          if q2q4answer == 2:
            print("Question 4: Incorrect (Correct answer: pepa)")
          if q2q5answer == 1:
            print("Question 5: Correct")
          if q2q5answer == 2:
            print("Question 5: Incorrect (Correct answer: matapihi)")
          if q2q6answer == 1:
            print("Question 6: Correct")
          if q2q6answer == 2:
            print("Question 6: Incorrect (Correct answer: kūaha)")
          if q2q7answer == 1:
            print("Question 7: Correct")
          if q2q7answer == 2:
            print("Question 7: Incorrect (Correct answer: tūru)")
          print()
          print("You have concluded Quiz 2.")
          main()
  
        elif quizlevel == 3:
          Quiz3Correct = 0
          Quiz3Incorrect = 0
          print("Maori Places/Geography quiz has begun.")
          print()
          q3q1play = False
          while not q3q1play:
            print("QUESTION 1")
            print("What does 'Maunga' mean in English? - E.g. Mount Maunganui")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) stream")
            time.sleep(0.2)
            print(" - B) hill")
            time.sleep(0.2)
            print(" - C) island")
            time.sleep(0.2)
            print(" - D) mountain")
            time.sleep(0.2)
            # Mountain
            q3q1 = input("Enter: ")
            if q3q1 == "d" or q3q1 == "D":
              Quiz3Correct += 1
              q3q1answer = 1
              q3q1play = True
            elif q3q1 == "a" or q3q1 == "A" or q3q1 == "B" or q3q1 == "b" or q3q1 == "c" or q3q1 == "C":
              Quiz3Incorrect += 1
              q3q1answer = 2
              q3q1play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q3q1play = False
            print()
            print("------------------------------------------")
          q3q2play = False
          while not q3q2play:
            print("QUESTION 2")
            print("What does 'Roto' mean in English? - E.g. Rotorua")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) bay")
            time.sleep(0.2)
            print(" - B) lake")
            time.sleep(0.2)
            print(" - C) valley")
            time.sleep(0.2)
            print(" - D) path")
            time.sleep(0.2)
            # Lake
            q3q2 = input("Enter: ")
            if q3q2 == "b" or q3q2 == "B":
              Quiz3Correct += 1
              q3q2answer = 1
              q3q2play = True
            elif q3q2 == "a" or q3q2 == "A" or q3q2 == "D" or q3q2 == "d" or q3q2 == "c" or q3q2 == "C":
              Quiz3Incorrect += 1
              q3q2answer = 2
              q3q2play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q3q2play = False
            print()
            print("------------------------------------------")
          q3q3play = False
          while not q3q3play:
            print("QUESTION 3")
            print("What does 'Awa' mean in English? - E.g. Te Awa")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) river")
            time.sleep(0.2)
            print(" - B) hill")
            time.sleep(0.2)
            print(" - C) level area")
            time.sleep(0.2)
            print(" - D) bay")
            time.sleep(0.2)
            # River / Valley
            q3q3 = input("Enter: ")
            if q3q3 == "a" or q3q3 == "A":
              Quiz3Correct += 1
              q3q3answer = 1
              q3q3play = True
            elif q3q3 == "d" or q3q3 == "D" or q3q3 == "B" or q3q3 == "b" or q3q3 == "c" or q3q3 == "C":
              Quiz3Incorrect += 1
              q3q3answer = 2
              q3q3play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q3q3play = False
            print()
            print("------------------------------------------")
          q3q4play = False
          while not q3q4play:
            print("QUESTION 4")
            print("What does 'Whanga' mean in English? - E.g. Whanganui")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) mountain")
            time.sleep(0.2)
            print(" - B) bay")
            time.sleep(0.2)
            print(" - C) island")
            time.sleep(0.2)
            print(" - D) lake")
            time.sleep(0.2)
            # Bay
            q3q4 = input("Enter: ")
            if q3q4 == "b" or q3q4 == "B":
              Quiz3Correct += 1
              q3q4answer = 1
              q3q4play = True
            elif q3q4 == "a" or q3q4 == "A" or q3q4 == "d" or q3q4 == "D" or q3q4 == "c" or q3q4 == "C":
              Quiz3Incorrect += 1
              q3q4answer = 2
              q3q4play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q3q4play = False
            print()
            print("------------------------------------------")
          q3q5play = False
          while not q3q5play:
            print("QUESTION 5")
            print("What do you call a 'Hill' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Papa")
            time.sleep(0.2)
            print(" - B) Manga")
            time.sleep(0.2)
            print(" - C) Motu")
            time.sleep(0.2)
            print(" - D) Puke")
            time.sleep(0.2)
            # Puke
            q3q5 = input("Enter: ")
            if q3q5 == "d" or q3q5 == "D":
              Quiz3Correct += 1
              q3q5answer = 1
              q3q5play = True
            elif q3q5 == "a" or q3q5 == "A" or q3q5 == "B" or q3q5 == "b" or q3q5 == "c" or q3q5 == "C":
              Quiz3Incorrect += 1
              q3q5answer = 2
              q3q5play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q3q5play = False
            print()
            print("------------------------------------------")
          q3q6play = False
          while not q3q6play:
            print("QUESTION 6")
            print("What do you call the 'Sea' in Te Reo Maori")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Moana")
            time.sleep(0.2)
            print(" - B) Ara")
            time.sleep(0.2)
            print(" - C) Puna")
            time.sleep(0.2)
            print(" - D) Whanga")
            time.sleep(0.2)
            # Moana
            q3q6 = input("Enter: ")
            if q3q6 == "a" or q3q6 == "a":
              Quiz3Correct += 1
              q3q6answer = 1
              q3q6play = True
            elif q3q6 == "d" or q3q6 == "D" or q3q6 == "B" or q3q6 == "b" or q3q6 == "c" or q3q6 == "C":
              Quiz3Incorrect += 1
              q3q6answer = 2
              q3q6play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q3q6play = False
            print()
            print("------------------------------------------")
          q3q7play = False
          while not q3q7play:
            print("QUESTION 7")
            print("What do you call an 'Island' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Wai")
            time.sleep(0.2)
            print(" - B) Motu")
            time.sleep(0.2)
            print(" - C) Whanga")
            time.sleep(0.2)
            print(" - D) Maunga")
            time.sleep(0.2)
            # Motu
            q3q7 = input("Enter: ")
            if q3q7 == "b" or q3q7 == "B":
              Quiz3Correct += 1
              q3q7answer = 1
              q3q7play = True
            elif q3q7 == "a" or q3q7 == "A" or q3q7 == "d" or q3q7 == "D" or q3q7 == "c" or q3q7 == "C":
              Quiz3Incorrect += 1
              q3q7answer = 2
              q3q7play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q3q7play = False
            print()
            print("------------------------------------------")
          print("You got {}/7 questions correct.".format(Quiz3Correct))
          print()

          # (Commit 10) The program will now show which answers were correct and which
          # were incorrect (with correct answers) once the quiz has concluded.
  
          if q3q1answer == 1:
            print("Question 1: Correct")
          if q3q1answer == 2:
            print("Question 1: Incorrect (Correct answer: Mountain)")
          if q3q2answer == 1:
            print("Question 2: Correct")
          if q3q2answer == 2:
            print("Question 2: Incorrect (Correct answer: Lake)")
          if q3q3answer == 1:
            print("Question 3: Correct")
          if q3q3answer == 2:
            print("Question 3: Incorrect (Correct answer: River / Valley)")
          if q3q4answer == 1:
            print("Question 4: Correct")
          if q3q4answer == 2:
            print("Question 4: Incorrect (Correct answer: Bay)")
          if q3q5answer == 1:
            print("Question 5: Correct")
          if q3q5answer == 2:
            print("Question 5: Incorrect (Correct answer: Puke)")
          if q3q6answer == 1:
            print("Question 6: Correct")
          if q3q6answer == 2:
            print("Question 6: Incorrect (Correct answer: Moana)")
          if q3q7answer == 1:
            print("Question 7: Correct")
          if q3q7answer == 2:
            print("Question 7: Incorrect (Correct answer: Motu)")
          print()
          print("You have concluded Quiz 3.")
          main()
          
        elif quizlevel == 4:
          Quiz4Correct = 0
          Quiz4Incorrect = 0
          print("Maori Proverbs quiz has begun.")
          print()
          q4q1play = False
          while not q4q1play:
            print("QUESTION 1")
            print("How do you say 'Be a leader not a follower' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) E noho e, kia raungāwari")
            time.sleep(0.2)
            print(" - B) He rā ki tua")
            time.sleep(0.2)
            print(" - C) Haere taka mua, taka muri; kaua e whai")
            time.sleep(0.2)
            print(" - D) He taonga nui te tūpato")
            time.sleep(0.2)
            # Haere taka mua, taka muri; kaua e whai
            q4q1 = input("Enter: ")
            if q4q1 == "c" or q4q1 == "C":
              Quiz4Correct += 1
              q4q1answer = 1
              q4q1play = True
            elif q4q1 == "a" or q4q1 == "A" or q4q1 == "d" or q4q1 == "D" or q4q1 == "b" or q4q1 == "B":
              Quiz4Incorrect += 1
              q4q1answer = 2
              q4q1play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q4q1play = False
            print()
            print("------------------------------------------")
          q4q2play = False
          while not q4q2play:
            print("QUESTION 2")
            print("How do you say 'Calm after the storm' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) He maonga āwhā")
            time.sleep(0.2)
            print(" - B) I orea te tuatara ka puta ki waho")
            time.sleep(0.2)
            print(" - C) E tupu atu kūmara, e ohu e te anuhe")
            time.sleep(0.2)
            print(" - D) He taonga tonu te wareware")
            time.sleep(0.2)
            # He maonga āwhā
            q4q2 = input("Enter: ")
            if q4q2 == "a" or q4q2 == "A":
              Quiz4Correct += 1
              q4q2answer = 1
              q4q2play = True
            elif q4q2 == "c" or q4q2 == "C" or q4q2 == "d" or q4q2 == "D" or q4q2 == "b" or q4q2 == "B":
              Quiz4Incorrect += 1
              q4q2answer = 2
              q4q2play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q4q2play = False
            print()
            print("------------------------------------------")
          q4q3play = False
          while not q4q3play:
            print("QUESTION 3")
            print("How do you say 'It is the thought that counts' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) I timu noa te tai")
            time.sleep(0.2)
            print(" - B) Ahakoa he iti kete, he iti nā te aroha")
            time.sleep(0.2)
            print(" - C) He pai ake te iti i te kore")
            time.sleep(0.2)
            print(" - D) He manawa tītī")
            time.sleep(0.2)
            # Ahakoa he iti kete, he iti nā te aroha
            q4q3 = input("Enter: ")
            if q4q3 == "b" or q4q3 == "B":
              Quiz4Correct += 1
              q4q3answer = 1
              q4q3play = True
            elif q4q3 == "a" or q4q3 == "A" or q4q3 == "d" or q4q3 == "D" or q4q3 == "c" or q4q3 == "C":
              Quiz4Incorrect += 1
              q4q3answer = 2
              q4q3play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q4q3play = False
            print()
            print("------------------------------------------")
          q4q4play = False
          while not q4q4play:
            print("QUESTION 4")
            print("How do you say 'Better times are coming' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) E kore a muri e hokia")
            time.sleep(0.2)
            print(" - B) He rā ki tua")
            time.sleep(0.2)
            print(" - C) Haere taka mua, taka muri; kaua e whai")
            time.sleep(0.2)
            print(" - D) Kua hua te marama")
            time.sleep(0.2)
            # He rā ki tua
            q4q4 = input("Enter: ")
            if q4q4 == "b" or q4q4 == "B":
              Quiz4Correct += 1
              q4q4answer = 1
              q4q4play = True
            elif q4q4 == "a" or q4q4 == "A" or q4q4 == "d" or q4q4 == "D" or q4q4 == "c" or q4q4 == "C":
              Quiz4Incorrect += 1
              q4q4answer = 2
              q4q4play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q4q4play = False
            print()
            print("------------------------------------------")
          q4q5play = False
          while not q4q5play:
            print("QUESTION 5")
            print("How do you say 'What is done is done' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) He rā whatiwhati kō")
            time.sleep(0.2)
            print(" - B) Mauri tū mauri ora")
            time.sleep(0.2)
            print(" - C) He taonga tonu te wareware")
            time.sleep(0.2)
            print(" - D) E kore a muri e hokia")
            time.sleep(0.2)
            # E kore a muri e hokia
            q4q5 = input("Enter: ")
            if q4q5 == "d" or q4q5 == "D":
              Quiz4Correct += 1
              q4q5answer = 1
              q4q5play = True
            elif q4q5 == "a" or q4q5 == "A" or q4q5 == "C" or q4q5 == "c" or q4q5 == "b" or q4q5 == "B":
              Quiz4Incorrect += 1
              q4q5answer = 2
              q4q5play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q4q5play = False
            print()
            print("------------------------------------------")
          q4q6play = False
          while not q4q6play:
            print("QUESTION 6")
            print("What does 'Aroha mai, aroha atu' mean in English?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Small in size is contrasted with great in value or beauty")
            time.sleep(0.2)
            print(" - B) A day of hard work")
            time.sleep(0.2)
            print(" - C) Love received demands love returned")
            time.sleep(0.2)
            print(" - D) A little is better than none")
            time.sleep(0.2)
            # Love received demands love returned
            q4q6 = input("Enter: ")
            if q4q6 == "c" or q4q6 == "C":
              Quiz4Correct += 1
              q4q6answer = 1
              q4q6play = True
            elif q4q6 == "a" or q4q6 == "A" or q4q6 == "d" or q4q6 == "D" or q4q6 == "b" or q4q6 == "B":
              Quiz4Incorrect += 1
              q4q6answer = 2
              q4q6play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q4q6play = False
            print()
            print("------------------------------------------")
          q4q7play = False
          while not q4q7play:
            print("QUESTION 7")
            print("What does 'E kore e mimiti te aroha mōu' mean in English?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) He who does not seek will not find")
            time.sleep(0.2)
            print(" - B) Caution is highly prized")
            time.sleep(0.2)
            print(" - C) My love for you will never wane")
            time.sleep(0.2)
            print(" - D) A little is better than none")
            time.sleep(0.2)
            # My love for you will never wane
            q4q7 = input("Enter: ")
            if q4q7 == "c" or q4q7 == "C":
              Quiz4Correct += 1
              q4q7answer = 1
              q4q7play = True
            elif q4q7 == "a" or q4q7 == "A" or q4q7 == "d" or q4q7 == "D" or q4q7 == "b" or q4q7 == "B":
              Quiz4Incorrect += 1
              q4q7answer = 2
              q4q7play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q4q7play = False
            print()
            print("------------------------------------------")
          print("You got {}/7 questions correct.".format(Quiz4Correct))
          print()

          # (Commit 10) The program will now show which answers were correct and which
          # were incorrect (with correct answers) once the quiz has concluded.
  
          if q4q1answer == 1:
            print("Question 1: Correct")
          if q4q1answer == 2:
            print("Question 1: Incorrect (Correct answer: Haere taka mua, taka muri; kaua e whai)")
          if q4q2answer == 1:
            print("Question 2: Correct")
          if q4q2answer == 2:
            print("Question 2: Incorrect (Correct answer: He maonga āwhā)")
          if q4q3answer == 1:
            print("Question 3: Correct")
          if q4q3answer == 2:
            print("Question 3: Incorrect (Correct answer: Ahakoa he iti kete, he iti nā te aroha)")
          if q4q4answer == 1:
            print("Question 4: Correct")
          if q4q4answer == 2:
            print("Question 4: Incorrect (Correct answer: He rā ki tua)")
          if q4q5answer == 1:
            print("Question 5: Correct")
          if q4q5answer == 2:
            print("Question 5: Incorrect (Correct answer: E kore a muri e hokia)")
          if q4q6answer == 1:
            print("Question 6: Correct")
          if q4q6answer == 2:
            print("Question 6: Incorrect (Correct answer: Love received demands love returned)")
          if q4q7answer == 1:
            print("Question 7: Correct")
          if q4q7answer == 2:
            print("Question 7: Incorrect (Correct answer: My love for you will never wane)")
          print()
          print("You have concluded Quiz 4.")
          main()
  
        elif quizlevel == 5:
          Quiz5Correct = 0
          Quiz5Incorrect = 0
          print("Maori Sentences - Commands quiz has begun.")
          print()
          q5q1play = False
          while not q5q1play:
            print("QUESTION 1")
            print("How do you tell someone to 'Stand' in Teo Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) E noho")
            time.sleep(0.2)
            print(" - B) Patua te pōro")
            time.sleep(0.2)
            print(" - C) E tū")
            time.sleep(0.2)
            print(" - D) Kia kaha")
            time.sleep(0.2)
            # E tū
            q5q1 = input("Enter: ")
            if q5q1 == "c" or q5q1 == "C":
              Quiz5Correct += 1
              q5q1answer = 1
              q5q1play = True
            elif q5q1 == "a" or q5q1 == "A" or q5q1 == "d" or q5q1 == "D" or q5q1 == "b" or q5q1 == "B":
              Quiz5Incorrect += 1
              q5q1answer = 2
              q5q1play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q5q1play = False
            print()
            print("------------------------------------------")
          q5q2play = False
          while not q5q2play:
            print("QUESTION 2")
            print("How do you tell someone to 'Sit' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) E noho")
            time.sleep(0.2)
            print(" - B) Taihoa")
            time.sleep(0.2)
            print(" - C) Haere mai")
            time.sleep(0.2)
            print(" - D) E tū")
            time.sleep(0.2)
            # E noho
            q5q2 = input("Enter: ")
            if q5q2 == "a" or q5q2 == "A":
              Quiz5Correct += 1
              q5q2answer = 1
              q5q2play = True
            elif q5q2 == "c" or q5q2 == "C" or q5q2 == "d" or q5q2 == "D" or q5q2 == "b" or q5q2 == "B":
              Quiz5Incorrect += 1
              q5q2answer = 2
              q5q2play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q5q2play = False
            print()
            print("------------------------------------------")
          q5q3play = False
          while not q5q3play:
            print("QUESTION 3")
            print("How do you tell someone 'You should go home' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Kaua e patua te kurī")
            time.sleep(0.2)
            print(" - B) Me haere koe ki te kāinga")
            time.sleep(0.2)
            print(" - C) Taihoa e tunu i ngā ika")
            time.sleep(0.2)
            print(" - D) Me whakarongo koe ki tōu whaea")
            time.sleep(0.2)
            # Me haere koe ki te kāinga
            q5q3 = input("Enter: ")
            if q5q3 == "b" or q5q3 == "B":
              Quiz5Correct += 1
              q5q3answer = 1
              q5q3play = True
            elif q5q3 == "a" or q5q3 == "A" or q5q3 == "d" or q5q3 == "D" or q5q3 == "c" or q5q3 == "C":
              Quiz5Incorrect += 1
              q5q3answer = 2
              q5q3play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q5q3play = False
            print()
            print("------------------------------------------")
          q5q4play = False
          while not q5q4play:
            print("QUESTION 4")
            print("How do you tell someone 'You should wash the clothes' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Kia tūpato te tapahi")
            time.sleep(0.2)
            print(" - B) Me horoi ngā kākahu")
            time.sleep(0.2)
            print(" - C) Ka waiata tātou")
            time.sleep(0.2)
            print(" - D) Taihoa e tunu i ngā ika!")
            time.sleep(0.2)
            # Me horoi ngā kākahu
            q5q4 = input("Enter: ")
            if q5q4 == "b" or q5q4 == "B":
              Quiz5Correct += 1
              q5q4answer = 1
              q5q4play = True
            elif q5q4 == "a" or q5q4 == "A" or q5q4 == "d" or q5q4 == "D" or q5q4 == "c" or q5q4 == "C":
              Quiz5Incorrect += 1
              q5q4answer = 2
              q5q4play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q5q4play = False
            print()
            print("------------------------------------------")
          q5q5play = False
          while not q5q5play:
            print("QUESTION 5")
            print("How do you demand someone to 'Wash the clothes' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Horoia ngā kākahu")
            time.sleep(0.2)
            print(" - B) Whakakoia te māripi")
            time.sleep(0.2)
            print(" - C) Patua te pōro")
            time.sleep(0.2)
            print(" - D) Me haere koe ki te kāinga")
            time.sleep(0.2)
            # Horoia ngā kākahu
            q5q5 = input("Enter: ")
            if q5q5 == "a" or q5q5 == "A":
              Quiz5Correct += 1
              q5q5answer = 1
              q5q5play = True
            elif q5q5 == "c" or q5q5 == "C" or q5q5 == "d" or q5q5 == "D" or q5q5 == "b" or q5q5 == "B":
              Quiz5Incorrect += 1
              q5q5answer = 2
              q5q5play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q5q5play = False
            print()
            print("------------------------------------------")
          q5q6play = False
          while not q5q6play:
            print("QUESTION 6")
            print("How do you tell someone 'Let's go to the shop' in Te Reo Maori (to two or more people)?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Ka waiata tātou")
            time.sleep(0.2)
            print(" - B) Ka haere tāua ki te toa")
            time.sleep(0.2)
            print(" - C) Taihoa e oma")
            time.sleep(0.2)
            print(" - D) Kāti te tangi")
            time.sleep(0.2)
            # Ka haere tāua ki te toa
            q5q6 = input("Enter: ")
            if q5q6 == "b" or q5q6 == "B":
              Quiz5Correct += 1
              q5q6answer = 1
              q5q6play = True
            elif q5q6 == "a" or q5q6 == "A" or q5q6 == "d" or q5q6 == "D" or q5q6 == "c" or q5q6 == "C":
              Quiz5Incorrect += 1
              q5q6answer = 2
              q5q6play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q5q6play = False
            print()
            print("------------------------------------------")
          q5q7play = False
          while not q5q7play:
            print("QUESTION 7")
            print("What does 'Haere mai' mean in English?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Be strong")
            time.sleep(0.2)
            print(" - B) Wait")
            time.sleep(0.2)
            print(" - C) Come here")
            time.sleep(0.2)
            print(" - D) Be careful")
            time.sleep(0.2)
            # Come here
            q5q7 = input("Enter: ")
            if q5q7 == "c" or q5q7 == "C":
              Quiz5Correct += 1
              q5q7answer = 1
              q5q7play = True
            elif q5q7 == "a" or q5q7 == "A" or q5q7 == "d" or q5q7 == "D" or q5q7 == "b" or q5q7 == "B":
              Quiz5Incorrect += 1
              q5q7answer = 2
              q5q7play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q5q7play = False
            print()
            print("------------------------------------------")
            print("You got {}/7 questions correct.".format(Quiz5Correct))
            print()

            # (Commit 10) The program will now show which answers were correct and which
            # were incorrect (with correct answers) once the quiz has concluded.
  
            if q5q1answer == 1:
              print("Question 1: Correct")
            if q5q1answer == 2:
              print("Question 1: Incorrect (Correct answer: E tū)")
            if q5q2answer == 1:
              print("Question 2: Correct")
            if q5q2answer == 2:
              print("Question 2: Incorrect (Correct answer: E noho)")
            if q5q3answer == 1:
              print("Question 3: Correct")
            if q5q3answer == 2:
              print("Question 3: Incorrect (Correct answer: Me haere koe ki te kāinga)")
            if q5q4answer == 1:
              print("Question 4: Correct")
            if q5q4answer == 2:
              print("Question 4: Incorrect (Correct answer: Me horoi ngā kākahu)")
            if q5q5answer == 1:
              print("Question 5: Correct")
            if q5q5answer == 2:
              print("Question 5: Incorrect (Correct answer: Horoia ngā kākahu)")
            if q5q6answer == 1:
              print("Question 6: Correct")
            if q5q6answer == 2:
              print("Question 6: Incorrect (Correct answer: Ka haere tāua ki te toa)")
            if q5q7answer == 1:
              print("Question 7: Correct")
            if q5q7answer == 2:
              print("Question 7: Incorrect (Correct answer: Come here)")
            print()
            print("You have concluded Quiz 5.")
            main()
          
        elif quizlevel == 6:
          Quiz6Correct = 0
          Quiz6Incorrect = 0
          print("Maori Sentences - Questions quiz has begun.")
          print()
          q6q1play = False
          while not q6q1play:
            print("QUESTION 1")
            print("How do you say 'Yes' and 'No' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Aha + Wai")
            time.sleep(0.2)
            print(" - B) Hea + Kāo")
            time.sleep(0.2)
            print(" - C) Āe + Wai")
            time.sleep(0.2)
            print(" - D) Āe + Kāo")
            time.sleep(0.2)
            # Āe + Kāo
            q6q1 = input("Enter: ")
            if q6q1 == "d" or q6q1 == "D":
              Quiz6Correct += 1
              q6q1answer = 1
              q6q1play = True
            elif q6q1 == "a" or q6q1 == "A" or q6q1 == "c" or q6q1 == "C" or q6q1 == "b" or q6q1 == "B":
              Quiz6Incorrect += 1
              q6q1answer = 2
              q6q1play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q6q1play = False
            print()
            print("------------------------------------------")
          q6q2play = False
          while not q6q2play:
            print("QUESTION 2")
            print("How would you say 'The sun is shining' as a QUESTION in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Kei roto te kai i te umu?")
            time.sleep(0.2)
            print(" - B) Kei te whiti te rā?")
            time.sleep(0.2)
            print(" - C) He inu māu?")
            time.sleep(0.2)
            print(" - D) He waka tōna?")
            time.sleep(0.2)
            # Kei te whiti te rā?
            q6q2 = input("Enter: ")
            if q6q2 == "b" or q6q2 == "B":
              Quiz6Correct += 1
              q6q2answer = 1
              q6q2play = True
            elif q6q2 == "a" or q6q2 == "A" or q6q2 == "c" or q6q2 == "C" or q6q2 == "d" or q6q2 == "D":
              Quiz6Incorrect += 1
              q6q2answer = 2
              q6q2play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q6q2play = False
            print()
            print("------------------------------------------")
          q6q3play = False
          while not q6q3play:
            print("QUESTION 3")
            print("How do you say 'When did you return?' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Āhea te kēmu?")
            time.sleep(0.2)
            print(" - B) Kei hea tōku waka?")
            time.sleep(0.2)
            print(" - C) Kua hoki mai koe i hea?")
            time.sleep(0.2)
            print(" - D) Nōnahea koe i hoki mai ai?")
            time.sleep(0.2)
            # Nōnahea koe i hoki mai ai?
            q6q3 = input("Enter: ")
            if q6q3 == "d" or q6q3 == "D":
              Quiz6Correct += 1
              q6q3answer = 1
              q6q3play = True
            elif q6q3 == "a" or q6q3 == "A" or q6q3 == "c" or q6q3 == "C" or q6q3 == "b" or q6q3 == "B":
              Quiz6Incorrect += 1
              q6q3answer = 2
              q6q3play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q6q3play = False
            print()
            print("------------------------------------------")
          q6q4play = False
          while not q6q4play:
            print("QUESTION 4")
            print("How do you say 'Where are you from?' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Ka haere ia ki hea?")
            time.sleep(0.2)
            print(" - B) Kei hea koe?")
            time.sleep(0.2)
            print(" - C) Nō hea koe?")
            time.sleep(0.2)
            print(" - D) E haere mai ana rāua i hea?")
            time.sleep(0.2)
            # Nō hea koe?
            q6q4 = input("Enter: ")
            if q6q4 == "c" or q6q4 == "C":
              Quiz6Correct += 1
              q6q4answer = 1
              q6q4play = True
            elif q6q4 == "a" or q6q4 == "A" or q6q4 == "d" or q6q4 == "D" or q6q4 == "b" or q6q4 == "B":
              Quiz6Incorrect += 1
              q6q4answer = 2
              q6q4play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q6q4play = False
            print()
            print("------------------------------------------")
          q6q5play = False
          while not q6q5play:
            print("QUESTION 5")
            print("How do you say 'To where is he going?' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) Ka haere ia ki hea?")
            time.sleep(0.2)
            print(" - B) Ko tēhea te kapu pai ki a koe?")
            time.sleep(0.2)
            print(" - C) Ka haere koe ki hea?")
            time.sleep(0.2)
            print(" - D) Kei te pēhea koe?")
            time.sleep(0.2)
            # Ka haere ia ki hea?
            q6q5 = input("Enter: ")
            if q6q5 == "d" or q6q5 == "D":
              Quiz6Correct += 1
              q6q5answer = 1
              q6q5play = True
            elif q6q5 == "a" or q6q5 == "A" or q6q5 == "c" or q6q5 == "C" or q6q5 == "b" or q6q5 == "B":
              Quiz6Incorrect += 1
              q6q5answer = 2
              q6q5play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q6q5play = False
            print()
            print("------------------------------------------")
          q6q6play = False
          while not q6q6play:
            print("QUESTION 6")
            print("How do you say 'What's this?' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) E kimi ana ia ki te aha?")
            time.sleep(0.2)
            print(" - B) Hei aha tēnei?")
            time.sleep(0.2)
            print(" - C) Kei te aha ia?")
            time.sleep(0.2)
            print(" - D) He aha tēnei?")
            time.sleep(0.2)
            # He aha tēnei?
            q6q6 = input("Enter: ")
            if q6q6 == "d" or q6q6 == "D":
              Quiz6Correct += 1
              q6q6answer = 1
              q6q6play = True
            elif q6q6 == "a" or q6q6 == "A" or q6q6 == "c" or q6q6 == "C" or q6q6 == "b" or q6q6 == "B":
              Quiz6Incorrect += 1
              q6q6answer = 2
              q6q6play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q6q6play = False
            print()
            print("------------------------------------------")
          q6q7play = False
          while not q6q7play:
            print("QUESTION 7")
            print("How do you ask 'Who are you?' in Te Reo Maori?")
            print()
            print("Which of the following is the correct answer?")
            time.sleep(0.2)
            print(" - A) I pēhea tāu kai?")
            time.sleep(0.2)
            print(" - B) Mō wai tēnei waka?")
            time.sleep(0.2)
            print(" - C) Kei a wai ngā tīkiti?")
            time.sleep(0.2)
            print(" - D) Ko wai koe?")
            time.sleep(0.2)
            # Ko wai koe?
            q6q7 = input("Enter: ")
            if q6q7 == "d" or q6q7 == "D":
              Quiz6Correct += 1
              q6q7answer = 1
              q6q7play = True
            elif q6q7 == "a" or q6q7 == "A" or q6q7 == "c" or q6q7 == "C" or q6q7 == "b" or q6q7 == "B":
              Quiz6Incorrect += 1
              q6q7answer = 2
              q6q7play = True
            else:
              print("That is an invalid answer. Make sure you are typing the letter of chosen answer.")
              print("Please try again.")
              q6q7play = False
            print()
            print("------------------------------------------")
            print("You got {}/7 questions correct.".format(Quiz6Correct))
            print()

            # (Commit 10) The program will now show which answers were correct and which
            # were incorrect (with correct answers) once the quiz has concluded.
  
            if q6q1answer == 1:
              print("Question 1: Correct")
            if q6q1answer == 2:
              print("Question 1: Incorrect (Correct answer: Āe + Kāo)")
            if q6q2answer == 1:
              print("Question 2: Correct")
            if q6q2answer == 2:
              print("Question 2: Incorrect (Correct answer: Kei te whiti te rā?)")
            if q6q3answer == 1:
              print("Question 3: Correct")
            if q6q3answer == 2:
              print("Question 3: Incorrect (Correct answer: Nōnahea koe i hoki mai ai?)")
            if q6q4answer == 1:
              print("Question 4: Correct")
            if q6q4answer == 2:
              print("Question 4: Incorrect (Correct answer: Nō hea koe?)")
            if q6q5answer == 1:
              print("Question 5: Correct")
            if q6q5answer == 2:
              print("Question 5: Incorrect (Correct answer: Ka haere ia ki hea?)")
            if q6q6answer == 1:
              print("Question 6: Correct")
            if q6q6answer == 2:
              print("Question 6: Incorrect (Correct answer: He aha tēnei?)")
            if q6q7answer == 1:
              print("Question 7: Correct")
            if q6q7answer == 2:
              print("Question 7: Incorrect (Correct answer: Ko wai koe?)")
            print()
            print("You have concluded Quiz 6.")
            main()
            
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
    time.sleep(1)
    print(" - If so, please continue the program by typing: Yes")
    print(" - If not, please break the program by typing: No")
    instructionscontinue = str(input()).lower()
    if instructionscontinue == "yes" or instructionscontinue == "Yes":
      print("The program will now continue.")
      print()
      main()
      intro = True
    elif instructionscontinue == "No" or instructionscontinue == "no":
      sys.exit(print("The program will now self-destruct"))
    else:
      print("Sorry, " + instructionscontinue + " is not a valid answer.")
    
  """
  Starting Welcome (Phase 1) - v1.0
  Authorised by Liam Pettigrew
  17th June 2021
  
  This is the start of the program, where the user is asked if they want to view the instructions.
  """
  intro = False
  while not intro:
    print("Welcome to the Te Reo Maaori Python Education Wizard!")
    time.sleep(1)
    print(" - For instructions, please type: Instructions... ")
    print(" - To continue the program, please type: Continue... ")
    cont = str(input()).lower()
    if cont == "Instructions" or cont == "instructions":
      print("...Instructions go here...")
      print()
      ins()
      intro = True
    elif cont == "Continue" or cont == "continue":
      intro = True
      main()
    elif cont != "instructions" and cont != "Instructions" and cont != "continue" and cont != "Continue":
      print("Sorry " + cont + " is not a valid answer. Please try again... ")
      print()

# (Commit 10) A ValueError checker has been added to make the program more stable when a ValueError occurs.
except ValueError:
  print()
  print("That is an invalid answer. Please try again.")
  print()
  main()