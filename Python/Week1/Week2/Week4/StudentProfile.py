# 1. Create an empty dictionary
# 2. Prompt the user for the student name key
# 3. Prompt user for the student age key
# 4. Prompt the user for the student grade key
# 5. USe a loop to prompt the user for the student hobbies until they enter "Done", then add the students hobbies
# 6. Print the dictionary to the console

student = {}

studentName = input("Enter your student's name: ")
student["Name"] = studentName

print(student)

studentAge = input("Enter your student's age: ")
student["Age"] = studentAge

print(student)

studentGrade = input("Enter your student's grade: ")
student["Grade"] = studentGrade

hobbies = []
hobby = input("Enter your student's hobby; Type 'done' when done: ").lower()
hobbies.append(hobby)

while hobby != "done":
    hobby = input("Enter your student's hobby; Type 'done' when done: ").lower()
    hobbies.append(hobby)

student["Hobbies"] = hobbies

print(student)

