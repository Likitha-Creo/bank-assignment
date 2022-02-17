class Bank:
    def __init__(self, balance):
        self.balance = balance

first_atm = Bank(100)
second_atm = Bank(50)

class User:

    def __init__(self, name, card_name, acc_type, balance, pin, trans_count, max_a):
        self.name = name
        self.card_name = card_name
        self.acc_type = acc_type
        self.balance = balance
        self.pin = pin
        self.trans_count = trans_count
        self.max_a = max_a

    def withdraw(self):

        amount = float(input("Enter the amount"))
        bank_name = input("From which atm you want to withdraw money? 1 or 2")
        if bank_name == "1":
            bank_name = first_atm
        else:
            bank_name = second_atm
        pin = int(input("Enter pin"))
        if self.trans_count < 3 and amount <= 10 and self.max_a <= 25 and \
                (self.acc_type == "Balance" or self.acc_type == "Credit"):
            if pin == self.pin:
                if self.balance >= amount:
                    self.balance -= amount
                    self.trans_count += 1
                    self.max_a += amount
                    bank_name.balance -= amount
                    return self.balance
                elif self.balance == 0:
                    return self.balance
                else:
                    print("Insufficient balance")
            else:
                print("Card name or pin doesn't match")
        else:
            print("Access denied")

    def pin_reset(self):

        if self.trans_count < 3:
            new_pin = int(input("Enter new pin"))
            new = new_pin
            count = 0
            while new_pin > 0:
                new_pin = new_pin // 10
                count = count + 1
            if count == 4:
                self.pin = new
                self.trans_count += 1
                return self.pin
            else:
                print("Enter a new four digit pin")
                return new
        else:
            print("Transaction limit exceeded this day")


if __name__ == "__main__":

    user_dict = {
        "tom" : User("Tom", "tom", "Balance", 30, 1239, 0, 0),
        "jerry" : User("Jerry", "jerry", "Balance", 16, 2345, 0, 0),
        "bheem" : User("Chota Bheem", "bheem", "Balance", 22, 3456, 0, 0),
        "chutki" : User("Chutki", "chutki", "Balance", 5, 4567, 0, 0),
        "raju" : User("Raju", "raju", "Balance", 10.62, 5678, 0, 0),
        "kalia" : User("Kalia", "kalia", "Balance", 0, 6789, 0, 0),
        "kirmada" : User("Kirmada", "kirmada", "Access Denied", 0, 7890, 0, 0),
        "little_singham" : User("Little Singham", "little", "Credit", 0, 8901, 0, 0)
    }
    while True:
            print("Enter the card name")
            card_name = input()
            if user_dict.get(card_name) is not None:
                user_dict.get(card_name).withdraw()
                print(user_dict.get(card_name).balance)
                print(user_dict.get(card_name).trans_count)
                if first_atm.balance <= 25:
                    first_atm.balance += 75
                if second_atm.balance <= 10:
                    second_atm.balance += 40
                new_bal1 = first_atm.balance
                new_bal2 = second_atm.balance
                print("new_bal1", new_bal1)
                print("new_bal2", new_bal2)
                print("Do you want to reset the pin? Y or N")
                choose = input()
                if choose == "Y":
                    user_dict.get(card_name).pin_reset()
                print("Do you want to continue ? Y or N")
                choice = input()
                if choice == "N":
                    break
            else:
                print("User not found !, please enter existing user")
