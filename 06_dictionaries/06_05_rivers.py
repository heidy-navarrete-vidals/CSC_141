rivers = {'amazon river': 'peru',
          'nile river': 'egypt',
          'mississippi river': 'america'}
for river, country in rivers.items():
    print(f"\nThe {river.title()} belongs in {country.title()}.")
    print(f"River name: {river.title()}")
    print(f"Country name: {country.title()}")