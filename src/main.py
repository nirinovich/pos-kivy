#!/usr/bin/env python3
"""
Simple Kivy Hello World Application
"""

# Import Kivy components
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HelloWorldView(BoxLayout):
    """
    Simple Hello World View
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20
        
        # Create the visual elements
        self.setup_ui()
    
    def setup_ui(self):
        """Create all the visual elements."""
        
        # Main title
        title = Label(
            text='Hello World!',
            font_size='32sp',
            size_hint_y=0.6,
            halign='center'
        )
        title.bind(size=title.setter('text_size'))
        
        # Status message
        self.status_label = Label(
            text='Welcome to K\'iosk POS System',
            font_size='18sp',
            size_hint_y=0.2,
            halign='center'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        
        # Button
        hello_button = Button(
            text='Click Me',
            size_hint_y=0.2,
            font_size='18sp'
        )
        hello_button.bind(on_press=self.on_button_press)
        
        # Add all elements to the layout
        self.add_widget(title)
        self.add_widget(self.status_label)
        self.add_widget(hello_button)
    
    def on_button_press(self, instance):
        """Handle button press."""
        self.status_label.text = "Hello! You clicked the button!"


class HelloWorldApp(App):
    """
    Simple Hello World Application
    """
    
    def build(self):
        """Build and return the main widget."""
        # Set window title
        self.title = "Kivy Hello World"
        
        # Create and return the view
        return HelloWorldView()


# Run the application
if __name__ == '__main__':
    print("🚀 Starting Kivy Hello World Application...")
    print("=" * 40)
    
    # Start the Kivy app
    HelloWorldApp().run()