pet_01 = {'type': 'cat',
          'owner': 'heidy'}
pet_02 = {'type': 'cat',
          'owner': 'daniel'}
pet_03 = {'type': 'cat',
          'owner': 'jennifer'}

pets = [pet_01, pet_02, pet_03]
for pet in pets:
    print(f"\n{pet}")
    for key, value in pet.items():
        print(f"\n{key}: {value}")