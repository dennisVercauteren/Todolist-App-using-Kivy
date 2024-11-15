from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty
import os
import json

# File to store tasks
TASKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasks.json')

class TaskCard(MDCard):
    text = StringProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = dp(60)
        self.padding = [dp(15), dp(10)]
        self.spacing = dp(10)
        self.radius = [dp(5)]
        self.elevation = 1
        self.ripple_behavior = True

class TodoList(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(15)
        self.md_bg_color = [0.12, 0.12, 0.12, 1]
        
        # Initialize tasks list
        self.tasks = []
        
        # Title
        title = MDLabel(
            text='Todo List',
            font_style='H4',
            size_hint_y=None,
            height=dp(60),
            halign='center'
        )
        self.add_widget(title)
        
        # Input area
        input_area = MDBoxLayout(
            size_hint_y=None,
            height=dp(60),
            spacing=dp(10),
            padding=[0, dp(10)]
        )
        
        # Text input
        self.task_input = MDTextField(
            hint_text='Add a new task...',
            mode="rectangle",
            size_hint_x=0.8,
            font_size=dp(16)
        )
        self.task_input.bind(on_text_validate=self.add_task)
        
        # Add button
        add_button = MDRaisedButton(
            text="ADD",
            size_hint_x=0.2,
            font_size=dp(14)
        )
        add_button.bind(on_press=self.add_task)
        
        input_area.add_widget(self.task_input)
        input_area.add_widget(add_button)
        self.add_widget(input_area)
        
        # Tasks area with scroll
        self.tasks_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(8),
            size_hint_y=None,
            padding=[0, dp(10)]
        )
        self.tasks_layout.bind(minimum_height=self.tasks_layout.setter('height'))
        
        scroll = ScrollView(
            size_hint=(1, None),
            size=(Window.width, Window.height - dp(180))
        )
        scroll.add_widget(self.tasks_layout)
        self.add_widget(scroll)
        
        # Load saved tasks
        self.load_tasks()
            
    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            # Create task data
            task_data = {'text': task_text, 'completed': False}
            self.tasks.append(task_data)
            
            # Create visual task
            self._create_task_widget(task_data)
            
            # Clear input and save tasks
            self.task_input.text = ''
            self.save_tasks()
            
    def _create_task_widget(self, task_data):
        # Create card for task
        task_card = TaskCard()
        
        # Task label
        label = MDLabel(
            text=task_data['text'],
            size_hint_x=0.7,
            theme_text_color="Secondary" if task_data['completed'] else "Primary"
        )
        
        # Buttons container
        buttons = MDBoxLayout(
            size_hint_x=0.3,
            spacing=dp(5)
        )
        
        # Complete button
        complete_btn = MDIconButton(
            icon='check-circle-outline' if not task_data['completed'] else 'check-circle',
            theme_icon_color="Custom",
            icon_color=[0.2, 0.8, 0.2, 1] if task_data['completed'] else [0.5, 0.5, 0.5, 1],
            size_hint_x=None,
            width=dp(40)
        )
        
        def on_complete(btn):
            task_data['completed'] = not task_data['completed']
            label.theme_text_color = "Secondary" if task_data['completed'] else "Primary"
            btn.icon = 'check-circle' if task_data['completed'] else 'check-circle-outline'
            btn.icon_color = [0.2, 0.8, 0.2, 1] if task_data['completed'] else [0.5, 0.5, 0.5, 1]
            self.save_tasks()
            
        complete_btn.bind(on_press=on_complete)
        
        # Delete button
        delete_btn = MDIconButton(
            icon='delete-outline',
            theme_icon_color="Custom",
            icon_color=[0.8, 0.2, 0.2, 1],
            size_hint_x=None,
            width=dp(40)
        )
        delete_btn.bind(on_press=lambda x: self.delete_task(task_card, task_data))
        
        buttons.add_widget(complete_btn)
        buttons.add_widget(delete_btn)
        
        task_card.add_widget(label)
        task_card.add_widget(buttons)
        
        self.tasks_layout.add_widget(task_card)
            
    def delete_task(self, task_widget, task_data):
        self.tasks_layout.remove_widget(task_widget)
        self.tasks.remove(task_data)
        self.save_tasks()
        
    def load_tasks(self):
        try:
            if os.path.exists(TASKS_FILE):
                with open(TASKS_FILE, 'r') as f:
                    self.tasks = json.load(f)
                    for task_data in self.tasks:
                        self._create_task_widget(task_data)
        except Exception as e:
            print(f"Error loading tasks: {e}")
            
    def save_tasks(self):
        try:
            with open(TASKS_FILE, 'w') as f:
                json.dump(self.tasks, f)
        except Exception as e:
            print(f"Error saving tasks: {e}")

class TodoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        
        Window.size = (400, 600)
        Window.minimum_width = 400
        Window.minimum_height = 600
        
        return TodoList()

if __name__ == '__main__':
    TodoApp().run()
