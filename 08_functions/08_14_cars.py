def make_car(model, manufacturer, **car_info):
    """Print information about a car."""
    car_info['model'] = model
    car_info['manufacturer'] = manufacturer
    return car_info

car_profile = make_car('outback', 'Toyota', color='red', tire_type='snow')
print(car_profile)