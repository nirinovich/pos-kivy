from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginView(BoxLayout):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        self.add_widget(Label(text="🔐 Login to K'iosk", font_size='24sp', size_hint_y=0.2))

        self.username_input = TextInput(hint_text='Username', multiline=False, size_hint_y=0.15)
        self.add_widget(self.username_input)

        self.password_input = TextInput(hint_text='Password', multiline=False, password=True, size_hint_y=0.15)
        self.add_widget(self.password_input)

        self.status_label = Label(text='', font_size='16sp', size_hint_y=0.1)
        self.add_widget(self.status_label)

        login_btn = Button(text='Login', size_hint_y=0.15, font_size='18sp')
        login_btn.bind(on_press=self.on_login)
        self.add_widget(login_btn)

    def on_login(self, instance):
        if self.controller:
            username = self.username_input.text.strip()
            password = self.password_input.text.strip()
            self.controller.handle_login(username, password)

    def update_status(self, message):
        self.status_label.text = message