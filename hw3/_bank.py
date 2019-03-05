"""Bank."""


class Bank:
    """Describe job of primitive bank."""
    COUNTER = 0

    def __init__(self, name: str):
        """Create named bank"""
        self.name = name
        self.is_open = False
        Bank.COUNTER += 1

    def openBank(self):
        """Open bank"""
        self.is_open = True
        print(f'We open {self.name} bank.')        

    def closeBank(self):
        """Close bank"""
        self.is_open = False
        print(f'Now {self.name} bank is close.')

    @staticmethod
    def printShedule():
        print("We work from 8:00 to 18-00.\nIn Sunday from 8:00 to 16:00")


class BankWithStorage(Bank):
    """Describe job of bank which have storage of the money"""
    COUNTER_WITH_STORAGE = 0

    def __init__(self, name: str):
        super(BankWithStorage, self).__init__(name)
        BankWithStorage.COUNTER_WITH_STORAGE += 1

    def openBank(self, limit: int):
        """Open bank with storage and storage_limit"""
        super(BankWithStorage, self).openBank()
        self.storage = 0
        self._storage_limit = limit
        print(f'We open {self.name} bank. In our bank you can put money in storage. ({self._storage_limit} - storage_limit)')

    def closeBank(self):
        """Close bank and nullification storage"""
        super(BankWithStorage, self).closeBank()
        print(f'({self._empty_storage} - count of created banks)')

    def add_to_storage(self, money: float):
        """Take money to storage if enough space for it"""
        if self.storage + money > self._storage_limit:
            print("Sorry, it is too much for out storage. We can take from you only ", self._storage_limit - self.storage)
        else:
            self.storage = self.storage + money
            print("We put in storage ", money)

    @classmethod
    def double_counter_storage(cls):
        cls.COUNTER_WITH_STORAGE *= 2
        return f'Now counter = {cls.COUNTER_WITH_STORAGE}'

    @property
    def _empty_storage(self):
        self.storage = 0
        return self.COUNTER


class BankWithStock(Bank):
    """Describe job of bank which have stock of money to gice you a credit"""
    COUNTER_WITH_STOCK = 0

    def __init__(self, name: str):
        super(BankWithStock, self).__init__(name)
        BankWithStock.COUNTER_WITH_STOCK += 1

    def openBank(self, stock: int):
        """Open bank with stock of money"""
        super(BankWithStock, self).openBank()
        self.stock_of_money = stock
        print(f'We open {self.name} bank. In our bank you can take cash credit.({self.stock_of_money} - stock_of_money)')

    def closeBank(self):
        """Close bank and nullification it stock of money"""
        super(BankWithStock, self).closeBank()
        print(f'({self._empty_stock} - count of created banks)')

    def cash_credit(self, amount: int):
        """Give credit if enough money for this in stock"""
        if self.stock_of_money < 0 or amount > self.stock_of_money:
            print("Sorry, we can`t give you that amount of money. In our stock only ", self.stock_of_money)
        else:
            self.stock_of_money = self.stock_of_money - amount
            print("We give amount ", amount)

    @classmethod
    def double_counter_stock(cls):
        cls.COUNTER_WITH_STOCK *= 2
        return f'Now counter = {cls.COUNTER_WITH_STOCK}'

    @property
    def _empty_stock(self):
        self.stock_of_money = 0
        return self.COUNTER
