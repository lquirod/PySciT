# from tkinter import Tk, Label, Button, Radiobutton, IntVar
# #    ^ Use capital T here if using Python 2.7

# def ask_multiple_choice_question(prompt, options):
#     root = Tk()
#     if prompt:
#         Label(root, text=prompt).pack()
#     v = IntVar()
#     for i, option in enumerate(options):
#         Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")
#     Button(text="Submit", command=root.destroy).pack()
#     root.mainloop()
#     if v.get() == 0: return None
#     return options[v.get()]

# result = ask_multiple_choice_question(
#     "What is your favorite color?",
#     [   "Blue!",
#         "No -- Yellow!",
#         "Aaaaargh!"
#     ]
# )

# print("User's response was: {}".format(repr(result)))
# print("type: ")
# print(type(result))
# print((result))

#from tkinter import *
# def mychoicebox(choicelist):
#     global result

#     def buttonfn():
#         global result
#         result = var.get()
#         choicewin.quit()

#     choicewin = Tk()
#     choicewin.resizable(False, False)
#     choicewin.title("ChoiceBox")
#     Label(choicewin, text="Select an item:").grid(row=0, column=0, sticky="W")
#     var = StringVar(choicewin)
#     var.set("No data")  # default option
#     popupMenu = OptionMenu(choicewin, var, *choicelist)
#     popupMenu.grid(sticky=N + S + E + W, row=1, column=0)
#     Button(choicewin, text="Done", command=buttonfn).grid(row=2, column=0)
#     choicewin.mainloop()
#     return result

# # Testing:
# reply = mychoicebox(["one", "two", "three"])
# print("reply:", reply)

from tkinter import *

from tkinter import *
def choiceDialog( optionList = [],prompt = 'Please, select an option'):
    global result

    # def buttonfn():
    #     global result
    #     result = var.get()
    #     choicewin.quit()

    # choicewin = Tk()
    # choicewin.title("ChoiceBox")
    # Label(choicewin, text="Select an item:").grid(row=0, column=0, sticky="W")
    # var = StringVar(choicewin)
    # var.set("No data")  # default option
    # popupMenu = OptionMenu(choicewin, var, *choicelist)
    # popupMenu.grid(sticky=N + S + E + W, row=1, column=0)
    # Button(choicewin, text="Done", command=buttonfn).grid(row=2, column=0)
    # choicewin.mainloop()
    # # return result

    if len(optionList) == 0:
        return None
    root = Tk()
    root.title(prompt)
    root.geometry("+20+30")
    root.minsize(500, 200)
    
    Label(root, text=prompt).pack()
    v = IntVar()
    # v.set("No data")  # default option
    for i, option in enumerate(optionList):
        Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")
    Button(text="Submit", command=root.destroy).pack()
    root.mainloop()
    # if v.get() == 0: return None
    return optionList[v.get()]

# def ask_multiple_choice_question(prompt, options):
#     root = Tk()
#     if prompt:
#         Label(root, text=prompt).pack()
#     v = IntVar()
#     for i, option in enumerate(options):
#         Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")
#     Button(text="Submit", command=root.destroy).pack()
#     root.mainloop()
#     if v.get() == 0: return None
#     return options[v.get()]

reply = choiceDialog([
        "Blue!",
        "No -- Yellow!",
        "Aaaaargh!",
        "1Blue!",
        "1No -- Yellow!",
        "1Aaaaargh!",
        "2Blue!",
        "2No -- Yellow!",
        "2Aaaaargh!",
        "3Blue!",
        "3No -- Yellow!",
        "3Aaaaargh!",
        "4Blue!",
        "4No -- Yellow!",
        "4Aaaaargh!",
    ],
     "What is your favorite color?")
print("reply:")
print(reply)

print("type: ")
print(type(reply))
print((reply))