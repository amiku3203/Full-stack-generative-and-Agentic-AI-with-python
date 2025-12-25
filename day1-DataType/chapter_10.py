#disconary

student = {
    "name": "Amit",
    "age": 22,
    "course": "MERN"
}

print(student)
chai_order= dict(type="masala chai", size="Large",sugar=32)
print(chai_order)

liquid={}
liquid["help"]="black Tea"
print(liquid)
del liquid["help"]
print(liquid)

# memebership check 
print("name" in student)

print(student.keys())
print(student.values())

last_item= student.popitem()
print(last_item)

student.update(liquid)

size=student["age"]
print(size)