# mad libs project Week1, Python. 

# by Victor dos Santos

#Printing the first view to the reader
print("Please enter the followiong: ")
print()
#making request to input informations
familiar_name1 = input("One familiar (ex: mom, dad, brother): ")
familiar_name2 = input("Another familiar: ")
verb1 = input("A verb: ")
past_verb = input("Past verb: ")
adjective1 = input("Adjective: ")
adjective2 = input ("Another adjective: ")
comparative = input("Comparative: ")
felling = input("Filling: ")
exclamation = input("Exclamation: ").capitalize()
geometrical_formula = input("Geometrical formula: ")

# Organizing the informations in lines
line1 = f"I was looking for a {adjective1} place with my {familiar_name1}."
line2 = f"Then I {verb1} a {adjective2} one place close here."
line3 = f"My {familiar_name1} and I call my {familiar_name2} to see this {adjective2} close place."
line4 = f"But my {familiar_name2} was {felling}, because thought {comparative} than another places that my {familiar_name2} have seen.\n"
line5 = f"Well, when we get there, my {familiar_name1} and I {past_verb} each {geometrical_formula}, my {familiar_name2} exclaim: {exclamation}! \n"
line6 = f"And my {familiar_name2} was no more {felling}because my {familiar_name2} have seen things hasn't expected."

#Printing the informations.
print()
print("Now, read the following story and have fun ")
print("----------------------------------------------------------------------------------------------")
print(line1 + line2 + line3 + line4 + line5 + line6 )
print("----------------------------------------------------------------------------------------------")