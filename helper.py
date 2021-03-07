import logging
import logging.config
import smtplib

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from config import To_List, From_Address, From_Password


def config_logger(app):
    logging.config.dictConfig(app.config.get("LOGGING_CONFIG"))
    logger = logging.getLogger(app.config.get("DEFAULT_LOGGER_NAME"))
    app.logger.addHandler(logger)
    app.logger.info("Logger Configured.")


def send_mail():
    sent_mail_list = To_List
    today_date = datetime.today().strftime('%Y-%m-%d')

    message = MIMEMultipart()
    message['Subject'] = 'Daily Report For Covid Cases For Date {}'.format(today_date)
    message['From'] = From_Address
    message['To'] = ', '.join(sent_mail_list)

    mail_text = 'Hello, Here is the Report for Covid 19 active cases in graph format.'
    part = MIMEText(mail_text, 'html')
    message.attach(part)

    csv_file_name = 'covid-data.html'
    part = MIMEApplication(open(csv_file_name, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=csv_file_name)
    message.attach(part)

    s1 = smtplib.SMTP('smtp.gmail.com', 587)
    s1.starttls()
    s1.login(From_Address, From_Password)
    s1.sendmail(From_Address, To_List, message.as_string())
    s1.close()