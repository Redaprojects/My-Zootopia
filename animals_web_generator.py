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

def add_animals_info_and_implement_cards_into_html(animals_data):
    """
      Gets each animal information from json file based on name, location, diet and type, and returns it
      and make crds for each animal.
    """
    cards_output = ''
    for animal in animals_data:
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        location = animal.get("locations", [])[0]
        animal_type = characteristics.get("type")
        cards_output += '<li class="cards__item">'
        if "name" in animal:
            cards_output += f"Name: {name}<br>\n"
        if "locations" in animal:
            cards_output += f"Location: {location}<br>\n"
        if "characteristics" in animal:
            if "diet" in characteristics:
                cards_output += f"Diet: {diet}<br>\n"
            if "type" in characteristics:
                cards_output += f"Type: {animal_type}<br>\n"
        cards_output += '</li>'

    return cards_output


def implement_json_into_html_file(cards_output):
    """
    reads the HTML template file by using reading flies method then replaces the string with
    each animals info and creates a new HTML file with modified information.
    """
    with open('animals_template.html', 'r') as html_file:
        animals_template = html_file.read()

    updated_html = animals_template.replace("__REPLACE_ANIMALS_INFO__", cards_output)
    with open('animals.html', 'w') as new_html_file:
        new_html_file.write(updated_html)


def main():
    """calls all functions inside the file and runs the generator-program"""
    animals_data = initialize_animals_data()
    cards_output = add_animals_info_and_implement_cards_into_html(animals_data)
    implement_json_into_html_file(cards_output)


if __name__ == "__main__":
    main()