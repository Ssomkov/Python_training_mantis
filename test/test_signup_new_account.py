import string
import random


def random_username(prefix, max_length):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


def test_signup_new_account(app):
    username = random_username("user_", 10)
    email = username + "@localhost"
    password = "test"
    app.james.james_ensure_user_exists(username, password)
    app.signup.new_user(username, password, email)
    assert app.soap.can_login(username, password)
