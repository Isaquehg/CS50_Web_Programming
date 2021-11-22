#Lambda funcitons convert 1 line functions
people = [{"name": "Larry", "country": "USA"}, {"name": "Darry", "country": "Italy"}, {"name": "Merry", "country": "Mexico"}]

#def f(person):
#    return person["name"]
#we don't need to use a function to convert dicts into names

people.sort(key=lambda person: person["name"])

print(people)