# 1. Create a list of 5 of your favorite snacks
# 2. Create a tuple of 5 colleges you want to attend
# 3. Create a set of with 5 pieces of data on anything you want; 
# 4. Create a dictionary on a car; key must describe an attribute of the car, followed it's value.

favoritesnackslist = ["Popcorn", "Gummies", "Chocolate", "Apple", "Snack Bar"]
favoritesnackslist.append("Licorice")
favoritesnackslist.sort()
for snack in favoritesnackslist:

    myColleges = ("UC Berkeley", "UC Davis", "Standford University")
for College in myColleges:
    print(College)

numberGrade = {33 , 72, 42, 21, 94}
for grade in numberGrade:
    print(grade)

carAttribute = { "Brand": "Honda",
                "Model": "Civic",
                "Year": "2020",
                "Engine": "V12",
                "WheelSize": "18in"}
carAttribute["color"] = "silver"
for attribute in carAttribute:
    print(carAttribute.get(attribute))
    