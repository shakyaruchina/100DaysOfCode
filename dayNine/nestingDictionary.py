#Nesting 
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a list in a dictionary

travel_log1 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
print(travel_log1)

#Nesting dictionaries in a dictionary

#{Key:Value}; #Value = {Key:Value} #Value []
travel_log2 = {
    "France":{"cities_visited": ["Paris", "Lille", "Dijon"],"total_visits": 12},
    "Germany":{"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],"total_visits":5},
}
print(travel_log2)

#Nesting Dictionaries in a list

travel_log3 = [
    {
        "country":"France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5,
    },
    ]
print(travel_log3)