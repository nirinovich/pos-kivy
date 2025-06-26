from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner

class ProductView(BoxLayout):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 10

        # Top bar with back button
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=0.08, height=40, spacing=10)
        back_btn = Button(text="<", size_hint=(None, None), size=(40, 40), on_press=self.on_back)
        back_btn.background_color = (0.3, 0.3, 0.3, 1)
        top_bar.add_widget(back_btn)
        top_bar.add_widget(Label(text="Product Management", font_size='22sp', bold=True, halign='left'))
        self.add_widget(top_bar)

        # Divider
        self.add_widget(Label(
            text="─" * 60,
            font_size='16sp',
            size_hint_y=0.05,
            color=(.7, .7, .7, 1)
        ))

        # Product list area with scroll
        self.selected_btn = None
        self.selected_product = None
        self.product_list = GridLayout(cols=1, spacing=8, size_hint_y=None)
        self.product_list.bind(minimum_height=self.product_list.setter('height'))
        scroll = ScrollView(size_hint=(1, 0.28))
        scroll.add_widget(self.product_list)
        self.add_widget(scroll)

        # Form for add/edit
        form = GridLayout(cols=2, spacing=10, size_hint_y=0.18)
        form.add_widget(Label(text="Name:", font_size='16sp'))
        self.name_input = TextInput(font_size='16sp', multiline=False)
        form.add_widget(self.name_input)
        form.add_widget(Label(text="Price:", font_size='16sp'))
        self.price_input = TextInput(font_size='16sp', multiline=False, input_filter='float')
        form.add_widget(self.price_input)
        form.add_widget(Label(text="Category:", font_size='16sp'))
        self.category_spinner = Spinner(text="Select Category", font_size='16sp')
        form.add_widget(self.category_spinner)
        self.add_widget(form)

        # Action buttons
        btn_box = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=0.12)
        add_btn = Button(text="Add", background_color=(0.2, 0.7, 0.2, 1), font_size='16sp', on_press=self.on_add)
        edit_btn = Button(text="Edit", background_color=(0.2, 0.4, 0.8, 1), font_size='16sp', on_press=self.on_edit)
        delete_btn = Button(text="Delete", background_color=(0.8, 0.2, 0.2, 1), font_size='16sp', on_press=self.on_delete)
        btn_box.add_widget(add_btn)
        btn_box.add_widget(edit_btn)
        btn_box.add_widget(delete_btn)
        self.add_widget(btn_box)

        # Category management button
        cat_btn = Button(text="Manage Categories", size_hint_y=0.08, font_size='15sp', on_press=self.on_manage_categories)
        self.add_widget(cat_btn)

        # Status
        self.status_label = Label(text="", size_hint_y=0.08, font_size='15sp', color=(0.5,0.2,0.2,1))
        self.add_widget(self.status_label)

        # Initial load
        if self.controller:
            self.controller.set_view(self)
            self.controller.refresh_products()
            self.controller.refresh_categories()

    def update_product_list(self, products):
        self.product_list.clear_widgets()
        self.selected_btn = None
        self.selected_product = None
        if not products:
            self.product_list.add_widget(Label(text="No products yet.", font_size='15sp'))
        else:
            for prod in products:
                btn = Button(
                    text=f"{prod[0]}: {prod[1]} - ${prod[2]:.2f} [{prod[3] if prod[3] else 'No Category'}]",
                    size_hint_y=None,
                    height=44,
                    font_size='16sp',
                    background_normal='',
                    background_color=(0.95, 0.95, 0.95, 1),
                    color=(0,0,0,1),
                    on_press=lambda instance, p=prod: self.on_select(instance, p)
                )
                self.product_list.add_widget(btn)

    def update_category_spinner(self, categories):
        self.category_spinner.values = [cat[1] for cat in categories]
        if categories:
            self.category_spinner.text = categories[0][1]
        else:
            self.category_spinner.text = "No Category"

    def on_select(self, btn, product):
        if self.selected_btn:
            self.selected_btn.background_color = (0.95, 0.95, 0.95, 1)
        btn.background_color = (0.7, 0.85, 1, 1)
        self.selected_btn = btn
        self.selected_product = product
        product_id, name, price, category = product
        self.name_input.text = name
        self.price_input.text = str(price)
        self.category_spinner.text = category if category else "No Category"
        if self.controller:
            self.controller.select_product(product_id, name, price, category)

    def set_form(self, name, price, category):
        self.name_input.text = name
        self.price_input.text = str(price)
        self.category_spinner.text = category

    def on_add(self, instance):
        if self.controller:
            self.controller.add_product(
                self.name_input.text,
                self.price_input.text,
                self.category_spinner.text
            )

    def on_edit(self, instance):
        if self.controller:
            self.controller.edit_product(
                self.name_input.text,
                self.price_input.text,
                self.category_spinner.text
            )

    def on_delete(self, instance):
        if self.controller:
            self.controller.delete_product()

    def update_status(self, message):
        self.status_label.text = message

    def on_back(self, instance):
        if self.controller and self.controller.app and hasattr(self.controller.app, "show_dashboard"):
            self.controller.app.show_dashboard()

    def on_manage_categories(self, instance):
        if self.controller:
            self.controller.show_category_page()

