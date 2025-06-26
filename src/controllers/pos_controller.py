class POSController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def handle_init_db(self):
        try:
            self.model.initialize()
            count = self.model.get_product_count()
            self.view.update_status(f"✅ Database initialized!\nProducts in DB: {count}")
        except Exception as e:
            self.view.update_status(f"❌ Error: {str(e)}")