from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.uix.widget import Widget

class CategoryView(MDBoxLayout):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.controller.view = self
        self.orientation = 'vertical'
        self.padding = [dp(40), dp(40), dp(40), dp(40)]
        self.spacing = dp(20)
        self.md_bg_color = get_color_from_hex("#F5F6FA")

        # Top bar
        top_bar = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=dp(56), spacing=dp(10))
        back_btn = MDIconButton(icon="arrow-left", on_release=self.on_back)
        top_bar.add_widget(back_btn)
        top_bar.add_widget(MDLabel(
            text="Category Management",
            font_size='24sp',
            halign='center',
            theme_text_color="Primary"
        ))
        top_bar.add_widget(Widget(size_hint_x=None, width=dp(40)))
        self.add_widget(top_bar)

        # Category list label
        self.add_widget(MDLabel(
            text="Categories:",
            font_size='18sp',
            size_hint_y=None,
            height=dp(30),
            halign='left',
            theme_text_color="Primary"
        ))

        # Category list
        scroll = MDScrollView(size_hint=(1, 0.35))
        self.category_list = MDGridLayout(cols=1, spacing=dp(8), size_hint_y=None, padding=[0, dp(10), 0, dp(10)])
        self.category_list.bind(minimum_height=self.category_list.setter('height'))
        scroll.add_widget(self.category_list)
        self.add_widget(scroll)

        # Add category form
        form = MDBoxLayout(orientation='horizontal', spacing=dp(10), size_hint_y=None, height=dp(50))
        form.add_widget(MDLabel(
            text="New Category:",
            font_size='16sp',
            size_hint_x=0.4,
            halign='right',
            theme_text_color="Primary"
        ))
        self.new_cat_input = MDTextField(font_size='16sp', multiline=False, size_hint_x=0.6)
        form.add_widget(self.new_cat_input)
        self.add_widget(form)

        add_btn = MDButton(
            MDButtonText(text="Add Category"),
            style="elevated",
            size_hint=(None, None),
            size=(dp(180), dp(40)),
            on_release=self.on_add_category
        )
        self.add_widget(add_btn)

        self.status_label = MDLabel(
            text="",
            size_hint_y=None,
            height=dp(30),
            font_size='15sp',
            halign="center",
            theme_text_color="Primary"
        )
        self.add_widget(self.status_label)

        self.controller.refresh_categories()

    def update_category_list(self, categories):
        self.category_list.clear_widgets()
        if not categories:
            self.category_list.add_widget(MDLabel(
                text="No categories yet.",
                font_size='15sp',
                size_hint_y=None,
                height=dp(30),
                halign="center",
                theme_text_color="Primary"
            ))
        else:
            for cat in categories:
                box = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40), padding=[dp(10), 0, dp(10), 0])
                label = MDLabel(
                    text=cat[1],
                    font_size='16sp',
                    halign='left',
                    theme_text_color="Primary"
                )
                del_btn = MDIconButton(icon="delete", on_release=lambda inst, cid=cat[0]: self.on_delete_category(cid))
                box.add_widget(label)
                box.add_widget(del_btn)
                self.category_list.add_widget(box)

    def on_add_category(self, instance):
        self.controller.add_category(self.new_cat_input.text)
        self.new_cat_input.text = ""

    def on_delete_category(self, category_id):
        self.controller.delete_category(category_id)

    def update_status(self, message):
        self.status_label.text = message

    def on_back(self, instance):
        if hasattr(self.controller, "on_back"):
            self.controller.on_back()