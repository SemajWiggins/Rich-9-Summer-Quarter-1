# Step 1: Create a list of every Genius at your table
geniuses = ["Semaj", "Marshawn", "Max", "Avery", "Kauri"]

# Step 2: Loop through that list and print everyones name to the termianl
# What type of loop are we using here?
for genius in geniuses:
    print(genius)

# Step 3: Prompt the user to print the list again
answer = input("Do you want me to print the list again? Y/N")
while answer == "Y":
    for genius in geniuses:
        print (genius)
    answer = input("Do you want me to print the list again? Y/N")