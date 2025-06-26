from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from models.user import UserModel
from views.login_view import LoginView
from controllers.login_controller import LoginController
from views.dashboard_view import DashboardView  # <-- Add this import

class POSApp(App):
    def build(self):
        self.user_model = UserModel()
        # For demo: create a default user if none exists
        self.user_model.add_user("admin", "admin123")
        self.root_widget = BoxLayout()
        self.show_login()
        return self.root_widget

    def show_login(self):
        login_view = LoginView()
        login_controller = LoginController(login_view, self.user_model, self)
        login_view.controller = login_controller
        self.root_widget.clear_widgets()
        self.root_widget.add_widget(login_view)

    def show_dashboard(self):
        dashboard_view = DashboardView()
        self.root_widget.clear_widgets()
        self.root_widget.add_widget(dashboard_view)

# Run the application
if __name__ == '__main__':
    print("🚀 Starting K'iosk...")
    print("=" * 40)
    
    # Start the Kivy app
    POSApp().run()