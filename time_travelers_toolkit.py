from datetime import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
from custom_module import generate_time_travel_message

current_datetime = dt.today().year
print(current_datetime)

base_cost = Decimal('1000')
random_year = randint(int(current_datetime), 10000)
cost_multiplier = abs(random_year - current_datetime)

time_travel_cost = base_cost * cost_multiplier

final_cost = round(time_travel_cost, 2)

destinations = ["France"]

random_destination = choice(destinations)

print(generate_time_travel_message(random_year, random_destination, final_cost))
