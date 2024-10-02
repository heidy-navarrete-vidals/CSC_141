cities = {
    'reading': {
        'country': 'america',
        'population': '95K',
        'fact': 'The fourth largest city in Pennsylvania.',
        },

    'philadelphia': {
        'country': 'america',
        'population': '1.6M',
        'fact': 'The cheesteak was invented here.',
        },

    'lancaster': {
        'country': 'america',
        'population': '50K',
        'fact': 'President James Buchanan lived here.',
    },
}

for city, city_info in cities.items():
    print(f"\nCity Name: {city.title()}")
    
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")