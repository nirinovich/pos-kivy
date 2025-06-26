from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class DashboardView(BoxLayout):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 30

        # Title
        self.add_widget(Label(
            text="K'iosk POS Dashboard",
            font_size='28sp',
            size_hint_y=0.2,
            bold=True,
            halign='center'
        ))

        # Main buttons grid
        grid = GridLayout(cols=2, spacing=20, size_hint_y=0.5)
        grid.add_widget(Button(text="New Sale", font_size='20sp', on_press=self.on_new_sale))
        grid.add_widget(Button(text="Inventory", font_size='20sp', on_press=self.on_inventory))
        grid.add_widget(Button(text="Reports", font_size='20sp', on_press=self.on_reports))
        grid.add_widget(Button(text="Settings", font_size='20sp', on_press=self.on_settings))
        self.add_widget(grid)

        # Status area
        self.status_label = Label(
            text="Store: OPEN\nSales Today: 0.00 Ar\nLast Sync: --",
            font_size='16sp',
            size_hint_y=0.2,
            halign='left',
            valign='top'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        self.add_widget(self.status_label)

    # Button handlers (to be connected to controller logic)
    def on_new_sale(self, instance):
        if self.controller:
            self.controller.go_to_new_sale()

    def on_inventory(self, instance):
        if self.controller:
            self.controller.go_to_inventory()

    def on_reports(self, instance):
        if self.controller:
            self.controller.go_to_reports()

    def on_settings(self, instance):
        if self.controller:
            self.controller.go_to_settings()

    def update_status(self, store_status, sales_today, last_sync):
        self.status_label.text = f"Store: {store_status}\nSales Today: ${sales_today:.2f}\nLast Sync: {last_sync}"