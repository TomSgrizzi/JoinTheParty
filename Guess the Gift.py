#Rule generation and finding game. The game creates a random rule based on either initials, or number of letters,
# or semantic field. The user has to find the rule by submitting for five times the correct word, after that
#time, the game will reveal the rule. The game will also allow a "Quit" button where the user can find the rule by itself

########## PACKAGES ############

import string
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Text
import random
from tkinter import messagebox
#API from FIGMA : figd_C9UCsaqRfgV6P4Ek_nKxrWXE7bBV-c5TtAD-z6NV
################ SETTING UP THE GUI ######################
root = Tk()
root.title("Join the Party")
root.geometry('700x350')
initialize_frame = tk.Frame(root)
game_page = tk.Frame(root)

def initialize_the_frame ():
    initialize_frame = tk.Frame(root)
    return initialize_frame

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
initialize_frame.grid(column=1,row=0)

def initialize_the_frame ():
    initialize_frame = tk.Frame(root)
    return initialize_frame

########## GLOBAL VARIABLES #########
guess_number = 1
right_words = []
right_number = 0
game_chosen = 0

######## VARIABLES FOR RANDOM INDEX CHARACTER ########
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
random_letter = random.choice(string.ascii_lowercase)
random_index = random.choice([0,1,2,3,4,5,-1])


######## VARIABLES FOR RANDOM LENGHT OF WORD ########
random_word_lenght = random.choice(range(2,8))

###### Buttons and fields Intro page ###           NOT COPIED

initialize = Button(initialize_frame, text="Let's play!", background="green",command=lambda: show_frame(game_page,initialize_frame), foreground="white")
quit = Button(game_page,text="Quit",background="red",foreground="white",command=lambda: root.destroy())


######## GUI FEEDBACKS #####
correct = Label(game_page, text="That's a nice gift!",padx=10)
wrong = Label(game_page, text="Nah, I don't like that gift",padx=10)

############## GUI FUNCTIONS ################

def initialize_clicked():
    # Hide label and rules
    label.grid_forget()
    rules.grid_forget()
    initialize.grid_forget()
    initialize_the_frame()

def show_frame(frame,current_frame):
    current_frame.grid_forget()
    frame.grid(column=1,row=0)
    frame.tkraise()


def show_message():
    question = messagebox.showinfo(title="Congrats!",message=f'Congrats! You had to find words having the letter "{random_letter}" at the position number {random_index+1}, you got it and you may now join the party!')


def show_message_menouno():
    question = messagebox.showinfo(title="Congrats!",message=f'Congrats! You had to find words having the letter "{random_letter}" as the last letter, you got it and you may now join the party!')


def cheating_message():
    issue = messagebox.showinfo(title="Warning!",message=f'Are you trying to cheat? You already used the word "{attempt.get()}", submit a different word.')

def solution_message_random_letter_at_random_place():
    solution = messagebox.askquestion('Getting tired?', "You have been waiting at the party's door for a long time, do you want to know the solution?",
                                        icon='warning')
    if solution == "yes":
        if random_index == -1:
            messagebox.showinfo(title="Congrats!",message=f'Congrats! You had to find words having the letter "{random_letter}" as the last letter, you got it and you may now join the party!')
        else:
            messagebox.showinfo(title="Solution", message=f'You had to find words having the letter "{random_letter}" at the position number {random_index+1}')
        root.destroy()

def invalid_input():
    invalid_inpu = messagebox.showinfo(title="Warning!",message="Invalid input, try again.")


def warning_random_lenght_of_words():
    issue = messagebox.showinfo(title="Warning!",message=f"The word has at least {random_index-1} letters.")


def solution_random_lenght_of_words():
    solution = messagebox.askquestion('Getting tired?', "You have been waiting at the party's door for a long time, do you want to know the solution?",
                                        icon='warning')
    if solution == "yes":
        messagebox.showinfo(title="Solution", message=f'You had to find words of {random_word_lenght} characters.')
        root.destroy()

def congrats_random_lenght_of_words():
    question = messagebox.showinfo(title="Congrats!",message=f'Congrats! You had to find words of {random_word_lenght} characters, you got it and you may now join the party!')


def solution_initial_letter():
    question = messagebox.askquestion('Getting tired?', "You have been waiting at the party's door for a long time, do you want to know the solution?",
                                      icon='warning')
    if question == "yes":
        messagebox.showinfo(title="Solution",message=f"You had to find words having the letter {random_letter} as the initial letter")
        root.destroy()

def congrats_initial_letter():
    messagebox.showinfo(title='Congrats!',message=f"Congrats! You had to find words having the letter {random_letter} as the initial letter, you got it and now you can join the party!")


def reset_wigets():
    for widget in game_page.winfo_children:
        if isinstance(widget,tk.Entry):
            widget.delete(0,'end')
        if isinstance(widget, tk.StringVar):
            widget.set("")
        if isinstance(widget, tk.Label):
            widget.grid_forget()
        if isinstance(widget, tk.Text):
            widget.delete('1.0', tk.END)
        initialize_frame.grid(column=1,row=0)


################ GAME LOGIC ##########################

