class ProductController:
    def __init__(self, product_model, category_model, app=None):
        self.product_model = product_model
        self.category_model = category_model
        self.app = app
        self.product_view = None
        self.category_view = None
        self.selected_id = None

    def set_view(self, view):
        self.product_view = view

    def set_category_view(self, view):
        self.category_view = view

    # --- Product logic ---
    def refresh_products(self):
        products = self.product_model.get_all()
        if self.product_view:
            self.product_view.update_product_list(products)

    def add_product(self, name, price, category_name):
        if not name or not price or not category_name or category_name == "No Category":
            self.product_view.update_status("All fields required.")
            return
        categories = self.category_model.get_all()
        category_id = next((cat[0] for cat in categories if cat[1] == category_name), None)
        if category_id is None:
            self.product_view.update_status("Invalid category.")
            return
        self.product_model.add(name, float(price), category_id)
        self.refresh_products()
        self.product_view.update_status("Product added.")

    def select_product(self, product_id, name, price, category):
        self.selected_id = product_id
        if self.product_view:
            self.product_view.set_form(name, price, category)

    def edit_product(self, name, price, category_name):
        if self.selected_id is None:
            self.product_view.update_status("Select a product to edit.")
            return
        categories = self.category_model.get_all()
        category_id = next((cat[0] for cat in categories if cat[1] == category_name), None)
        if category_id is None:
            self.product_view.update_status("Invalid category.")
            return
        self.product_model.update(self.selected_id, name, float(price), category_id)
        self.refresh_products()
        self.product_view.update_status("Product updated.")

    def delete_product(self):
        if self.selected_id is None:
            self.product_view.update_status("Select a product to delete.")
            return
        self.product_model.delete(self.selected_id)
        self.selected_id = None
        self.refresh_products()
        self.product_view.update_status("Product deleted.")

    # --- Category logic ---
    def refresh_categories(self):
        categories = self.category_model.get_all()
        if self.product_view:
            self.product_view.update_category_spinner(categories)
        if self.category_view:
            self.category_view.update_category_list(categories)

    def add_category(self, name):
        if not name:
            self.category_view.update_status("Category name required.")
            return
        self.category_model.add(name)
        self.refresh_categories()
        self.category_view.update_status("Category added.")

    # --- Navigation ---
    def show_category_page(self):
        from views.product_view import CategoryView
        category_view = CategoryView(controller=self)
        self.set_category_view(category_view)
        self.app.root_widget.clear_widgets()
        self.app.root_widget.add_widget(category_view)

    def show_product_page(self):
        from views.product_view import ProductView
        product_view = ProductView(controller=self)
        self.set_view(product_view)
        self.app.root_widget.clear_widgets()
        self.app.root_widget.add_widget(product_view)