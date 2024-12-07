### This Python file creates an App using tkinter 
### The purpose of this app is a beta database for a Muslim match making 
### The app will be name 'Ahlan' which is Arabic for 'Welcome' 
### Users will enter there name, age, and email 
### Ahlan match makers will reach out to users in beta 
### App will be further developed to include match profile and questions 

from tkinter import *

# create app GUI window using tkinter command 
appWindow = Tk()
appWindow.title("Welcome | Ahlan")

# create a welcome label widget
labelWelcome = Label(appWindow, text = "Salamu Alaikum", font=('calibre',14,'normal'))

# pack the labelWelcome widget to the gui 
labelWelcome.pack(side='top')

# create a labelDescription widget that describes the app description
labelDescription = Label(appWindow, text="This is the beta version of Ahlan Muslim Match App. Here you will leave your contact information so our match specialist can match you with your possible spouse in shaa Allah!")

# pack labelDescription to gui after labelWelcome
labelDescription.pack()

# define a custom_function to store a button widget to close the app
def custom_function():
        print("You successfully closed the page.")
        appWindow.destroy()

button = Button(appWindow, text="Close app!", command = custom_function)


# This will create a local database called appBuild1.db
# The database will have a table called app_data with
# three columns: name, age, email

import sqlite3

sql_connect = sqlite3.connect('appBuild1.db')

cur = sql_connect.cursor() # creates a cursor object

cur.execute('''
CREATE TABLE IF NOT EXISTS app_data (
    name TEXT,
    age INTEGER,
    email TEXT
    
    )
''')
sql_connect.commit()


name_var = StringVar() #declares a string variable
age_var = IntVar() #declares an integer variable
email_var = StringVar() #declares a string variable

label_age = Label(appWindow, text="What is your age?",
                 font=('helvetica',14,'bold'))
age_entry = Entry(appWindow,
    textvariable = age_var,
    font=('calibre',14,'normal'))                    

label_name = Label(appWindow, text="What is your name?",
                 font=('helvetica',14,'bold'))
name_entry = Entry(appWindow, 
    textvariable = name_var, 
    font=('calibre',14,'normal'))

label_email = Label(appWindow, text="What is your email?",
		  font=('helvetica',14,'bold'))
email_entry = Entry(appWindow,
	textvariable = email_var,
	font=('calibre',14,'normal'))

# New label to show output on the screen
output_label = Label(appWindow, text="", font=('calibre', 14, 'normal'))

def getNameAge():
    # Gets the name, age, and email data
    name = name_var.get()
    age = age_var.get()
    email = email_var.get()	

    # Display the input name and age in the output label
    output_label.config(text=f"Hello {name}, you are {age} years old. Our match specialist will contact you at email: {email}")

    # What do you want to do with the name and age data?
    # Save your data to your database using parameterized queries
    query = "INSERT INTO app_data (name, age, email) VALUES (?, ?, ?)"
    cur.execute(query, (name, age, email))
    sql_connect.commit()

    # Clear the name and age
    name_var.set("")
    age_var.set("")
    email_var.set("")
    	
 
    
submit_button = Button(appWindow,
    text="Submit",
    font=('calibre',14,'normal'),
    command = getNameAge)

label_name.pack()
name_entry.pack()
label_age.pack()
age_entry.pack()
label_email.pack()
email_entry.pack()
submit_button.pack()
button.pack()
output_label.pack()

# create tkinter loop
appWindow.mainloop()
