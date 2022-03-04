# -*- coding: UTF-8 -*-

import tkinter as tk_inter_
from tkinter import ttk as ttk_lib_

combo_win_ = tk_inter_.Tk()
# creates combobox
string_var_ = tk_inter_.StringVar
combo_entries_ = ttk_lib_.Combobox(combo_win_, width=30, textvariable=string_var_)


def select_priority_combo():
    # creates combo window
    combo_win_.title('Priority')
    combo_win_.geometry('250x200')
    combo_win_.configure(bg='#ff6600')
    combo_win_.eval('tk::PlaceWindow . center')  # Centers a combo in the os window
    combo_win_.attributes('-topmost', True)

    # labels the window
    label_ = tk_inter_.Label(combo_win_, text="Please set a priority \nof your message:", background="#ff6600",
                             foreground="White", font=(["Helvetica", "sans-serif"], 15, "bold"))
    label_.place(relx=.5, rely=.22, anchor="center")
    # adds combo drop menu
    combo_entries_['values'] = ["High", "Medium", "Low", "Select priority"]
    combo_entries_.current(3)
    combo_entries_.bind("<<ComboboxSelected>>", "Select priority")
    combo_entries_.place(relx=.5, rely=.5, anchor="center")
    # adds Select button
    button_ = tk_inter_.Button(combo_win_, text="Select Priority", background="Black", foreground="White",
                               font=(["Helvetica", "sans-serif"], 12, "bold"), command=handle_selected_priority)
    button_.place(relx=.5, rely=.75, anchor="center")

    combo_win_.mainloop()


def handle_selected_priority():
    from generate_index import generate_index
    selected_priority = combo_entries_.get()
    if selected_priority == "Select priority":
        selected_priority = "Low"
    combo_win_.destroy()
    generate_index(selected_priority)


