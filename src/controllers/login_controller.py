class LoginController:
    def __init__(self, view, user_model, app):
        self.view = view
        self.user_model = user_model
        self.app = app

    def handle_login(self, username, password):
        if not username or not password:
            self.view.update_status("Please enter both username and password.")
            return
        if self.user_model.verify_user(username, password):
            self.view.update_status("Login successful!")
            self.app.show_dashboard()
        else:
            self.view.update_status("Invalid credentials.")