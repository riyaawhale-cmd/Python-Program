#Create a adictionary
student ={
     "name":"Riya",
     "age":18,
     "course":"Python"
}
print("Dictionary",student)

#Access values
print("Name:",student["name"])

#Add a new key-value pair
student["city"]="Pune"
print("After adding:",student)

#Update a value
student["age"]=19
print("After updating:",student)

#Remove a key-value pair
student.pop("course")
print("After removing:",student)