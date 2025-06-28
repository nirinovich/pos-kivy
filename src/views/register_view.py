from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText, MDIconButton
from kivymd.uix.fitimage import FitImage
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.uix.widget import Widget

class RegisterView(MDBoxLayout):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'horizontal'

        # --- Left: Register Form ---
        form_box = MDBoxLayout(
            orientation='vertical',
            padding=[dp(50), dp(50), dp(50), dp(50)],
            spacing=dp(0),
            size_hint_x=0.5,
            md_bg_color=get_color_from_hex("#F5F6FA")
        )

        # Top bar: Back button + Title
        top_bar = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(56),
            spacing=dp(10)
        )
        back_btn = MDIconButton(
            icon="arrow-left",
            on_release=self.on_back
        )
        top_bar.add_widget(back_btn)
        top_bar.add_widget(MDLabel(
            text="Register to K'iosk",
            font_size='24sp',
            halign="left",
            valign="middle",
            size_hint_y=0.2,
            theme_text_color="Primary"
        ))
        top_bar.add_widget(Widget(size_hint_x=2))  # Spacer to push title to left
        form_box.add_widget(top_bar)

        # Spacer to push the input fields to vertical center
        form_box.add_widget(Widget(size_hint_y=1))

        # Centered input fields and button
        center_box = MDBoxLayout(
            orientation='vertical',
            spacing=dp(18),
            size_hint_y=None,
            height=dp(48)*3 + dp(18)*2 + dp(60)  # 3 fields + 2 spacings + button
        )

        self.status_label = MDLabel(
            text='',
            font_size='16sp',
            size_hint_y=None,
            height=dp(28),
            halign="center",
            theme_text_color="Primary"
        )
        center_box.add_widget(self.status_label)

        self.username_input = MDTextField(
            MDTextFieldHintText(text="Username"),
            theme_text_color="Secondary",
        )
        center_box.add_widget(self.username_input)

        self.password_input = MDTextField(
            MDTextFieldHintText(text="Password"),
            password=True,
            theme_text_color="Secondary",
        )
        center_box.add_widget(self.password_input)

        self.confirm_password_input = MDTextField(
            MDTextFieldHintText(text="Confirm Password"),
            password=True,
            theme_text_color="Secondary",
        )
        center_box.add_widget(self.confirm_password_input)

        # Register button centered
        self.register_button = MDButton(
            MDButtonIcon(icon="plus"),
            MDButtonText(text="Create account"),
            style="elevated",
            on_release=self.on_register,
            width=dp(220),
            pos_hint={"center_x": 0.5}
        )
        center_box.add_widget(self.register_button)

        form_box.add_widget(center_box)

        # Spacer to push the input fields to vertical center
        form_box.add_widget(Widget(size_hint_y=1))

        self.add_widget(form_box)

        # --- Right: Image ---
        self.image = FitImage(
            source="assets/login_image.jpg",
            size_hint_x=0.5,
        )
        self.add_widget(self.image)

    def on_register(self, instance):
        if self.controller:
            username = self.username_input.text.strip()
            password = self.password_input.text.strip()
            confirm_password = self.confirm_password_input.text.strip()
            self.controller.handle_register(username, password, confirm_password)

    def on_back(self, instance):
        if self.controller and self.controller.app and hasattr(self.controller.app, "show_login"):
            self.controller.app.show_login()

    def update_status(self, message):
        self.status_label.text = message