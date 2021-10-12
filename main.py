from termcolor import cprint
from tkinter import *
from ttkthemes import themed_tk
from tkinter import ttk , messagebox, filedialog
from PIL import Image, ImageTk

vendara = ['Vendara', 14]
root = themed_tk.ThemedTk()
root.geometry('900x600+500+200')
root.title('Admission-helper: Administrator Version')
root.set_theme('plastik')

# Functions
def callback():
    print(name_var.get())
    print(age_var.get())
    æ = parent_var.get().split(',')
    ś = []
    for ā in æ:
        if ā.replace(' ','') != '':
            ś.append(ā.replace(' ', ''))
    del æ
    æ = ś
    del ś
    print(æ)
    messagebox.showinfo('Info!', 'Admission succesfully added!')

def parents():
    messagebox.showinfo('Help', 'Parent name(s) seperated by commas\n\nexample:\n\n    parent-1, parent-2')


# Vars
name_var = StringVar()
age_var = IntVar()
age_var.set(6)
parent_var = StringVar()
parent_info = ImageTk.PhotoImage(image=Image.open('assets/icons/info-sign-icon.png'))


min_age = 6
max_age = 18
ages = []

for i in range(min_age, max_age + 1):
    ages.append(i)

# Buttons
submit_btn = ttk.Button(root, text='Submit', command=callback, width=12)
btn_pname_info = Button(root, image=parent_info, border=0, command=parents)

# Labels
lbl_sname = ttk.Label(root, font=vendara, text='Student Full Name:', )
lbl_sage = ttk.Label(root, font=vendara, text='Student Age:')
lbl_pname = ttk.Label(root, font=vendara, text='Parent Name(s):')


# Entrys
ent_sname = ttk.Entry(root, font=vendara, textvariable=name_var ,width=50)
ent_sage = ttk.Spinbox(root, font=vendara, textvariable=age_var ,width=48, values=ages, state='readonly')
ent_pname = ttk.Entry(root, font=vendara, textvariable=parent_var, width=50)

# grid
lbl_sname.grid(row=0, column=0)
ent_sname.grid(row=0, column=1, pady=10)
lbl_sage.grid(row=1, column=0)
ent_sage.grid(row=1, column=1)
lbl_pname.grid(row=2, column=0)
ent_pname.grid(row=2, column=1, pady=10)
btn_pname_info.grid(row=2, column=2, ipadx=10)

submit_btn.grid(row=3, column=0)

root.resizable(False, False)

# Mainloop
if __name__ == '__main__':
    root.mainloop()
