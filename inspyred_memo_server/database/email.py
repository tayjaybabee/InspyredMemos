"""
Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/database/email.py
 

Description:
    

"""
import smtplib
from email.mime.text import MIMEText
from itsdangerous import URLSafeTimedSerializer
from inspyred_memo_server.config import EMailConfig




class UserVerification:
    """
    Handles user email verification for the InspyredMemos application.
    
    This class manages the generation and validation of email verification tokens,
    and sends verification emails to users.
    """
    
    def __init__(
            self,
            mail_server,
            mail_port,
            mail_user,
            mail_password,
            verification_url_base,
            secret_key=None
    ):
        """
        Initialize the UserVerification system.
        
        Args:
            mail_server (str): SMTP server address.
            mail_port (int): SMTP server port.
            mail_user (str): SMTP username for authentication.
            mail_password (str): SMTP password for authentication.
            verification_url_base (str): Base URL for verification links.
            secret_key (str, optional): Secret key for token generation. 
                If not provided, will attempt to read from environment variable 
                'INSPYRED_MEMOS_SECRET_KEY'. Defaults to a warning value if neither is set.
        """
        import os
        
        self.mail_server = mail_server
        self.mail_port = mail_port
        self.mail_user = mail_user
        self.mail_password = mail_password
        self.verification_url_base = verification_url_base
        
        # Use provided secret_key, or fallback to environment variable
        if secret_key is None:
            secret_key = os.environ.get('INSPYRED_MEMOS_SECRET_KEY')
            if secret_key is None:
                import warnings
                warnings.warn(
                    "No secret key provided for email verification. "
                    "Set INSPYRED_MEMOS_SECRET_KEY environment variable or pass secret_key parameter. "
                    "Using insecure default - DO NOT USE IN PRODUCTION!",
                    SecurityWarning,
                    stacklevel=2
                )
                secret_key = 'insecure-default-key-change-immediately'
        
        self.serializer = URLSafeTimedSerializer(secret_key)
    
    def generate_verification_token(self, email):
        """
        Generate a time-limited verification token for an email address.
        
        Args:
            email (str): The email address to generate a token for.
            
        Returns:
            str: The verification token.
        """
        return self.serializer.dumps(email, salt='email-verification')
    
    def verify_token(self, token, max_age=3600):
        """
        Verify a verification token and extract the email address.
        
        Args:
            token (str): The verification token to validate.
            max_age (int): Maximum age of the token in seconds (default: 3600/1 hour).
            
        Returns:
            str or None: The email address if valid, None if invalid or expired.
        """
        from itsdangerous import SignatureExpired, BadSignature, BadData
        
        try:
            email = self.serializer.loads(
                token,
                salt='email-verification',
                max_age=max_age
            )
            return email
        except (SignatureExpired, BadSignature, BadData) as e:
            # Token is invalid, expired, or malformed
            return None
    
    def send_verification_email(self, to_email, token):
        """
        Send a verification email to the specified address.
        
        Args:
            to_email (str): The recipient's email address.
            token (str): The verification token to include in the email.
            
        Returns:
            bool: True if email was sent successfully, False otherwise.
        """
        import logging
        
        verification_url = f"{self.verification_url_base}?token={token}"
        
        msg = MIMEText(
            f"Click the following link to verify your email: {verification_url}\n\n"
            f"This link will expire in 1 hour."
        )
        msg['Subject'] = 'Verify your InspyredMemos account'
        msg['From'] = self.mail_user
        msg['To'] = to_email
        
        try:
            with smtplib.SMTP(self.mail_server, self.mail_port) as server:
                server.starttls()
                server.login(self.mail_user, self.mail_password)
                server.send_message(msg)
            return True
        except Exception as e:
            logging.error(f"Failed to send verification email to {to_email}: {e}")
            return False
