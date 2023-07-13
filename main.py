import os
import time
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet
from dotenv import load_dotenv
load_dotenv()
# MySQL database details
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
# Backup settings
BACKUP_DIR = os.getenv('BACKUP_DIR')
ENCRYPT_KEY = os.getenv('ENCRYPT_KEY')
# Encryption function using Fernet symmetric encryption
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
# mail function
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')
#set flag to 0 when database is not completed
flag=1
# Backup MySQL database
def backup_database():
    timestamp = time.strftime('%Y%m%d%H%M%S')
    backup_file = f'{DB_NAME}_{timestamp}.sql'
    backup_path = os.path.join(BACKUP_DIR, backup_file)
    command = f'mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {backup_path}'
    subprocess.run(command, shell=True)
    encrypt_file(backup_path, ENCRYPT_KEY)
    print(f'Successfully backed up and encrypted the database to {backup_path}')
def start_database():
    print('Starting the MySQL database...')
def shutdown_database():
    print('Shutting down the MySQL database...')
def send_notification_email():
    subject = 'Database Backup Completed'
    body = 'The backup process has completed successfully.'+ '\n' + 'Please check the backup folder:'+BACKUP_DIR+'\n'+'Password:'+'\n'+ENCRYPT_KEY+'\n'+'Thank you'
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print('Email notification sent successfully!')
    except Exception as e:
        print('Error sending email notification:', str(e))
def main():
    #Arfa: start_database()
    #aman: backup_database()
    #amogh:shutdown_database()
    #Adwait: send_notification_email()
    send_notification_email()
# Run the script
if __name__ == '__main__':
    main()
