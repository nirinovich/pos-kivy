from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

class ProductView(BoxLayout):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 10

        # Title
        self.add_widget(Label(text="Product Management", font_size='24sp', size_hint_y=0.1))

        # Product list area with scroll
        self.product_list = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.product_list.bind(minimum_height=self.product_list.setter('height'))
        scroll = ScrollView(size_hint=(1, 0.4))
        scroll.add_widget(self.product_list)
        self.add_widget(scroll)

        # Form for add/edit
        form = GridLayout(cols=2, spacing=10, size_hint_y=0.2)
        form.add_widget(Label(text="Name:"))
        self.name_input = TextInput()
        form.add_widget(self.name_input)
        form.add_widget(Label(text="Price:"))
        self.price_input = TextInput(input_filter='float')
        form.add_widget(self.price_input)
        self.add_widget(form)

        # Action buttons
        btn_box = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.1)
        add_btn = Button(text="Add", on_press=self.on_add)
        edit_btn = Button(text="Edit", on_press=self.on_edit)
        delete_btn = Button(text="Delete", on_press=self.on_delete)
        btn_box.add_widget(add_btn)
        btn_box.add_widget(edit_btn)
        btn_box.add_widget(delete_btn)
        self.add_widget(btn_box)

        # Status
        self.status_label = Label(text="", size_hint_y=0.1)
        self.add_widget(self.status_label)

    def update_product_list(self, products):
        self.product_list.clear_widgets()
        if not products:
            self.product_list.add_widget(Label(text="No products yet."))
        else:
            for prod in products:
                btn = Button(
                    text=f"{prod[0]}: {prod[1]} - ${prod[2]:.2f}",
                    size_hint_y=None,
                    height=40,
                    on_press=lambda instance, p=prod: self.on_select(p)
                )
                self.product_list.add_widget(btn)

    def on_select(self, product):
        product_id, name, price = product
        if self.controller:
            self.controller.select_product(product_id, name, price)

    def set_form(self, name, price):
        self.name_input.text = name
        self.price_input.text = str(price)

    def on_add(self, instance):
        if self.controller:
            self.controller.add_product(self.name_input.text, self.price_input.text)

    def on_edit(self, instance):
        if self.controller:
            self.controller.edit_product(self.name_input.text, self.price_input.text)

    def on_delete(self, instance):
        if self.controller:
            self.controller.delete_product()

    def update_status(self, message):
        self.status_label.text = message