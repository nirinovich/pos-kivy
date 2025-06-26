class CategoryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def refresh_categories(self):
        categories = self.model.get_all()
        self.view.update_category_list(categories)

    def add_category(self, name):
        if not name.strip():
            self.view.update_status("Category name required.")
            return
        success = self.model.add(name.strip())
        if success:
            self.view.update_status("Category added.")
        else:
            self.view.update_status("Category already exists.")
        self.refresh_categories()

    def delete_category(self, category_id):
        self.model.delete(category_id)
        self.refresh_categories()
        self.view.update_status("Category deleted.")