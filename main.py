'''from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

FONT_STYLE = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_letters = [(choice(letters)) for char in range(randint(8, 10))]

password_symbols = [(choice(symbols)) for char in range(randint(2, 4))]
def password_generator():

    password_numbers = [(choice(numbers))for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
                website: {
                     "email": email,
                     "Password": password,
                }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Your added details are:\nEmail: {email}\nPassword: {password}.")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    #saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- Find password -------------------------- #


# def find_password():
#     website = website_entry.get()
#     print(website)
#     try:
#         with open("data.json") as data_file:
#             data = json.load(data_file)
#     except FileNotFoundError:
#         messagebox.showinfo(title="Error", message="No Data File Found")
#     else:
#         if website in data:
#             email = data[website]["email"]
#             password = data[website]["Password"]
#             messagebox.showinfo(title=website, text=f"email: {email}\npassword: {password}")
#         else:
#             messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.config(padx=5, pady=5)
website_label.grid(column=0, row=1)


website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

# search_button = Button(text="Search", command=find_password)
# search_button.grid(column=2, row=1, sticky="EW")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "sravanisiriguppa7@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
'''
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

FONT_STYLE = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_letters = [(choice(letters)) for char in range(randint(8, 10))]

password_symbols = [(choice(symbols)) for char in range(randint(2, 4))]

password_numbers = [(choice(numbers))for char in range(randint(2, 4))]
def password_generator():

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
                website: {
                     "email": email,
                     "Password": password,
                }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Your added details are:\nEmail: {email}\nPassword: {password}.")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    #saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.config(padx=5, pady=5)
website_label.grid(column=0, row=1)


website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "sravanisiriguppa7@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
