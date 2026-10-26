
from pyscript import display, document

# This is the list of club members, I just used AI to give me a random list of names.
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
    # This gets the values from the input fields
    first_name = document.getElementById("Firstname").value
    last_name = document.getElementById("Lastname").value

    #This takes the first name and last name from the input and combines them for checking using "in" in verify_member 
    full_name = first_name.strip() + " " + last_name.strip()

    #This checks whether the name is in the list or not
    verify_member = full_name in club_members

    # Select the correct message without if/else
    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    # Display the result on the webpage
    display(
        messages[verify_member],
        target="output1",
        append=False
    )

    #I used AI for this part to help fix what was wrong within my code because there was an error.
