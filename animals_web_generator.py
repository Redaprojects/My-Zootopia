import data_fetcher

def initialize_animals_data(name):
    """
    defines animals data from the api and returns it as a list.
    """
    animals_data = data_fetcher.fetch_data(name)
    if isinstance(animals_data, dict):
        animals_data = [animals_data]
    return animals_data


def serialize_animal_info(animals_data, selected_skin_type):
    """
      Gets each animal information from api based on name, location, diet, skin_type and type, then returns all infos as output
      besides it creates a card for each animal.
    """
    cards_output = ''
    name = animals_data.get("name")
    characteristics = animals_data.get("characteristics", {})
    diet = characteristics.get("diet")
    location = animals_data.get("locations", [])[0]
    animal_type = characteristics.get("type")
    #skin_type = characteristics.get("skin_type", {}).strip().lower()
    skin_type = characteristics.get("skin_type", "").strip().lower()
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
            if not skin_type or skin_type != selected_skin_type:
                return ""
            cards_output += f"<li><strong>Skin Type:</strong> {skin_type}</li>\n"
    cards_output += '</ul></div></li>'

    return cards_output


def serialize_all_animals_info(animals_data):
    """
    creates an empty list and iterates through over each animal then adds all infos about every one
    then returns strings inside the list.
    """
    selected_skin_type = get_skin_type_filter(animals_data)
    output = []
    for animal_obj in animals_data:
        output.append(serialize_animal_info(animal_obj, selected_skin_type))
    return "".join(output)


def render_no_animal_found(name):
    """returns the head incase there is no animal name found"""
    return f"<h2>The animal '{name}' doesn't exist.</h2>"


def implement_api_data_into_html_file(cards_output):
    """
    reads the HTML template file by using reading flies method then replaces the string with
    each animals info and creates a new HTML file with modified information.
    """
    with open('animals_template.html', 'r') as html_file:
        animals_template = html_file.read()

    updated_html = animals_template.replace("__REPLACE_ANIMALS_INFO__", cards_output)
    with open('animals.html', 'w') as new_html_file:
        new_html_file.write(updated_html)


def get_skin_type_filter(animals_data):
    """
    Creates a set of lowercase skin types from animals_data and asks the user to select one.
    Returns the selected skin type in lowercase.
    """
    skin_types = set(
        animal.get("characteristics", {}).get("skin_type", "").lower()
        for animal in animals_data
        if animal.get("characteristics", {}).get("skin_type")
    )

    print("Available skin types:", ", ".join(skin_types))

    while True:
        selected_skin_type = input("Enter the skin type from the list above: ").lower().strip()
        if selected_skin_type in skin_types:
            return selected_skin_type
        else:
            print("Invalid skin type. Please choose one from the list.")


def main():
    """
    gets animal name from the user, calls all functions inside the program only if the animal name
    has been found in api information and runs the generator-program otherwise it stops the program.
    """
    name = input('Enter the animal name for ex.(cheetah): ').strip()
    animals_data = initialize_animals_data(name)
    if not animals_data:
        cards_output = render_no_animal_found(name)
        implement_api_data_into_html_file(cards_output)
        return

    cards_output = serialize_all_animals_info(animals_data)
    implement_api_data_into_html_file(cards_output)


if __name__ == "__main__":
    main()