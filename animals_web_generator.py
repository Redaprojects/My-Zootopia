import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(animals_data)

def each_animal_info():

    for animal in animals_data:
        name = animal["name"]
        diet = animal["characteristics"]["diet"]
        location = animal["locations"]
        type = animal["characteristics"]["type"]
        print(name, diet, location, type)
        if [name, diet, location, type] not in animals_data:
            continue
        print(f"Name: {animal["name"]}, Diet: {animal["characteristics"]["diet"]}, Location:"
        f"{animal["locations"]}, Type: {animal["type"]}")
each_animal_info()