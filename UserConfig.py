test_settings = {
    'Hi':'Greeting'
}

def add_setting (settings_dict, settings_pair):
    key = settings_pair[0].lower()
    value = settings_pair[1].lower()
    if key in settings_dict:
        return(f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    else:
        settings_dict.update({key:value})
        return(f"Setting '{key}' added with value '{value}' successfully!")
    

def update_setting (settings_dict, settings_pair):
    key = settings_pair[0].lower()
    value = settings_pair[1].lower()
    if key not in settings_dict:
        return(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")
    else:
        settings_dict.update({key:value})
        return(f"Setting '{key}' updated to '{value}' successfully!")

def delete_setting (settings_dict, settings_pair):
    key = settings_pair.lower()
    if key not in settings_dict:
        return("Setting not found!")
    else:
        del settings_dict[key]
        return(f"Setting '{key}' deleted successfully!")

def view_settings(settings_dict):
    if len(settings_dict) == 0:
        return("No settings available.")
    else:
        output = "Current User Settings:\n"
        for setting in settings_dict:
            capitalized_key = setting.capitalize()
            value = settings_dict[setting]
            output += f"{capitalized_key}: {value}\n"
        return output