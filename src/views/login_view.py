from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd.uix.fitimage import FitImage 
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

class LoginView(MDBoxLayout):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'horizontal'  # Horizontal split

        # --- Left: Image ---
        self.image = FitImage(
            source="assets/login_image.jpg",  # Replace with your image path
            size_hint_x=0.5,
        )
        self.add_widget(self.image)

        # --- Right: Login Form ---
        form_box = MDBoxLayout(
            orientation='vertical',
            padding=[dp(50), dp(50), dp(50), dp(50)],
            spacing=dp(20),
            size_hint_x=0.5,
            md_bg_color=get_color_from_hex("#F5F6FA")
        )

        form_box.add_widget(MDLabel(
            text="Login to K'iosk",
            font_size='24sp',
            size_hint_y=0.2,
            halign="center"
        ))

        self.status_label = MDLabel(
            text='',
            font_size='16sp',
            size_hint_y=0.1,
            halign="center",
            theme_text_color="Primary"
        )
        form_box.add_widget(self.status_label)

        self.username_input = MDTextField(
            MDTextFieldHintText(text="Username"),
            theme_text_color="Secondary"
        )
        form_box.add_widget(self.username_input)

        self.password_input = MDTextField(
            MDTextFieldHintText(text="Password"),
            password=True
        )
        form_box.add_widget(self.password_input)

        grid = MDGridLayout(
            cols=2,
            spacing=dp(40),
            size_hint_y=None,
            height=dp(180)
        )

        grid.add_widget(
            MDButton(
                MDButtonIcon(icon="login"),
                MDButtonText(text="Login"),
                style="elevated",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                on_release=self.on_login
            )
        )

        grid.add_widget(
            MDButton(
                MDButtonIcon(icon="account-plus"),
                MDButtonText(text="Register"),
                style="elevated",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                on_release=self.on_register
            )
        )

        form_box.add_widget(grid)
        self.add_widget(form_box)

    def on_login(self, instance):
        if self.controller:
            username = self.username_input.text.strip()
            password = self.password_input.text.strip()
            self.controller.handle_login(username, password)

    def on_register(self, instance):
        if self.controller:
            self.controller.go_to_register()

    def update_status(self, message):
        self.status_label.text = message