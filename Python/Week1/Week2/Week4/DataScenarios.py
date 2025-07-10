# 1. A restaurant menu with prices for each item
# 2. High scores to an arcade game
# 3. All of the months of the year
# 4. All the items in your backpack
# 5. Look up Student emails by their names
# 6. A shopping cart of groceries 
# 7. [Add a scenario of your own]

# Data Structures: List, Set, Tuples, and Dictionaries
print("Scenario #1: A restaurant menu with prices for each item")
print("Best Structure: Dictionary; best to pair food with price in key/value")
menu = {
    "French Toast": 12,
    "Grand Slam": 12,
    "T-Bone Steak": 18,
    "Avacado Toast": 15,
}
for item in menu.items():
    print(key, ": ", item)

    print("Scenario #2: A restaurant menu with prices for each item")
print("Best Structure: List: Need a mutable structure to update in real time")
highScores = [
    100,
    105,
    110,
    99,
]
for score in highScores:
    print(score)

print("\nScenario #3: All of the month in the year")
print("Best Structure: Tuple: We need a collection that does not need to change")
monthsInYear = (
    "January",
    "Febuary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)
for month in monthsInYear:
    print(month)