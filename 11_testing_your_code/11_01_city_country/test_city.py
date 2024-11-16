from city_functions import city_country

def test_city_and_country():
    """Run test."""
    city_and_country = city_country('Shibuya', 'Japan')
    assert city_and_country == 'Shibuya, Japan'