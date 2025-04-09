import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(animals_data)

def each_animal_info():
    for animal in animals_data:

        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        location = animal.get("locations", [])[0]
        animal_type = characteristics.get("type")
        #print(animal_type)
        if "name" in animal:
            print(f"Name: {name}")
        if "locations" in animal:
            print(f"Location: {location}")
        if "characteristics" in animal:
            if "diet" in characteristics:
                print(f"Diet: {diet}")
            if "type" in characteristics:
                print(f"Type: {animal_type}")
each_animal_info()