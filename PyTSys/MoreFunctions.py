from tkinter import *
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter import filedialog as fd

########################################################################################################
######## Operations file-related
#### Ask a path location file
def askFileLocation():
    def get_file_path():
        global file_path
        # Open and return file path
        file_path= fd.askopenfilename(title = "Select A File" )#filetypes = (("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
        l1 = Label(window, text = "File path: " + file_path).pack()
        return file_path

    window = Tk()
    # Creating a button to search the file
    b1 = Button(window, text = "Open File", command = get_file_path).pack()
    b2 = Button(window, text = "Close", command = window.destroy).pack()
    window.mainloop()

    return file_path
    # return 'C:/Users/Leticia/Documents/GitHub/Pruebas/pruebaCSV/trainPruebas.csv'

########################################################################################################
######## Input-like operations
#### Ask the user to choose an option (single).
# Return: the option selected
def choiceDialog( optionList = [],prompt = 'Please, select an option', retValue = 1):
    if len(optionList) == 0:
        return None
    root = Tk()
    root.title(prompt)
    root.geometry("+20+30")
    root.minsize(500, 200)
    
    Label(root, text=prompt).pack()
    var = IntVar()
    #     var = StringVar(choicewin)
    #     var.set("No data")  # default option
    var.set(None)  # default option
    for i, option in enumerate(optionList):
        Radiobutton(root, text=option, variable=var, value=i).pack(anchor="w")
    Button(text="Submit", command=root.destroy).pack()
    root.mainloop()
    if var.get() is None:
        return None
    else:
        if retValue == 0:
            return var.get()
        elif retValue == 1:
            return optionList[var.get()]
        else:
            return [var.get(), optionList[var.get()]]

