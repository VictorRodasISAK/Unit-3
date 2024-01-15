# test_quiz_036.py
from Quiz_036 import Account


def test_empty_account():
    new_account = Account()
    assert new_account.balance == 0
    assert new_account.holder_name == ""
    assert new_account.holder_email == ""
    numbers = new_account.numbers
    assert isinstance(numbers, list)
    account_number = new_account.get_account_no().split('-')
    assert len(account_number) == 3 and len(account_number[1]) == 5 and len(account_number[2]) == 1


def test_create_account():
    new_a = Account()
    assert new_a.get_balance() == 0
    assert new_a.set_holder_name(name="bob") == "Holder's name is Bob"
    assert new_a.set_holder_email(email="bob@xy.z") == "Holder's email is bob@xy.z"
    assert new_a.deposit(numbers=100) == "New balance: 100 USD"
