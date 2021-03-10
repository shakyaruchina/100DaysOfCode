#Dictionary {Key:Value}
#or {Key:Value, Key:Value}
programming_dictionary={
    "Bug": "An error in a program that prevens the program from running as expected.",
    "Function" : "A place of code that you can easily call over and over again.",
    }
print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#Empty dictionary
empty_dictionary = {}

#Wiping existing directory
# programming_dictionary = {}

#loop through a dictionary
for thing in programming_dictionary:
    #prints only key
    print(thing)
    #prints the value
    print(programming_dictionary[thing])

#Quiz 1
start_dict = {
    "a" :9,
    "b" :8,
}
final_dict = {
    "a":9,
    "b":8,
    "c" :7,
}
start_dict["c"]=7
final_dict = start_dict
print(final_dict)

#Quiz2
dict = {
    "a" : 1,
    "b" :2,
    "c" :3,
}
#Error
print(dict[1])
#print(dict)

#Quiz 3
order = {
    "starter": {1: "Salad", 2: "Soup"}, 
    "main": {1:["Burger","Fries"],2:["Steak"]},
    "dessert": {1:["Ice cream"],2:[]},
}
#prints Steak
print(order["main"][2][0])





