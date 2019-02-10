def test_signup_new_account(app):
    username = "user1"
    password = "test"
    app.james.james_ensure_user_exists(username, password)
