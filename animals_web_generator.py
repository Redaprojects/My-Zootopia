import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def initialize_animals_data():
    """
    defines animals data from json file and returns it.
    """
    animals_data = load_data('animals_data.json')
    return animals_data

def get_each_animal_info(animals_data):
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
        ...
    return output


def implement_json_into_html_file(output_info):
    """
    reads the HTML template file by using reading flies method then replaces the string with
    each animals info and creates a new HTML file with modified information.
    """
    with open('animals_template.html', 'r') as html_file:
        animals_template = html_file.read()


    updated_html = animals_template.replace("__REPLACE_ANIMALS_INFO__", output_info)
    with open('animals.html', 'w') as new_html_file:
        write_animals_template = new_html_file.write(updated_html)


def main():
    """calls all functions inside the file and runs the generator-program"""
    animals_data = initialize_animals_data()
    output_info = get_each_animal_info(animals_data)
    implement_json_into_html_file(output_info)


if __name__ == "__main__":
    main()