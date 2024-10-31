def build_profile(first, last, **user_info):
    """Display information about yourself."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Heidy', "Navarrete-Vidals", college='Albright', age='19', city='Reading')
print(user_profile)