
def city_country(city, country):
    """Print string."""
    location = f"{city}, {country}"
    return location

def city_country_population(city, country, population=0):
    """Can I add a population to the function?"""
    location = f"{city}, {country}"
    if population:
        location += f" -population {population}"
    return location