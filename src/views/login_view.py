from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd.uix.fitimage import FitImage 
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

class LoginView(MDBoxLayout):
    # ...existing code from src/views/login_view.py...
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'horizontal'  # Horizontal split
        # ...rest of the code...
    # ...rest of the class...
