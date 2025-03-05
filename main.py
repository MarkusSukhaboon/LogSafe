import csv
import tkinter
from tkinter import messagebox, ttk
import pyperclip
from pw_generator import create_pw

# Constants
LOGSAFE_IMG_PATH = "logsafe_bg_400x400.png"
LOGSAFE_ICO_PATH = "logsafe_icon_32x32.png"
WINDOW_BG_COLOR = "#f1e2c3"
LBL_COLOR = "#e4b4aa"
BTN_A_COLOR = "#87cf80"
BTN_B_COLOR = "#a4c3e0"

# Business logic
# Data handling via dictionary

all_entries_list = []# List of dictionaries

def create_list_from_csv():
    global all_entries_list
    all_entries_list = []
    try:
        with open('all_passwords.csv', 'r', newline='') as reader_file:
            reader = csv.DictReader(reader_file)
            for line in reader:
                all_entries_list.append(line)

        # Update combobox with webpage_app values
        update_combobox()

    except FileNotFoundError:
        print("CSV file not found. Starting with an empty list.")

def update_combobox():
    """Update the Combobox with unique website/app names from the CSV."""
    websites = [entry["webpage_app"] for entry in all_entries_list if "webpage_app" in entry]
    webpage_app_combobox["values"] = websites


def create_dict_from_user_input():
    data = {
        "entry_index": len(all_entries_list)+1, # only this value is generated from loaded list
        "webpage_app": webpage_app_var.get(),
        "login": login_var.get(),
        "password": password_var.get(),
        "comment": comment_var.get(),
    }
    return data

def create_pop_up_message(message_str):
    pop_up = tkinter.Toplevel(window)
    pop_up.geometry(window.winfo_geometry())
    pop_up.geometry("400x400")
    pop_up.columnconfigure([0, 2], weight=1)
    pop_up.columnconfigure([1], weight=2)
    pop_up.rowconfigure([0], weight=2)
    pop_up.rowconfigure([1, 2, 3], weight=1)
    tkinter.Canvas(pop_up, bg=WINDOW_BG_COLOR).grid(row=0, column=0, columnspan=3, padx=0, sticky="nsew")
    tkinter.Label(pop_up, text=message_str, pady=0).grid(row=1, column=1, pady=20, sticky="ew")
    tkinter.Button(pop_up, text="OK", bg=BTN_A_COLOR, command=pop_up.destroy).grid(row=2, column=1, pady=20, sticky="ew")


def safe_dictionary_entries():
    # Get the values from the entry widgets and strip off whitespace
    webpage_app = webpage_app_var.get().strip()
    login = login_var.get().strip()
    password = password_var.get().strip()

    # Validate required fields and
    # "return" which means to abort the saving-process
    if not webpage_app:
        create_pop_up_message("Webpage/App field cannot be empty!")
        return
    elif not login:
        create_pop_up_message("Login/E-Mail field cannot be empty!")
        return
    # In case user logs in via another account
    elif not password:
        password_var.set("E-Mail Login")
    # Reload list from CSV
    create_list_from_csv()

    # Create a dictionary for the current entry
    new_entry = create_dict_from_user_input()

    # Check if the entry already exists in the list
    entry_found = False
    for i, entry in enumerate(all_entries_list):
        if entry["webpage_app"] == new_entry["webpage_app"]:
            # Update the existing entry
            all_entries_list[i] = new_entry
            entry_found = True
            break

    # If the entry does not exist, append it to the list
    if not entry_found:
        all_entries_list.append(new_entry)

    # Print the list of all entries for debugging
    #print(all_entries_list)

    # Define the fieldnames for the CSV file
    fieldnames = ['entry_index', 'webpage_app', 'login', 'password', 'comment']

    # Write all entries to the CSV file
    with open("all_passwords.csv", "w", newline='') as writer_file:
        writer_obj = csv.DictWriter(writer_file, fieldnames=fieldnames)
        # Write the header
        writer_obj.writeheader()
        # Write all rows from the list
        for row in all_entries_list:
            writer_obj.writerow(row)

    # Update combobox with webpage_app values
    update_combobox()

    # Clear the input fields after saving
    webpage_app_var.set("")
    login_var.set("")
    password_var.set("")
    comment_var.set("")


# Copy-to-clipboard function
def copy_string(string_var):
    try:
        string = pyperclip.copy(string_var)
        #tkinter.messagebox.showinfo(f"Copied", {string})
        print(string)
    except Exception as e:
                messagebox.showerror("Error", f"Failed to generate code: {e}")


def update_entries(event):
    """Populate entry widgets based on selected website in Combobox."""
    # Load list of dictionaries from *.csv file
    # create_list_from_csv()
    selected_website = webpage_app_var.get()

    # Find the matching dictionary
    for entry in all_entries_list:
        if entry["webpage_app"] == selected_website:
            login_var.set(entry["login"])
            password_var.set(entry["password"])
            comment_var.set(entry["comment"])
            return

    # If no match is found, clear the fields
    login_var.set("")
    password_var.set("")
    comment_var.set("")

# UI
# Root window
window = tkinter.Tk()
window.title("LogSafe")
# Load the image file from disk.
icon = tkinter.PhotoImage(file=LOGSAFE_ICO_PATH)
# Set it as the window icon.
window.iconphoto(True, icon)
print(window.winfo_geometry())
window.geometry("800x800+0+0")
window.minsize(200, 200)
window.maxsize(400, 800)
window.config(bg=WINDOW_BG_COLOR)


# Tkinter variables
entry_index_var = tkinter.StringVar()
webpage_app_var = tkinter.StringVar()  # (value="https://www.")
login_var = tkinter.StringVar()
password_var = tkinter.StringVar()
pw_length_var = tkinter.IntVar(value=8)
comment_var = tkinter.StringVar()

