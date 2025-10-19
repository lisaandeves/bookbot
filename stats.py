def count_words(text):
    return len(text.split())

def count_characters(text):
    character_dict = {}
    for char in text:
        if char.lower() not in character_dict:
            character_dict[char.lower()] = 0

        character_dict[char.lower()] += 1
    
    return character_dict