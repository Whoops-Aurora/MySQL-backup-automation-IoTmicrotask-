# OS-project
# MySQL Database Backup Script for operating system course guided by Dr.Shrinivas Desai

This script performs a backup of a MySQL database, encrypts the backup files for security, and sends a notification email about the backup completion. It also includes optional features for starting and shutting down the MySQL database as well as scheduling the backup process.

## Features

- Backup of MySQL database
- Encryption of backup files for security
- Optional startup and shutdown of MySQL database
- Email notification about backup completion

## Prerequisites

- Python 3.6 or higher
- Required Python packages: cryptography, dotenv
- MySQL server installed and accessible
- SMTP server details for sending email notifications

## Setup

1. Clone the repository or download the script file.

2. Install the required Python packages by running the following command:
    pip install cryptography python-dotenv

3. Create a `.env` file in the same directory as the script and set the following environment variables:
- `DB_HOST`: MySQL database host address
- `DB_USER`: MySQL database username
- `DB_PASSWORD`: MySQL database password
- `DB_NAME`: MySQL database name
- `BACKUP_DIR`: Directory to store the backup files
- `ENCRYPT_KEY`: Encryption key for securing the backup files
- `SMTP_SERVER`: SMTP server address for email notifications
- `SMTP_PORT`: SMTP server port for email notifications
- `SENDER_EMAIL`: Email address of the sender for email notifications
- `SENDER_PASSWORD`: Password or app-specific password of the sender email
- `RECIPIENT_EMAIL`: Email address of the recipient for email notifications

4. Customize the `start_database()`, `shutdown_database()`, and `send_notification_email()` functions in the script as per your requirements.

5. Run the script using the following command:
    python3 script_name.py
Replace `script_name.py` with the actual name of your backup script file.

## Usage

- The script will start the MySQL database (if enabled), perform a backup of the specified database, encrypt the backup files, and shut down the MySQL database (if enabled).

- An email notification will be sent to the specified recipient email address upon completion of the backup process.

- Ensure that the specified backup directory exists and is writable by the script.

## Notes

- Make sure to secure the `.env` file as it contains sensitive information such as database credentials and encryption key.

- It's recommended to schedule regular backups using tools like cron or task scheduler for automated backup execution.

- Custom logic for starting and shutting down the MySQL database should be implemented in the `start_database()` and `shutdown_database()` functions, respectively.

- Additional customization can be done to enhance the email notification functionality or modify the backup process as per specific requirements.

