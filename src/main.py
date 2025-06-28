import sqlite3

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from models.user import UserModel
from models.category import CategoryModel
from models.product import ProductModel

from controllers.login_controller import LoginController
from controllers.product_controller import ProductController
from controllers.category_controller import CategoryController

from views.login_view import LoginView
from views.dashboard_view import DashboardView
from views.product_view import ProductView
from views.category_view import CategoryView
from views.register_view import RegisterView


class POSApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"  # or "Dark"
        self.theme_cls.primary_palette = "Blue"  # or "Indigo", "Teal", etc.
        self.theme_cls.primary_hue = "500"
        
        self.conn = sqlite3.connect("pos.db", check_same_thread=False, timeout=10)        
        self.category_model = CategoryModel(self.conn)
        self.product_model = ProductModel(self.conn)
        self.user_model = UserModel(self.conn)

        self.login_controller = LoginController(view=None, user_model=self.user_model, app=self)
        self.product_controller = ProductController(self.product_model, self.category_model, app=self)
        
        self.root_widget = MDBoxLayout()  # Use MDBoxLayout for proper theming
        self.show_login()
        return self.root_widget
    
    def show_login(self):
        user_model = UserModel(self.conn)
        login_view = LoginView()  # Create the view first, without controller
        login_controller = LoginController(view=login_view, user_model=user_model, app=self)
        login_view.controller = login_controller  # Set the controller on the view
        
        self.root_widget.clear_widgets()
        self.root_widget.add_widget(login_view)

    def show_dashboard(self):
        dashboard_view = DashboardView(controller=self)
        self.root_widget.clear_widgets()
        self.root_widget.add_widget(dashboard_view)

    def show_category_management(self):
        # Properly wire up the category MVC
        category_controller = CategoryController(self.category_model, None)  # View will be set after creation
        category_view = CategoryView(category_controller)
        category_controller.view = category_view

        self.root_widget.clear_widgets()
        self.root_widget.add_widget(category_view)

    def show_register(self):
        from controllers.register_controller import RegisterController
        from views.register_view import RegisterView

        register_view = RegisterView()  # Create the view first
        register_controller = RegisterController(view=register_view, user_model=self.user_model, app=self)
        register_view.controller = register_controller

        self.root_widget.clear_widgets()
        self.root_widget.add_widget(register_view)


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
    print("=" * 60)
    POSApp().run()
