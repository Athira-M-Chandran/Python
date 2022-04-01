import coffee.coffee_machine
import coffee_machine

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
drink = input("What would you like? (espresso/latte/cappuccino): ")
if drink == 'espresso':
    resource = {'Water': 300, 'Milk': 200, 'Coffee': 100, 'Money': 2}
elif drink == 'latte':
    resource = {'Water': 150, 'Milk': 150, 'Coffee': 50, 'Money': 2.50}
elif drink == 'cappuccino':
    resource = {'Water': 200, 'Milk': 300, 'Coffee': 150, 'Money': 3}
else:
    print("Sorry not in menu")
machine = {'Water': 1000, 'Milk': 500, 'Coffee': 500, 'Money': 0}
make_coffee = coffee_machine.coffee(drink, resource, machine)

# 2. Turn off the Coffee Machine by entering “off” to the prompt
condition = input("Enter 'on' to continue 'off' to turnoff machine : ")
make_coffee.turn(condition)

#3. Print report.

#make_coffee.report()
# 4. Check resources sufficient?

print(make_coffee.resources())

# 5. Process coins.


coin = int(input("Enter number of coins: "))
coin_list = make_coffee.coinlist(coin)

# 6. Check transaction successful?
if coin_list:
    print(make_coffee.transaction(sum(coin_list)))

# 7. Make Coffee.

#print(make_coffee.make())
