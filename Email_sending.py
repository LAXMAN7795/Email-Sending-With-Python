# Import necessary libraries
import smtplib  # Library to handle sending emails using SMTP
from email.message import EmailMessage  # To structure and send an email
from string import Template  # To use template strings for email content
from pathlib import Path  # To handle file paths and read files

# Read and load the HTML email template
# Make sure the 'pyhtml.html' file exists in the same directory as this script or provide the correct path.
html = Template(Path('pyhtml.html').read_text())

# Create an email message object
email = EmailMessage()
email['from'] = 'sender_email@example.com'  # Sender's email address
email['to'] = 'recipient_email@example.com'  # Recipient's email address
email['subject'] = 'Regarding 1 day leave'  # Subject of the email

# Set the content of the email
# Use substitute to replace placeholders in the HTML template (e.g., replace {{name}} with 'John').
# Ensure the content type is 'html' for rendering HTML in the email.
email.set_content(html.substitute({'name': 'Laxman'}), 'html')

# Send the email using an SMTP server
try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  # Connect to Gmail's SMTP server
        smtp.ehlo()  # Identify yourself to the server
        smtp.starttls()  # Start TLS encryption for secure communication
        smtp.login('sender_email@example.com', 'password123')  # Login to the sender's email account
        smtp.send_message(email)  # Send the email message
        print("Email sent successfully!")  # Success message
except FileNotFoundError as e:
    print("Error: HTML template file not found. Please check the path to 'pyhtml.html'.", e)
except smtplib.SMTPAuthenticationError:
    print("Error: Authentication failed. Please check the sender's email and password.")
except Exception as e:
    print("An unexpected error occurred:", e)
