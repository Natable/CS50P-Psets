# Dictionaries and Lists
# "name" : "Hermione" - the name is key and Hermione is the value assigned to it
# I suck ass at programming yall

students = [
    {"name" : "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name" : "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name" : "Ron", "house": "Gryffindor", "patronus": "Jack Russell terier"},
    {"name" : "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student ["patronus"], sep=", ")