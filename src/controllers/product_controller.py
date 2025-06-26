class ProductController:
    def __init__(self, model):
        self.model = model
        self.view = None
        self.selected_id = None

    def set_view(self, view):
        self.view = view

    def refresh_products(self):
        products = self.model.get_all()
        if self.view:
            self.view.update_product_list(products)

    def add_product(self, name, price):
        try:
            if not name or not price:
                self.view.update_status("Name and price required.")
                return
            price = float(price)
            self.model.add(name, price)
            self.view.update_status("Product added.")
            self.refresh_products()
        except Exception as e:
            self.view.update_status(f"Error: {e}")

    def select_product(self, product_id, name, price):
        self.selected_id = product_id
        if self.view:
            self.view.set_form(name, price)

    def edit_product(self, name, price):
        try:
            if self.selected_id is None:
                self.view.update_status("Select a product to edit.")
                return
            price = float(price)
            self.model.update(self.selected_id, name, price)
            self.view.update_status("Product updated.")
            self.refresh_products()
        except Exception as e:
            self.view.update_status(f"Error: {e}")

    def delete_product(self):
        try:
            if self.selected_id is None:
                self.view.update_status("Select a product to delete.")
                return
            self.model.delete(self.selected_id)
            self.view.update_status("Product deleted.")
            self.selected_id = None
            self.refresh_products()
        except Exception as e:
            self.view.update_status(f"Error: {e}")