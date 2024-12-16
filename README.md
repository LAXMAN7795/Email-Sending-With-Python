📧 Email Automation with HTML Template Using Python:
🚀 Project Overview:
This repository contains a Python script that automates sending HTML-formatted email notifications using Gmail's SMTP server. The script leverages a custom HTML email template (pyhtml.html) for dynamic content rendering with placeholders like ${name}. This allows sending personalized email notifications such as leave requests, notifications, or other formal alerts.

✨ Features
Dynamic Email Content: Customize email content using placeholder substitution in an HTML email template.
HTML Email Template Integration: Use dynamic data placeholders in the email content through HTML templates.
SMTP with Gmail Integration: Securely connect to Gmail's SMTP server with TLS encryption.
Error Handling: Built-in error handling for common issues such as authentication failures or missing files.
Simple and Reusable Code: Easy to integrate with other automation or user data inputs.

🔧 Tech Stack
Python Libraries:
smtplib: For sending emails using the SMTP protocol.
email.message: Handles email content structure and sending.
string.Template: For dynamic placeholder replacement.
pathlib: Handles file paths robustly.
Email Service: Gmail's SMTP server (smtp.gmail.com)
HTML Email Template: A reusable .html template for structuring email content.

📁 Repository Contents
.
├── Email_sending.py          # Python script for sending the email.
├── pyhtml.html              # HTML template for email formatting.
├── README.md                # Documentation for the repository.
└── requirements.txt         # List of dependencies (if required).

🛠️ How It Works
The script dynamically injects data into the pyhtml.html file placeholders using string.Template.
Sends the email securely through Gmail's SMTP server using TLS encryption.
Handles missing file errors, authentication failures, or other unexpected errors gracefully.
Displays appropriate success/error messages based on execution.

🏗️ Setup Instructions
To run this script, follow these steps:

1️⃣ Clone the Repository:
git clone https://github.com/username/repository-name.git
cd repository-name.

2️⃣ Set Up a Python Virtual Environment
(Optional but recommended)

Linux/macOS:
python3 -m venv env
source env/bin/activate.

Windows:
python -m venv env
.\env\Scripts\activate.

3️⃣ Install Required Dependencies
Ensure you install any required dependencies. For this script, there’s no need for third-party dependencies beyond Python's standard library.

Create a requirements.txt if additional dependencies are required in the future.
pip install -r requirements.txt.

4️⃣ Update Configuration in the Script
Edit these values in the Email_sending.py script:

Replace sender_email@example.com with your Gmail ID.
Replace password123 with your app password (use App Passwords instead of your main Gmail password for security).
Replace recipient_email@example.com with the recipient's email address.

5️⃣ Ensure HTML Template is Present
Make sure pyhtml.html is located in the same directory as Email_sending.py.

6️⃣ Run the Script
Once the above is configured:
python Email_sending.py

💬 Example Output
Success Case
Email sent successfully!

Common Errors:
FileNotFoundError:	HTML template file (pyhtml.html) is missing.
SMTPAuthenticationError:	Authentication failed. Verify password123 and enable "Less Secure Apps" or use App Passwords.
Unexpected Errors:	Any other unhandled exceptions are logged.

📊 Expected Email Example
Recipient will receive:
Subject: Regarding 1 day leave
Body:
Dear Sir/Madam,

I would like to inform you that I will not be able to come to the office tomorrow. 
Please grant me leave for one day. Your kind understanding is appreciated.

Thank you,
Laxman

🔒 Security Considerations
Use App Passwords instead of directly entering your main password into the script for Gmail authentication.
Avoid exposing sensitive credentials (password) on GitHub. Use environment variables for credentials securely.

You can set up App Passwords for Gmail by following these steps:

🛡️ What are App Passwords?
App Passwords are 16-digit passcodes that allow you to sign into your Google account securely without needing to use your primary password. They are ideal for third-party apps or scripts like your Email_sending.py script instead of exposing your real Gmail password.

🚀 How to Set Up App Passwords for Gmail
Go to Your Google Account Security Settings

Visit: https://myaccount.google.com/
Log in with Your Gmail Credentials

Navigate to the "Security" Section

On the left-hand menu, click Security.
Enable 2-Step Verification

App Passwords will only be available if 2-Step Verification is turned on.
Scroll to the 2-Step Verification section and enable it if it isn't already set up.
Generate an App Password

After enabling 2-Step Verification:
Scroll down to the App Passwords section.
Click on App Passwords.
From the drop-down, select the app (e.g., "Mail") and device type (e.g., "Windows Computer").
Click Generate.
Copy Your Generated App Password

Once the password is generated, copy it. You won't be able to view it again.
Use This App Password in Your Script

Replace 'password123' with this 16-digit App Password in your script.

🙏 Acknowledgments:
Thanks to:

Gmail's SMTP documentation.
Python's built-in smtplib and string.Template functionalities for ease of email rendering.

📄 Expected Output
When the script runs successfully and sends the email, the expected output in your terminal would look like this:

✅ Successful Case
Email sent successfully!
This indicates that:

The script connected to Gmail's SMTP server (smtp.gmail.com) using the provided App Password.
The email was sent to the recipient's email address as specified in the script.
The HTML email template was successfully rendered with dynamic content.

🛑 Error Scenarios
If any error occurs during execution, you might see these errors:

1. FileNotFoundError
Occurs if pyhtml.html is missing or the path to it is incorrect.
Error: HTML template file not found. Please check the path to 'pyhtml.html'.

2. SMTPAuthenticationError
Occurs if the login credentials are incorrect or the App Password is not set up properly.
Error: Authentication failed. Please check the sender's email and password.

3. Other Unexpected Exceptions
Any other issue could lead to:
An unexpected error occurred: <error details>

🧩 Example of the Sent Email
Once sent, the email should look like this:

Subject:
Regarding 1 day leave

Body of the email:
Leave Request Notification

Dear Sir/Madam,
I would like to inform you that I will not be able to come to the office tomorrow. Please grant me leave for one day. Your kind understanding is appreciated.

Thank you,
Laxman

This is dynamically populated with the placeholder content replaced by Laxman, as set in your script.
