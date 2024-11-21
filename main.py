#1. define your function
def pizza_price():

  #2. Ask customer what they want
  requested_toppings = imput("""""")
  print(f"you reqested: {requested_toppings})
  
base_price = 15
toppings_price = 0
calculated_toppings = []
# tomatoes (+$1.50),
# onions (+$1.25),
# pineapple (+$3.50), 
# mushrooms (+$3.75), and
# avocado (+$0.40).

for toppings in requested_toppings:

# skip toppings we've already calculated
if topping in calculated_toppings:
  continue
  
if topping == "T":
    toppings_price += 1.5

if topping == "O":
  toppings_price += 1.25

if topping == "P":
  toppings_price += 3.5

if topping == "M":
  toppings_price += 3.75

if topping == "A":
  toppings_price += .40

# add topping to calculated list 
calculated_toppiings += topping

total_price = base_price + toppings_price

if total_price > 20:
    total_price = total_price * .95

total_price = round(total_price, 2)

print(total_price)

pizza_price()
