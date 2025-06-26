from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

class ProductView(MDBoxLayout):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'
        self.padding = [dp(0), dp(20), dp(0), dp(0)]
        self.spacing = dp(0)
        self.md_bg_color = get_color_from_hex("#F5F6FA")  # Light background

        # --- Top bar ---
        top_bar = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=dp(56))
        back_btn = MDIconButton(icon="arrow-left", on_release=self.on_back)
        top_bar.add_widget(back_btn)
        top_bar.add_widget(MDLabel(
            text="Product Management",
            halign='center',
            theme_text_color="Primary"
        ))
        top_bar.add_widget(Widget(size_hint_x=None, width=dp(40)))  # Spacer
        self.add_widget(top_bar)

        # --- Main content area ---
        main_content = MDBoxLayout(orientation='horizontal', spacing=dp(40), padding=[dp(60), 0, dp(60), 0])

        # --- Left: Product List ---
        left_box = MDBoxLayout(orientation='vertical', size_hint_x=0.5, spacing=dp(20))
        left_box.add_widget(MDLabel(
            text="Products",
            halign="center",
            size_hint_y=None,
            height=dp(40),
            theme_text_color="Primary"
        ))
        self.product_list = MDGridLayout(cols=1, spacing=dp(8), size_hint_y=None, padding=[0, dp(10), 0, dp(10)])
        self.product_list.bind(minimum_height=self.product_list.setter('height'))
        scroll = MDScrollView(size_hint=(1, 1))
        scroll.add_widget(self.product_list)
        left_box.add_widget(scroll)
        main_content.add_widget(left_box)

        # --- Right: Form and Actions ---
        right_box = MDBoxLayout(orientation='vertical', size_hint_x=0.5, spacing=dp(20), padding=[dp(20), dp(40), dp(20), dp(40)])

        # Form fields
        form_grid = MDGridLayout(cols=2, spacing=dp(10), size_hint_y=None, height=dp(180))
        form_grid.add_widget(MDLabel(text="Name:", halign="right", theme_text_color="Primary"))
        self.name_input = MDTextField()
        form_grid.add_widget(self.name_input)
        form_grid.add_widget(MDLabel(text="Price:", halign="right", theme_text_color="Primary"))
        self.price_input = MDTextField(input_filter='float')
        form_grid.add_widget(self.price_input)
        form_grid.add_widget(MDLabel(text="Category:", halign="right", theme_text_color="Primary"))
        self.category_field = MDTextField(hint_text="Select Category", readonly=True)
        self.category_field.bind(on_focus=self.open_category_menu)
        form_grid.add_widget(self.category_field)
        right_box.add_widget(form_grid)

        # Action buttons row (using new button style)
        btn_row = MDBoxLayout(orientation='horizontal', spacing=dp(10), size_hint_y=None, height=dp(48))
        add_btn = MDButton(
            MDButtonIcon(icon="plus"),
            MDButtonText(text="Add"),
            style="elevated",
            md_bg_color=(0.2, 0.7, 0.2, 1),
            on_release=self.on_add
        )
        edit_btn = MDButton(
            MDButtonIcon(icon="pencil"),
            MDButtonText(text="Edit"),
            style="elevated",
            md_bg_color=(0.2, 0.4, 0.8, 1),
            on_release=self.on_edit
        )
        delete_btn = MDButton(
            MDButtonIcon(icon="delete"),
            MDButtonText(text="Delete"),
            style="elevated",
            md_bg_color=(0.8, 0.2, 0.2, 1),
            on_release=self.on_delete
        )
        btn_row.add_widget(add_btn)
        btn_row.add_widget(edit_btn)
        btn_row.add_widget(delete_btn)
        right_box.add_widget(btn_row)

        # Manage Categories button (new style)
        cat_btn = MDButton(
            MDButtonIcon(icon="shape-outline"),
            MDButtonText(text="Manage Categories"),
            style="elevated",
            on_release=self.on_manage_categories
        )
        right_box.add_widget(cat_btn)

        # Status message
        self.status_label = MDLabel(text="", halign="center", size_hint_y=None, height=dp(30), theme_text_color="Primary")
        right_box.add_widget(self.status_label)

        main_content.add_widget(right_box)
        self.add_widget(main_content)

        # --- Category menu ---
        self.category_menu_items = []
        self.category_menu = None

        # --- Initial load ---
        if self.controller:
            self.controller.set_view(self)
            self.controller.refresh_products()
            self.controller.refresh_categories()

    # --- Product List ---
    def update_product_list(self, products):
        self.product_list.clear_widgets()
        if not products:
            self.product_list.add_widget(MDLabel(text="No products yet.", halign="center", theme_text_color="Primary"))
        else:
            for prod in products:
                btn = MDButton(
                    MDButtonIcon(icon="cube-outline"),
                    MDButtonText(text=f"{prod[0]}: {prod[1]} - ${prod[2]:.2f} [{prod[3] if prod[3] else 'No Category'}]"),
                    size_hint_y=None,
                    height=dp(44),
                    style="elevated",
                    md_bg_color=(0.2, 0.6, 0.95, 1),
                    on_release=lambda instance, p=prod: self.on_select(instance, p)
                )
                self.product_list.add_widget(btn)

    # --- Category Dropdown ---
    def update_category_spinner(self, categories):
        self.category_menu_items = [
            {"text": cat[1], "on_release": lambda x=cat[1]: self.set_category(x)}
            for cat in categories
        ]
        if not self.category_menu:
            self.category_menu = MDDropdownMenu(
                caller=self.category_field,
                items=self.category_menu_items,
            )
        else:
            self.category_menu.items = self.category_menu_items
        if categories:
            self.category_field.text = categories[0][1]
        else:
            self.category_field.text = "No Category"

    def open_category_menu(self, instance, value):
        if value and self.category_menu:
            self.category_menu.open()

    def set_category(self, category_name):
        self.category_field.text = category_name
        if self.category_menu:
            self.category_menu.dismiss()

    # --- Form Actions ---
    def on_select(self, btn, product):
        product_id, name, price, category = product
        self.name_input.text = name
        self.price_input.text = str(price)
        self.category_field.text = category if category else "No Category"
        if self.controller:
            self.controller.select_product(product_id, name, price, category)

    def set_form(self, name, price, category):
        self.name_input.text = name
        self.price_input.text = str(price)
        self.category_field.text = category

    def on_add(self, instance):
        if self.controller:
            self.controller.add_product(
                self.name_input.text,
                self.price_input.text,
                self.category_field.text
            )

    def on_edit(self, instance):
        if self.controller:
            self.controller.edit_product(
                self.name_input.text,
                self.price_input.text,
                self.category_field.text
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
        if self.controller and self.controller.app and hasattr(self.controller.app, "show_category_management"):
            self.controller.app.show_category_management()