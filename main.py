from pyscript import display, document
# This is the list of club members
club_members = [
    "Juan Dela Cruz",
    "Maria Santos",
    "Alex Reyes",
    "Sofia Garcia",
    "Miguel Torres",
    "Andrea Flores",
    "Daniel Ramos",
    "Isabella Cruz",
    "Joshua Mendoza",
    "Gabriella Rivera",
    "Ethan Castillo",
    "Camille Bautista",
    "Nathan Villanueva",
    "Chloe Fernandez",
    "Liam Morales",
    "Ashley Aquino",
    "Gabriel Navarro",
    "Nicole Herrera",
    "Adrian Gonzales",
    "Beatrice Lim"
]


def Submit(e):
first_name = document.getElementById("Firstname").value
last_name = document.getElementById("Lastname").value #This these are the values that connect to the Input Texts with their respective ids as Firstname and Lastname

full_name = first_name.strip() + " " + last_name.strip() #This adds the values of the variable "first_name" to the values of the variable "last_name"


verify_member = full_name in club_members #The operator "in" checks if the input of the variable full_name is in the list of the variable club_members

messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

# Display the result on the webpage
display(messages[verify_member], target="output1", append= False)