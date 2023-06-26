info = {
    "name": "Interstellar",
    "rating": 7.8,
    "director": "nolan",
    "release": "2014",
    "age suitability ": 16
}

# while True:
#     key = input("Search for a key : ")
#     if key in info:
#         print('Found :', info[key])
#     else:
#         print("Key not found")

while True:
    key = input("Search for a key : ")
    try:
        print('Found :', info[key])
    except KeyError:
        print("Key not found")
