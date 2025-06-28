from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

class LoginView(MDBoxLayout):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'
        self.padding = [dp(50), dp(50), dp(50), dp(50)]
        self.spacing = dp(20)
        self.md_bg_color = get_color_from_hex("#F5F6FA")

        self.add_widget(MDLabel(
            text = "Login to K'iosk",
            font_size = '24sp',
            size_hint_y = 0.2,
            halign = "center"
        ))

        self.status_label = MDLabel(
            text = '',
            font_size = '16sp',
            size_hint_y = 0.1,
            halign = "center",
            theme_text_color = "Primary"
        )
        self.add_widget(self.status_label)

        self.username_input = MDTextField(
            MDTextFieldHintText(text = "Username",),
            theme_text_color = "Secondary"

        )
        
        self.add_widget(self.username_input)

        self.password_input = MDTextField(
            MDTextFieldHintText(text = "Password"),
            passwor = True)
        
        self.add_widget(self.password_input)

        grid = MDGridLayout(
            cols = 2, 
            spacing = dp(40), 
            size_hint_y = None, 
            height = dp(180))

        grid.add_widget(
            MDButton(
                MDButtonIcon(icon = "login"),
                MDButtonText(text = "Login"),
                style = "elevated",
                pos_hint = {"center_x": 0.5, "center_y": 0.5},
                on_release = self.on_login
            )
        )
        
        grid.add_widget(
            MDButton(
                MDButtonIcon(icon = "account-plus"),
                MDButtonText(text = "Register"),
                style = "elevated",
                pos_hint = {"center_x": 0.5, "center_y": 0.5},
            )
        )

        self.add_widget(grid)

    def on_login(self, instance):
        if self.controller:
            username = self.username_input.text.strip()
            password = self.password_input.text.strip()
            self.controller.handle_login(username, password)

    def update_status(self, message):
        self.status_label.text = message