def random_letter_at_random_place():
    global guess_number
    def check_input(word):
        global right_number
        input_word = word
        if input_word[random_index].lower() == random_letter:
            if input_word in right_words:
                cheating_message()
                right_number += -1
            else:
                right_words.append(input_word)
                wrong.grid_forget()
                correct.grid(column=1,row=14)
                print("correct")
            right_number += 1
            print(True)
        else:
            print(False)
            wrong.grid(column=1,row=14)
    print(attempt.get())
    print(random_index)

    def check_word_lenght(word):
        if len(word) > random_index:
            print("len word is "+str(len(word))+" and the index is "+str(random_index))
            check_input(word)
        else:
            invalid_input() 

    #if random_index == -1:
    #    print("Try to solve the puzzle")
    #elif random_index <= 3:
    #    print("The word has at least a couple of letters")
    #else:
    #    print(f"The word has at least {random_index-1} letters.")

    if guess_number > 0:
        word = attempt.get()
        check_word_lenght(word)
        guess_number += 1
        print(random_index)
        print(random_letter)
        if right_number >= 5:
            if random_index == -1:
                show_message_menouno()
            else:
                show_message()
        if guess_number >= 10 and right_number <= 5:
            solution_message_random_letter_at_random_place()
        user_input_entry.delete(0, END) 
        user_input_entry.focus()




def random_lenght_of_word():
    global guess_number

    def check_word_lenght(word):
        if len(word) < random_word_lenght:
            invalid_input()
        else:
            check_input(word)

    def check_input(word):
        global right_number
        input_word = word
        if len(input_word) == random_word_lenght:
            if input_word in right_words:
                cheating_message()
                right_number += -1
            else:
                wrong.grid_forget()
                correct.grid(column=1,row=14)
                right_words.append(input_word)
            right_number += 1
            print(True)
        else:
            print(False)
            wrong.grid(column=1,row=14)

    if random_word_lenght == 2 and len(attempt.get()) < 2:
        warning_random_lenght_of_words()

    if guess_number > 0:
        word = attempt.get()
        check_word_lenght(word)
        guess_number += 1
        print(random_word_lenght)
        if right_number >= 5:
            congrats_random_lenght_of_words()
        if guess_number >= 10 and right_number <= 5:
            solution_random_lenght_of_words()
        user_input_entry.delete(0, END) 
        user_input_entry.focus()


def initial_letter():
    global random_letter
    global guess_number

    def check_input(word):
        global right_number
        input_word = word
        if input_word[0].lower() == random_letter:
            if input_word in right_words:
                cheating_message()
                right_number += -1
            else:
                right_words.append(input_word)
                wrong.grid_forget()
                correct.grid(column=1,row=14)
            right_number += 1
            print(True)
        else:
            print(False)
            wrong.grid(column=1,row=14)

    if guess_number > 0:
        word = attempt.get()
        check_input(word)
        guess_number += 1
        print(random_letter)
        if right_number >= 5:
            congrats_initial_letter()
        if guess_number >= 10 and right_number != 5:
            solution_initial_letter()
        user_input_entry.delete(0, END) 
    

def sematic_field():
    pass


list_of_functions = [1,2,3]
game_chosen = random.choice(list_of_functions)

def random_function():
    if game_chosen == 1:
        print("random letter at random place")
        return random_letter_at_random_place()
    if game_chosen == 2:
        print("random length of word")
        return random_lenght_of_word()
    if game_chosen == 3:
        print("random initial letter")
        return initial_letter()








#### Buttons and fields Game page ####
entry_guess = ""
game_title = Label(game_page, text="Join the Party!", foreground="black",font=('Calibri',40),pady=10)
entry_intro = Label(game_page, text="What gift do you bring?",font=('Calibri',14))
attempt = StringVar()
user_input_entry = ttk.Entry(game_page,  textvariable=attempt, font=('Calibri', 12))
submit_button = ttk.Button(game_page, text="Submit", command=random_function)

congrats = ttk.Button(game_page,text=f"\n Congrats! You got the rule and you may come in!", command=show_message)
text_widget = Text(game_page, height=10, width=40)



################### GUI ELEMENTS ######################

label = Label(initialize_frame, text="Join the Party!", foreground="black",font=('Calibri',40),pady=10)
rules = Label(initialize_frame, text="""
              
Welcome to "Join the Party"!
The rule is simple: only if you carry the right gift you will be accepted to the party.
The game will randomly generate an "entry rule", and all you have to do is find it.
How? By submitting your hypotheses on what constitutes the right gift.
Every gift (i.e., every word) is analyzed by the game in terms of whether it complies or not with the entry rule.
The game will tell you whether the gift is accepted or not,
and only when you have submitted 5 consecutive correct gift, the game will assume you got the right rule.
Come join the party!
""",padx=10)


###### Intro Page #####
initialize_the_frame()
label.grid(column=1,row=0)
rules.grid(column=1,row=1)
print("")
initialize.grid(column=1,row=2)

###### Game Page #####
game_title.grid(column=1,row=0)
entry_intro.grid(column=1,row=1)
user_input_entry.grid(column=1,row=13)
user_input_entry.focus()
submit_button.grid(column=1,row=15)
root.bind('<Return>',lambda e: random_function())




root.mainloop()