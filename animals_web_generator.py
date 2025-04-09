import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(animals_data)

def get_each_animal_info():
    """
      Gets each animal information from json file based on name, location, diet and type, and prints it.
    """
    output = ""
    for animal in animals_data:


        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        location = animal.get("locations", [])[0]
        animal_type = characteristics.get("type")
        #print(animal_type)
        if "name" in animal:
            output += f"Name: {name}\n"
        if "locations" in animal:
            output += f"Location: {location}\n"
        if "characteristics" in animal:
            if "diet" in characteristics:
                output += f"Diet: {diet}\n"
            if "type" in characteristics:
                output += f"Type: {animal_type}\n"
    return output
output_info = get_each_animal_info()

def implement_json_into_html_file():
    with open('animals_template.html', 'r') as html_file:
        animals_template = html_file.read()


    updated_html = animals_template.replace("__REPLACE_ANIMALS_INFO__", output_info)
    print(updated_html)

def main():
    implement_json_into_html_file()


if __name__ == "__main__":
    main()