from kivy.app import App
from models.database import POSDatabase
from views.pos_view import POSView
from controllers.pos_controller import POSController

class POSApp(App):
    def build(self):
        model = POSDatabase()
        view = POSView()
        controller = POSController(view, model)
        view.controller = controller
        self.title = "K'iosk POS Prototype"
        return view

# Run the application
if __name__ == '__main__':
    print("🚀 Starting K'iosk...")
    print("=" * 40)
    
    # Start the Kivy app
    POSApp().run()