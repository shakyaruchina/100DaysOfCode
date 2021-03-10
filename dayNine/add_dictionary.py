travel_log = [
    {
        "country" : "France",
        "visits": 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visits": 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    },
]

#Adding new entry to travel log

def add_new_country(new_country_visited, visit_number, cities_visited):
    new_country= {}
    new_country["country"] = new_country_visited
    new_country["visits"] = visit_number
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia",2,["Moscow", "Saint Petersburg"])
print(travel_log) 