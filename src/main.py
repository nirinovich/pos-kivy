from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import sqlite3

from models.user import UserModel
from models.category import CategoryModel
from models.product import ProductModel
from controllers.login_controller import LoginController
from controllers.product_controller import ProductController
from views.login_view import LoginView
from views.dashboard_view import DashboardView
from views.product_view import ProductView

class POSApp(App):
    def build(self):
        self.conn = sqlite3.connect("pos.db", check_same_thread=False)
        self.category_model = CategoryModel(self.conn)
        self.product_model = ProductModel(self.conn)
        self.product_controller = ProductController(self.product_model, self.category_model, app=self)
        self.root_widget = BoxLayout()
        self.show_dashboard()
        return self.root_widget

    def show_dashboard(self):
        dashboard_view = DashboardView(controller=self)
        self.root_widget.clear_widgets()
        self.root_widget.add_widget(dashboard_view)

    def go_to_product_management(self):
        product_view = ProductView(controller=self.product_controller)
        self.product_controller.set_view(product_view)
        self.root_widget.clear_widgets()
        self.root_widget.add_widget(product_view)

    # Other navigation
    def go_to_new_sale(self):
        pass

    def go_to_reports(self):
        pass

    def go_to_settings(self):
        pass

# Run the application
if __name__ == '__main__':
    print("🚀 Starting K'iosk...")
    print("=" * 40)
    
    # Start the Kivy app
    POSApp().run()