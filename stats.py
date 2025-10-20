def count_words(text):
    return len(text.split())

def count_characters(text):
    character_dict = {}
    for char in text:
        if char.lower() not in character_dict:
            character_dict[char.lower()] = 0

        character_dict[char.lower()] += 1
    
    return character_dict

def sort_dictionary(dict):
    sorted_dictionary = []
    def sort_key(stuff):
        return stuff["num"]

    for key in dict:
        if key.isalpha():
            d = {"char" : key, "num" : dict[key]}
            sorted_dictionary.append(d)

    sorted_dictionary.sort(reverse=True, key=sort_key)
    return sorted_dictionary