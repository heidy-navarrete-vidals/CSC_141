def describe_city(city_name, country = 'America'):
    """Display information about a city"""
    print(f"\n{city_name} is in {country}.")

describe_city('New York City')
describe_city('Los Angeles')
describe_city(city_name = 'Shibuya', country = 'Japan')