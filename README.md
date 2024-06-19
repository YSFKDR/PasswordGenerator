# Password Generator

This is a Password Generator application built using Python and Tkinter. The application allows users to generate strong, secure passwords based on customizable criteria.

## Features

- Generate passwords of variable lengths (4-64 characters).
- Include letters, mixed case, punctuation, and numbers in the generated passwords.
- Copy the generated password to the clipboard with a single click.
- Toggle between light and dark themes.

## Requirements

- Python 3.x
- Tkinter (included with standard Python distribution)

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended).

   ```sh
   python -m venv pgenv
   ```
4. Activate the virtual environment.

   ```sh
   # On Windows
   pgenv\Scripts\activate

   # On macOS/Linux
   source pgenv/bin/activate
   ```
5. Install the required packages.
   
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Navigate to the project directory.
2. Run the main application script.

   ``` sh
   python main.py
   ```

## Directory Structure

   ```markdown
   Password-Generator/
   ├── 
   ├── main.py                # Entry point for the application.
   ├── gui.py                 # Contains the user interface code.
   ├── password_generator.py  # Contains the logic for generating passwords.
   ├── utils.py               # Contains utility functions such as copying text to the clipboard.
   ├── requirements.txt       # List of required packages.
   ├── README.md              # Project documentation.
   └── LICENSE                # License for the project.
   ```

## Files

- `main.py`: Entry point for the application.
- `gui.py`: Contains the user interface code.
- `password`_generator.py: Contains the logic for generating passwords.
- `utils.py`: Contains utility functions such as copying text to the clipboard.

## Screenshots

## Customization

You can customize the application by modifying the following files:

- `gui.py`: Change the appearance and behavior of the GUI.
- `password_generator.py`: Modify the password generation logic.
- `utils.py`: Add or modify utility functions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.