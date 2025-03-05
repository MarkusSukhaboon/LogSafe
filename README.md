# LogSafe - Password Manager

## Overview

LogSafe is a simple password manager application built using Python and the Tkinter library. It allows users to store and manage their passwords for various websites and applications securely. The application provides features such as password generation, copying credentials to the clipboard, and saving entries to a CSV file for future reference.

## Features

- **Password Storage**: Store website/app names, login credentials, passwords, and comments.
- **Password Generation**: Generate random passwords with customizable length.
- **Copy to Clipboard**: Easily copy website/app names, login credentials, passwords, and comments to the clipboard.
- **CSV Storage**: Save all entries to a CSV file (`all_passwords.csv`) for persistent storage.
- **Load Records**: Load previously saved records from the CSV file and populate the fields for easy access.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- `pyperclip` library (for copying text to the clipboard)
- `csv` library (for handling CSV files)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/LogSafe.git
   cd LogSafe
   ```

2. **Install Dependencies**:
   ```bash
   pip install pyperclip
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

## Usage

1. **Enter Website/App Details**:
   - Enter the website or app name in the "Webpage / App" field.
   - Enter your login credentials (e.g., email or username) in the "Login / E-Mail" field.
   - Enter your password in the "Password" field or generate a new one using the "Create" button.
   - Optionally, add a comment in the "Comment" field.

2. **Generate Password**:
   - Use the "Password Length" dropdown to select the desired length of the password.
   - Click the "Create" button to generate a random password.

3. **Copy to Clipboard**:
   - Use the "Copy" buttons next to each field to copy the respective information to the clipboard.

4. **Save Entry**:
   - Click the "Save in database" button to save the entry to the CSV file.

5. **Load Record**:
   - Use the "Load Record" dropdown to select a previously saved website/app name.
   - The corresponding login, password, and comment fields will be automatically populated.

## File Structure

- `main.py`: The main script that runs the LogSafe application.
- `pw_generator.py`: A helper script that generates random passwords.
- `all_passwords.csv`: The CSV file where all password entries are stored.
- `logsafe_bg_400x400.png`: Background image for the application.
- `logsafe_icon_32x32.png`: Icon for the application window.

## Code Overview

### `main.py`

- **Imports**: The script imports necessary libraries such as `csv`, `tkinter`, `pyperclip`, and the `create_pw` function from `pw_generator.py`.
- **Constants**: Defines constants for image paths and color schemes.
- **Business Logic**: Functions for handling data entry, saving to CSV, and updating the UI.
- **UI Setup**: Configures the Tkinter window, labels, input fields, buttons, and comboboxes.

### `pw_generator.py`

- **Function**: `create_pw(pw_length)` generates a random password of the specified length using a combination of letters, digits, and symbols.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Python community for providing excellent libraries and resources.
- Special thanks to the creators of Tkinter and pyperclip for making this project possible.

## Contact

For any questions or feedback, please reach out to [animakontakt@gmail.com].

---

Enjoy using LogSafe to manage your passwords securely!
