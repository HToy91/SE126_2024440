ronald = {
    #"property": value,
    "classType": "mage",
    "homeland": "main land china",
    "health": 77,
    "age": 42,
    "weapons": ["sword", "quarterstaff"]
}

print(ronald)

#to add a property with value
ronald["pets"] = "dog"

print(ronald)

print(ronald["homeland"])

print(ronald["weapons"][1])

ronald["weapons"].append("lightstaff")

print(ronald["weapons"])

print(f"Ronald's main weapon is a {ronald["weapons"][0]} when it should be a {ronald["weapons"][2]}")