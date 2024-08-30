 #1
car = {
    "color": "dark gray",
    "seats": "8",
    "year": 2008
}

print(car["color"])
print(car["seats"])
print(car["year"])


print(car.get("color"))
print(car.get("seats"))
print(car.get("year"))

 #2
house = {
    "stories": 2,
    "rooms": 4,
    "color": "white"
}

for i in house.keys:
    print(i)

#3
furniture = {
    "color" : ["Green", "Red", "White"],
    "inside_Drawer" : ["Pen","Phone Charger," ],
    "Sofa_Color" : ["Light Brown", "Black"]
}



#4
student_age_boy = {
    "Dachi": 12,
    "Luka": 31,
    "Data": 15,
    "student_age_girl": {
        "Mariami": 11,
        "Anna": 32
    }
}
