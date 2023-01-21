dictionary = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}

newDictionary = {}
for key, value in dictionary.items():
    if value >= 3:
        newDictionary[key] = value

print(newDictionary)
