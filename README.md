# Todo List App

A simple Todo List application built with [KivyMD](https://github.com/kivymd/KivyMD). This app allows you to add, complete, and delete tasks with a user-friendly interface. Tasks are saved locally in a JSON file, so your to-dos persist between sessions.

## Features

- **Add Tasks**: Quickly add new tasks to your list.
- **Complete Tasks**: Mark tasks as completed or uncompleted.
- **Delete Tasks**: Remove tasks you no longer need.
- **Persistent Storage**: Tasks are saved locally in `tasks.json`.

## Screenshots

![image](https://github.com/user-attachments/assets/7fd50a74-dc50-4677-9528-6707f4145120)


## Requirements

- Python 3.x
- [Kivy](https://kivy.org/#home)
- [KivyMD](https://github.com/kivymd/KivyMD)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**

   ```bash
   pip install kivy kivymd
   ```

   *Alternatively, install from the `requirements.txt` if provided:*

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using the following command:

```bash
python todo_app.py
```

*Replace `todo_app.py` with the actual filename if different.*

## File Structure

- `todo_app.py`: Main application script.
- `tasks.json`: JSON file where tasks are stored persistently.

## Customization

- **Theme Settings**: Modify the theme by changing `self.theme_cls.theme_style` and `self.theme_cls.primary_palette` in the `TodoApp` class.
- **Window Size**: Adjust the window size by changing `Window.size` and `Window.minimum_width/height`.

## How It Works

- **Adding Tasks**: Enter a task in the text field and press the "ADD" button or hit enter.
- **Completing Tasks**: Click the check-circle icon to toggle the task's completed status.
- **Deleting Tasks**: Click the trash can icon to remove the task from the list.
- **Persistent Storage**: Tasks are saved to `tasks.json` upon addition, completion, or deletion.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---
