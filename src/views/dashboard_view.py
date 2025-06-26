from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

class DashboardView(MDBoxLayout):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'
        self.padding = [dp(40), dp(40), dp(40), dp(40)]
        self.spacing = dp(30)
        self.md_bg_color = get_color_from_hex("#F5F6FA")  # Light background

        self.add_widget(MDLabel(
            text="K'iosk POS Dashboard",
            font_size=dp(32),
            bold=True,
            size_hint_y=0.2,
            halign='center',
            theme_text_color="Primary"
        ))

        card = MDCard(
            orientation="vertical",
            padding=dp(24),
            size_hint=(None, None),
            size=(dp(600), dp(260)),
            elevation=8,
            pos_hint={"center_x": 0.5},
            md_bg_color=get_color_from_hex("#FFFFFF"),
        )

        grid = MDGridLayout(cols=2, spacing=dp(20), size_hint_y=None, height=dp(180))

        grid.add_widget(
            MDButton(
                MDButtonIcon(icon="cash-register"),
                MDButtonText(text="New Sale"),
                style="elevated",
                on_release=self.on_new_sale,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        grid.add_widget(
            MDButton(
                MDButtonIcon(icon="package-variant"),
                MDButtonText(text="Product Management"),
                style="elevated",
                on_release=self.on_product_management,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        grid.add_widget(
            MDButton(
                MDButtonIcon(icon="chart-bar"),
                MDButtonText(text="Reports"),
                style="elevated",
                on_release=self.on_reports,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        grid.add_widget(
            MDButton(
                MDButtonIcon(icon="cog"),
                MDButtonText(text="Settings"),
                style="elevated",
                on_release=self.on_settings,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        card.add_widget(grid)
        self.add_widget(card)

        self.status_label = MDLabel(
            text="Store: OPEN\nSales Today: $0.00\nLast Sync: --",
            font_size=dp(18),
            size_hint_y=0.2,
            halign='left',
            valign='top',
            theme_text_color="Secondary"
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        self.add_widget(self.status_label)

    def on_new_sale(self, instance):
        if self.controller:
            self.controller.go_to_new_sale()

    def on_product_management(self, instance):
        if self.controller:
            self.controller.go_to_product_management()

    def on_reports(self, instance):
        if self.controller:
            self.controller.go_to_reports()

    def on_settings(self, instance):
        if self.controller:
            self.controller.go_to_settings()

    def update_status(self, store_status, sales_today, last_sync):
        self.status_label.text = f"Store: {store_status}\nSales Today: ${sales_today:.2f}\nLast Sync: {last_sync}"