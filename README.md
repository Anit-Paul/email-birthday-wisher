
# Email Birthday Wisher

## Description
This is a Python-based project that automates the process of sending birthday wishes via email. It picks up the birthdays from a database and sends a personalized birthday message to each person on their special day. The email content is customizable by choosing one of three predefined letter templates.

## Features
- Sends birthday emails automatically on the person's birthday.
- Uses an SMTP server (Gmail) to send the emails.
- Customizable letter templates for personalized messages.
- Error handling for SMTP connection and email sending failures.

## Prerequisites
- Python 3.x
- `smtplib` library (included in Python standard library)
- A Gmail account with an App Password (for security)
- Database file with the users' names, emails, and birthdates (expected to be imported via `data.py`)

## Setup

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/email-birthday-wisher.git
   ```

2. Install any dependencies (if necessary).

3. Update the following variables in `Birthday.py`:
   - `self.path` - Path to the folder containing your letter templates (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`).
   - `self.sender` - Your email address (Gmail).
   - `self.password` - Your Gmail App password (generate it via your Google account).

4. Ensure the `data.py` file contains the necessary information such as names, email addresses, and birthdays. The expected structure for the data is a list of objects with `name`, `email`, `month`, and `day`.

## Usage

To run the birthday email automation:
1. Navigate to the project folder:
   ```bash
   cd email-birthday-wisher
   ```

2. Execute the script:
   ```bash
   python Birthday.py
   ```

The script will automatically send birthday wishes to any user whose birthday matches the current date.

## Customizing the Letter
The birthday letter templates (`letter_1.txt`, `letter_2.txt`, and `letter_3.txt`) are stored in the `path` folder. You can edit these text files to change the content of the birthday messages. Use the placeholder `[NAME]` to insert the recipient's name dynamically.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
