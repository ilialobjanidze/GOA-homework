#1
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

for key, value in my_dict.items():
    print("Key:", key, ", Value:", value)

#2
# სამივე მანქანის dictionary-ს შექმნა
car1 = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "price": "$20,000"
}

car2 = {
    "brand": "Honda",
    "model": "Civic",
    "year": 2019,
    "price": "$18,500"
}

car3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2021,
    "price": "$26,000"
}

# მანქანების dictionary-ების სია
cars = [car1, car2, car3]

# მომხმარებლისთვის ინფორმაციის ჩვენება
print("გამარჯობა! აქ არის რამდენიმე მანქანა, რომელთა შეძენა შეგიძლიათ:")
for i, car in enumerate(cars, start=1):
    print("\nმანქანა", i)
    print("ბრენდი:", car["brand"])
    print("მოდელი:", car["model"])
    print("წელი:", car["year"])
    print("ფასი:", car["price"])
