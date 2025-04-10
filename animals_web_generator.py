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




def serialize_animal_info(animals_data):
    """
      Gets each animal information from json file based on name, location, diet and type, and returns it
      and make crds for each animal.
    """
    selected_skin_type = get_filter(animals_data)
    cards_output = ''
    name = animals_data.get("name")
    characteristics = animals_data.get("characteristics", {})
    diet = characteristics.get("diet")
    location = animals_data.get("locations", [])[0]
    animal_type = characteristics.get("type")
    skin_type = characteristics.get("skin_type")
    cards_output += '<li class="cards__item">'
    if "name" in animals_data:
        cards_output += f"<div class=\"card__title\">{name}</div>"
        cards_output += "<div class =\"card__text\">"
        cards_output += "<ul>"
    if "characteristics" in animals_data:
        if "diet" in characteristics:
            cards_output += f"<li><strong>Diet:</strong> {diet}</li>\n"
    if "locations" in animals_data:
        cards_output += f"<li><strong>Location:</strong> {location}</li>\n"
    if "characteristics" in animals_data:
        if "type" in characteristics:
            cards_output += f"<li><strong>Type:</strong> {animal_type}</li>\n"
        if "skin_type" in characteristics:
            cards_output += f"<li><strong>Type:</strong> {skin_type}</li>\n"
    cards_output += '</ul></div></li>'

    return cards_output


def serialize_all_animals_info(animals_data):

    output = []
    for animal_obj in animals_data:
        output.append(serialize_animal_info(animal_obj))
    return "".join(output)


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


def get_filter(animals_data):
    """"""
    skin_types = set([animal.get("characteristics", {}).get("skin_type") for animal in animals_data])
    print("open available skin types: ", ", ".join(skin_types))
    selected_skin_type = input("Enter the skin type from the list above: ")
    return selected_skin_type

def main():
    """calls all functions inside the file and runs the generator-program"""
    animals_data = initialize_animals_data()
    cards_output = serialize_all_animals_info(animals_data)
    implement_json_into_html_file(cards_output)


if __name__ == "__main__":
    main()