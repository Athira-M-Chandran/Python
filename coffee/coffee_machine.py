import sys


class coffee:
    def __init__(self, drink, resource, machine):
        self.drink = drink
        self.machine = machine
        self.resource = resource

    def turn(self, condition):
        try:
            if condition.lower() == 'off':
                sys.exit("Process ends!")
            elif condition.lower() == 'on':
                return coffee.report(self)
            else:
                sys.exit("Invalid Entry!")
        except Exception as e:
            return str(e)

    def report(self):
        try:
            for key, value in self.resource.items():
                print(f"{key} : {value}")
                print(' ')
        except Exception as e:
            return str(e)

    def resources(self):
        try:
            for i in self.machine.items():
                if i[0] == 'Money':
                    break
                for j in self.resource.items():
                    if i[0] == j[0]:
                        if i[1] >= j[1]:
                            flag = 1
                        else:
                            return "Sorry there is not enough " + i[0]
            return "Enough resources available"
        except Exception as e:
            return e

    def coinlist(self,coin):
        try:
            coin_list = []
            coin_count = 0

            for i in range(coin):
                coin_type = input("Enter coin type for : quarters/dimes/nickles/pennies? ")
                enter_coin = int(input("Enter no. of coins of " + coin_type + " : "))
                coin_count += enter_coin
                if coin_count > coin:
                    print('Invalid Entry')
                    break
                if coin_type == "quarters":
                    coin_list.append(enter_coin * 0.25)
                elif coin_type == "dimes":
                    coin_list.append(enter_coin * 0.10)
                elif coin_type == "nickles":
                    coin_list.append(enter_coin * 0.05)
                elif coin_type == "pennies":
                    coin_list.append(enter_coin * 0.01)
                if coin_count == coin:
                    return coin_list
        except TypeError as tp:
            return tp
        except Exception as e:
            return e

    def transaction(self, money):
        try:
            self.machine.update({'Money': money})
            
            if self.resource['Money'] > self.machine['Money']:
                self.machine.update({'Money': 0})
                return "Sorry that's not enough money. Money refunded."

            elif self.resource['Money'] < self.machine['Money']:
                print("Here is $" + str(self.machine['Money'] - self.resource['Money']) + " dollars in change.")
                return coffee.make(self)

            else:
                print('$' + str(self.machine['Money']) + ' accepted')
                self.machine.update({'Money': money})

                return coffee.make(self)
        except Exception as e:
            return e

    def make(self):
        try:
            for i in self.machine.items():
                for j in self.resource.items():
                    if i[0] == j[0]:
                        self.machine.update({i[0]: i[1] - j[1]})
            self.machine.update({"Money": 0})

            return "Here is your " + self.drink + " Enjoy!"
        except Exception as e:
            return e
