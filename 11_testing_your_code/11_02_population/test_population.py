from population_function import city_country, city_country_population

def test_city_and_country():
    """Run test."""
    city_and_country = city_country('Shibuya', 'Japan')
    assert city_and_country == 'Shibuya, Japan'

def test_city_country_population():
    """Test population."""
    population = city_country_population('Shibuya', 'Japan', population=30_000_000)
    assert population == 'Shibuya, Japan -population 30000000'