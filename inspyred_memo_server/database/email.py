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
    def __init__(
            self,
            mail_server,
            mail_port,
            mail_user,
            mail_password,
            verification_url_base
    ):
