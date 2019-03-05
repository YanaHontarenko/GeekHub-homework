# Describe with the help of classes any known to you process or system.
# Example: cooking, employee interaction in a company, a zoo, a motor, etc.
# At least once it is necessary to use inheritance, private method and (or) private attribute.
# Each module, class, public method and function (if you use) should have a docstring.
# For public methods and __init __ (), specify the type of incoming and return data, if possible.
from _bank import Bank, BankWithStock, BankWithStorage

def main(first: str, second: str, third: str):
    simple_bank = Bank(first)
    simple_bank.openBank()
    if simple_bank.is_open:
        print("Simple bank still open")
    simple_bank.closeBank()

    bank_with_storage = BankWithStorage(second)
    bank_with_storage.openBank(1000)
    bank_with_storage.add_to_storage(400.45)
    bank_with_storage.add_to_storage(1000)
    bank_with_storage.closeBank()

    bank_with_stock = BankWithStock(third)
    bank_with_stock.openBank(1000)
    bank_with_stock.cash_credit(400)
    bank_with_stock.cash_credit(1000)
    bank_with_stock.closeBank()


if __name__ == '__main__':
    main("Simple", "Cool", "Great")
