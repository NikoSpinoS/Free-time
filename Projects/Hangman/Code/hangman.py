import time
import turtle

#Δημιουργία λίστας λέξεων

words = ['programming','supernatural','ability','malfunction','virus']
splited_words = []
for i in range(len(words)):
    letters = []
    for j in words[i]:
        letters.append(j)
    splited_words.append(letters)    

#-Εκκίνηση αντίστροφης μέτρησης πριν αρχήσει το παιχνίδι-
#-Εμ΄φανιση μηνυμάτων στην αρχή και στο τέλος παιχνιδιού-
#-Κλήση word_generator-

def timer():
    for i in range(3,0,-1):
        print("GAME STARTS IN",i)
        time.sleep(1)
    else:
        print("GAME STARTED...")
        word_generator(words)
        print("GAME OVER...")

#-Όταν ο χρήστης καταφέρνει να βρει κάποια λέξη καλείται να βρει την επόμενη της λίστας words-
#-Ορισμός λίστας hidden_word η οποία εμφανίζει "_" για κάθε γράμμα της λέξης που δεν έχει βρει ο χρήστης-
#-Οριμός λίστας chosen_word με τη λέξη που πρέπει να βρει ο χρήστης-
#-Κινήσεις turtle-
#-Κλήση της word_guessing-
#-Ειδοποίηση του χρήστη όταν βρει όλες τις λέξεις που υπάρχουν στη λίστα words και στην εναλλαγή λέξεων-

def word_generator(words):
    k = 0
    while k < len(words):
        chosen_word = words[k]
        hidden_word = []
        for i in words[k]:
            hidden_word.append("_")
        for i in range(len(hidden_word)):
            if i == len(hidden_word) - 1:
                print("_")
            else:
                print("_",end=" ")
        word_guessing(chosen_word,hidden_word,10)
        if k == len(words) - 1:
            turtle.goto(425,-360)
            print("Congratulations, you found all the words! You have reached the point.")
            break
        else:
            print("Prepare for the next word...")
            time.sleep(2)
            k += 1
            if k == 1:
                turtle.goto(-250,310)
            elif k == 2:
                turtle.goto(-180,240)
            elif k == 3:
                turtle.goto(100,-80)
            else:
                turtle.goto(230,-250)

#-Καταχώρηση γραμμάτων από τον χρήστη προκειμένου να βρει τη λέξη-
#-Περιορισμός προσπαθειών με τη μεταβλητή tries-

def word_guessing(chosen_word,hidden_word,tries):
    while True:
        flag = False
        if chosen_word == hidden_word:
            print("Congratulations!")
            print("You found the word:")
            for i in range(len(hidden_word)):
                if i == len(hidden_word) - 1:
                    print(hidden_word[i])
                else:
                    print(hidden_word[i],end="")
            break
        elif tries == 0:
            print("You are out of tries... Better luck next time!")
            break
        letter = str(input("Guess a letter of the word: "))
        for i in range(len(chosen_word)):
            if letter == hidden_word[i]:
                flag = True
                print("You have already found this letter, guess another one!")
                break
            if letter == chosen_word[i]:
                hidden_word[i] = chosen_word[i]
                flag = True
                print("Correct letter!")
                for characters in range(len(hidden_word)):
                    if characters == len(hidden_word) - 1:
                        print(hidden_word[characters])
                    else:
                        print(hidden_word[characters],end=" ")
        if flag == False:
            tries -= 1
            print("Wrong letter...")
            print(tries,"Tries remaining...")
            continue

#-Σχεδιασμός του σημείου στο οποίο το turtle προσεγγίζει όλο και περισσότερο με την εύρεση κάθε λέξης-

def turtle_point_drawing():
    print("Find all the words to reach the point!")
    turtle.penup()
    turtle.goto(455,-390)
    turtle.left(90)
    turtle.pendown()
    for i in range(4):
        turtle.forward(30)
        turtle.left(90)
    for i in range(3):
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)
    else:
        turtle.right(90)
    for i in range(3):
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)
    turtle.penup()
    turtle.goto(-455,390)
    turtle.pendown()

#-Τρέξιμο του προγράμματος-

turtle_point_drawing()
timer()
