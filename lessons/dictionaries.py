"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int] 

# Initialize to an empty dictionary 
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400  # Underscore is optional
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)  # Prints curly braces for dict instead of brackets for list

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students. ")  # Use single quotes within f string because f string needs double

# Remove a key-value pair from a dictionary by its key
schools.pop("Duke")

# Test for existance of a key
is_duke_present: bool = "Duke" in schools  # Is duke in schools? True or False
print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200  # Relative reassignment

print(schools)

# Demonstration of dictionary literals

schools = {}  # Example of empty dictionary literal. Same as schools = dict(), but shorter
print(schools)

# Alernatively, initialize key-value pts
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# # What happens when a key does not exist. Look at traceback error message from bottom-up
# print(schools["UNCC"])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")
