full_dot = '●'
empty_dot = '○'

def create_character (name,strength,intelligence,charisma):
    #Verificar:
    if not isinstance(name, str):
        return("The character name should be a string")
    elif not name:
        return("The character should have a name")
    elif len(name) > 10:
        return("The character name is too long")
    elif " " in name:
        return("The character name should not contain spaces")
    elif not isinstance(strength, int) or not isinstance (intelligence, int) or not isinstance (charisma, int):
        return("All stats should be integers")
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return("All stats should be no less than 1")
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return("All stats should be no more than 4")
    elif strength + intelligence + charisma != 7:
        return("The character should start with 7 points")
    
    #Circle logic:
    circles = "○○○○○○○○○○"
    #Strength:
    strength_keep = circles[strength:]
    strength_replace = circles[:strength]
    circle_strength = ("●"*strength) + strength_keep
    #Intelligence:
    intel_keep = circles[intelligence:]
    intel_replace = circles[:intelligence]
    circle_intel = ("●"*intelligence) + intel_keep
    #Charisma:
    char_keep = circles[charisma:]
    char_replace = circles[:charisma]
    circle_char = ("●"*charisma) + char_keep

    return f'{name}\nSTR {circle_strength}\nINT {circle_intel}\nCHA {circle_char}'

create_character("John", 4, 2, 1)