class CategoryView(BoxLayout):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'
        self.padding = [20, 20, 20, 20]
        self.spacing = 15

        # --- Top bar ---
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        back_btn = Button(text="<", size_hint=(None, None), size=(40, 40), on_press=self.on_back,
                          background_color=(0.2, 0.2, 0.2, 1))
        top_bar.add_widget(back_btn)
        top_bar.add_widget(Label(text="Category Management", font_size='24sp', bold=True, halign='center', valign='middle'))
        top_bar.add_widget(Label(size_hint_x=None, width=40))  # Spacer for symmetry
        self.add_widget(top_bar)

        # --- Category list ---
        self.add_widget(Label(text="Categories:", font_size='18sp', size_hint_y=None, height=30, halign='left', valign='middle'))

        scroll = ScrollView(size_hint=(1, 0.35))
        self.category_list = GridLayout(cols=1, spacing=8, size_hint_y=None, padding=[0, 10, 0, 10])
        self.category_list.bind(minimum_height=self.category_list.setter('height'))
        scroll.add_widget(self.category_list)
        self.add_widget(scroll)

        # --- Add category form ---
        form = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        form.add_widget(Label(text="New Category:", font_size='16sp', size_hint_x=0.4, halign='right', valign='middle'))
        self.new_cat_input = TextInput(font_size='16sp', multiline=False, size_hint_x=0.6)
        form.add_widget(self.new_cat_input)
        self.add_widget(form)

        add_btn = Button(text="Add Category", background_color=(0.2, 0.5, 0.2, 1), font_size='16sp',
                         size_hint=(None, None), size=(180, 40), on_press=self.on_add_category,
                         pos_hint={'center_x': 0.5})
        self.add_widget(add_btn)

        self.status_label = Label(text="", size_hint_y=None, height=30, font_size='15sp', color=(0.5,0.2,0.2,1))
        self.add_widget(self.status_label)

        # Initial load
        if self.controller:
            self.controller.set_category_view(self)
            self.controller.refresh_categories()

    def update_category_list(self, categories):
        self.category_list.clear_widgets()
        if not categories:
            self.category_list.add_widget(Label(text="No categories yet.", font_size='15sp', size_hint_y=None, height=30))
        else:
            for cat in categories:
                box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, padding=[10, 0, 10, 0])
                label = Label(text=cat[1], font_size='16sp', halign='left', valign='middle')
                box.add_widget(label)
                self.category_list.add_widget(box)

    def on_add_category(self, instance):
        if self.controller:
            self.controller.add_category(self.new_cat_input.text)

    def update_status(self, message):
        self.status_label.text = message

    def on_back(self, instance):
        if self.controller:
            self.controller.show_product_page()