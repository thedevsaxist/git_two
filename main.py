name = "Chidiebube"

def greeting():
    print(f"Hello {name}!")

greeting()

try:
    if name == "Chidiebube":
        print(f"Welcome {name}")
except NameError:
    print("Access denied")