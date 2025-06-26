from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDButton, MDButtonText
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
            text="Login to K'iosk",
            font_size='24sp',
            size_hint_y=0.2,
            halign="center",
            theme_text_color="Primary"
        ))

        self.username_input = MDTextField(hint_text='Username', size_hint_y=0.15)
        self.add_widget(self.username_input)

        self.password_input = MDTextField(hint_text='Password', password=True, size_hint_y=0.15)
        self.add_widget(self.password_input)

        self.status_label = MDLabel(
            text='',
            font_size='16sp',
            size_hint_y=0.1,
            halign="center",
            theme_text_color="Primary"
        )
        self.add_widget(self.status_label)

        login_btn = MDButton(
            MDButtonText(text='Login'),
            style="elevated",
            size_hint_y=0.15,
            on_release=self.on_login
        )
        self.add_widget(login_btn)

    def on_login(self, instance):
        if self.controller:
            username = self.username_input.text.strip()
            password = self.password_input.text.strip()
            self.controller.handle_login(username, password)

    def update_status(self, message):
        self.status_label.text = message