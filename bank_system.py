from typing import List

class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Transfer money from account1 to account2 if both accounts are valid
        # and account1 has enough balance
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        # Deposit money into an account if it's valid
        if not (1 <= account <= self.n):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Withdraw money from an account if it's valid and has enough balance
        if not (1 <= account <= self.n):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


# Example usage
if __name__ == "__main__":
    bank = Bank([100, 200, 300])

    print("Withdraw from Account 1:", bank.withdraw(1, 50))     # True  → [50, 200, 300]
    print("Transfer from 2 → 3:", bank.transfer(2, 3, 100))     # True  → [50, 100, 400]
    print("Deposit into Account 3:", bank.deposit(3, 50))       # True  → [50, 100, 450]
    print("Withdraw too much:", bank.withdraw(1, 1000))         # False
    print("Invalid transfer:", bank.transfer(4, 1, 10))         # False

    # ✅ Quick self-checks
    assert bank.balance == [50, 100, 450], "Final balances do not match expected result"
    assert bank.withdraw(2, 50) == True, "Withdraw test failed"
    assert bank.deposit(1, 100) == True, "Deposit test failed"
    assert bank.transfer(1, 3, 50) == True, "Transfer test failed"

    print("\n All tests passed successfully!")
