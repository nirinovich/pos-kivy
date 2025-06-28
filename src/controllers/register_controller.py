class RegisterController:
    def __init__(self, view, user_model, app):
        self.view = view
        self.user_model = user_model
        self.app = app

    def handle_register(self, username, password, confirm_password):
        if not username or not password or not confirm_password:
            self.view.update_status("Please fill in all fields.")
            return
        if password != confirm_password:
            self.view.update_status("Passwords do not match.")
            return
        if self.user_model.add_user(username, password):
            self.view.update_status("Register successful!")
            self.app.show_login()
        else:
            self.view.update_status("Register failed, username may be taken")