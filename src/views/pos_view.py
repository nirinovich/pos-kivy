from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class POSView(BoxLayout):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20
        self.status_label = Label(
            text='Welcome to K\'iosk POS System',
            font_size='18sp',
            size_hint_y=0.2,
            halign='center'
        )
        self.setup_ui()

    def setup_ui(self):
        title = Label(
            text='K\'iosk POS Prototype',
            font_size='32sp',
            size_hint_y=0.6,
            halign='center'
        )
        title.bind(size=title.setter('text_size'))

        init_db_button = Button(
            text='Initialize Database',
            size_hint_y=0.2,
            font_size='18sp'
        )
        init_db_button.bind(on_press=self.on_init_db)

        self.status_label.bind(size=self.status_label.setter('text_size'))

        self.add_widget(title)
        self.add_widget(self.status_label)
        self.add_widget(init_db_button)

    def on_init_db(self, instance):
        if self.controller:
            self.controller.handle_init_db()

    def update_status(self, message):
        self.status_label.text = message