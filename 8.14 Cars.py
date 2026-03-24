#Car function for my new Elantra!
def describe_car(make, model, **car_info):
    """Store information about a car in a dictionary."""
    car_info['make'] = make.title()
    car_info['model'] = model.title()
    return car_info

# Car details
car= describe_car('hyundai', 'elantra', color='gunmetal', 
                  leather_trim=True, year=2025, mileage=1055,)

# Printing the car 
print(f"I bought a vehicle last year. It has the following features:{car}")
