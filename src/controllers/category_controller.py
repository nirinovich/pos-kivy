from models.category import CategoryModel  # adjust import as needed

class CategoryController:
    def __init__(self, view):
        self.view = view

    def add_category(self, name):
        # Add logic to save to DB
        if not name.strip():
            self.view.update_status("Category name cannot be empty.")
            return
        # Example: Category.create(name)
        self.view.update_status(f"Added category: {name}")
        self.refresh_categories()

    def refresh_categories(self):
        # Fetch categories from DB
        # Example: categories = Category.get_all()
        categories = []  # Replace with real fetch
        self.view.update_category_list(categories)