# Canvas for logo
logo_canvas = tkinter.Canvas(window, width=400, height=400, highlightthickness=0)
logsafe_logo = tkinter.PhotoImage(file=LOGSAFE_IMG_PATH)
logo_canvas.create_image(0, 0, anchor="nw", image=logsafe_logo)  # Background
logo_canvas.grid(row=0, rowspan=1, column=0, columnspan=4, padx=0, pady=0, sticky="nsew")

## Labels and input boxes
# Label and input box webpage / app
webpage_app_lbl = tkinter.Label(text="Webpage / App",
                                font=("arial", 12, "bold"),
                                bg=LBL_COLOR,
                                width=12,
                                height=1)
webpage_app_lbl.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

webpage_app_input = tkinter.Entry(textvariable=webpage_app_var,
                                  font=("arial", 12, "bold"),
                                  width=16)
webpage_app_input.grid(row=1, column=1, columnspan=2, padx=5, pady=10, sticky="nsew")

webpage_app_copy_btn = tkinter.Button(text="Copy",
                                      font=("arial", 12, "bold"),
                                      bg=BTN_B_COLOR,
                                      width=5,
                                      height=1,
                                      command=lambda: copy_string(webpage_app_var.get()))
webpage_app_copy_btn.grid(row=1, column=3, padx=5, pady=10, sticky="nsew")

# Label and input box login / e-mail
login_lbl = tkinter.Label(text="Login / E-Mail",
                          font=("arial", 12, "bold"),
                          bg=LBL_COLOR,
                          width=12,
                          height=1)
login_lbl.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

login_input = tkinter.Entry(textvariable=login_var,
                            font=("arial", 12, "bold"),
                            width=16)
login_input.grid(row=2, column=1, columnspan=2, padx=5, pady=10, sticky="nsew")

login_input_btn = tkinter.Button(text="Copy",
                                 font=("arial", 12, "bold"),
                                 bg=BTN_B_COLOR,
                                 width=5,
                                 height=1,
                                 command=lambda: copy_string(login_var.get()))
login_input_btn.grid(row=2, column=3, padx=5, pady=10, sticky="nsew")

# Label and input box password
password_lbl = tkinter.Label(text="Password",
                             font=("arial", 12, "bold"),
                             bg=LBL_COLOR,
                             width=12,
                             height=1)
password_lbl.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

password_input = tkinter.Entry(textvariable=password_var,
                               font=("arial", 12, "bold"),
                               width=16)
password_input.grid(row=3, column=1, columnspan=2, padx=5, pady=10, sticky="nsew")

password_input_btn = tkinter.Button(text="Copy",
                                    font=("arial", 12, "bold"),
                                    bg=BTN_B_COLOR,
                                    width=5,
                                    height=1,
                                    command=lambda: copy_string(password_var.get()))
password_input_btn.grid(row=3, column=3, padx=5, pady=10, sticky="nsew")

# Generate password
pw_generator_lbl_1 = tkinter.Label(text="Password Length",
                                   font=("arial", 12, "bold"),
                                   bg=LBL_COLOR,
                                   width=12,
                                   height=1)
pw_generator_lbl_1.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

# Create the Combobox for password length
pw_length_combobox = ttk.Combobox(window,
                                  textvariable=pw_length_var,
                                  values=list(range(1, 21)),
                                  width=2)
pw_length_combobox.grid(row=4, column=2, padx=5, pady=10, sticky="nse")

pw_generator_btn = tkinter.Button(text="Create",
                                  font=("arial", 12, "bold"),
                                  bg=BTN_A_COLOR,
                                  width=5,
                                  height=1,
                                  command=lambda: password_var.set(create_pw(pw_length_var.get())))
pw_generator_btn.grid(row=4, column=3, columnspan=1, padx=5, pady=10, sticky="nsew")

# Label and input box comment
comment_lbl = tkinter.Label(text="Comment",
                            font=("arial", 12, "bold"),
                            bg=LBL_COLOR,
                            width=12,
                            height=1)
comment_lbl.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

comment_input = tkinter.Entry(textvariable=comment_var,
                              font=("arial", 12, "bold"),
                              width=16)
comment_input.grid(row=5, column=1, columnspan=2, padx=5, pady=10, sticky="nsew")

comment_input_btn = tkinter.Button(text="Copy",
                                   font=("arial", 12, "bold"),
                                   bg=BTN_B_COLOR,
                                   width=5,
                                   height=1,
                                   command=lambda: copy_string(comment_var.get()))
comment_input_btn.grid(row=5, column=3, padx=5, pady=10, sticky="nsew")

# Save button
safe_dictionary_entries_btn = tkinter.Button(text="Save in database",
                                             font=("arial", 12, "bold"),
                                             bg=BTN_A_COLOR,
                                             height=1,
                                             command=safe_dictionary_entries)
safe_dictionary_entries_btn.grid(row=6, column=1, columnspan=3, padx=5, pady=10, sticky="nsew")

# Combobox for webpage/app selection

load_record_lbl = tkinter.Label(text="Load Record",
                            font=("arial", 12, "bold"),
                            bg=LBL_COLOR,
                            width=12,
                            height=1)
load_record_lbl.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

webpage_app_combobox = ttk.Combobox(window, textvariable=webpage_app_var,
                                    width=1,
                                    )
webpage_app_combobox.grid(row=7, column=1, columnspan=3, padx=5, pady=10, sticky="nsew")
webpage_app_combobox.bind("<<ComboboxSelected>>", update_entries)

# Load data from CSV and update the Combobox
create_list_from_csv()

# Start the main loop
window.mainloop()