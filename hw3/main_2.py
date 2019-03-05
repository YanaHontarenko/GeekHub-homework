# Describe with the help of classes any known to you process or system.
# Example: cooking, employee interaction in a company, a zoo, a motor, etc.
# At least once it is necessary to use inheritance, private method and (or) private attribute.
# Each module, class, public method and function (if you use) should have a docstring.
# For public methods and __init __ (), specify the type of incoming and return data, if possible.
# Use static method, method of the class and property.
from _bank import Bank, BankWithStorage, BankWithStock


def main():
    A = Bank('A')
    B = BankWithStock('B')
    C = BankWithStorage('C')

    print("Call static method")
    BankWithStock.printShedule()

    print("Call class method from BankWithStock")
    print(BankWithStock.double_counter_stock())
    print("In general counter - ", BankWithStock.COUNTER)
    D = BankWithStorage("D")
    print("Call class method from BankWithStorage")
    print(BankWithStorage.double_counter_storage())
    print("In general counter - ", BankWithStorage.COUNTER)
    print("In counter from BankWithStock- ", BankWithStock.COUNTER_WITH_STOCK)

if __name__ == '__main__':
    main()
