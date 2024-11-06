from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.mail.smtp import SMTPServer
from src.config import settings


class MailMessage:
    smtp: SMTPServer = SMTPServer()

    @classmethod
    def _message(cls) -> MIMEMultipart:
        return MIMEMultipart()

    @classmethod
    def send(
            cls,
            text: str,
            to_adress: str,
            from_adress: str = settings.email_auth.adress,
            subject: str = "Auth credentials",
    ) -> None:
        message = cls._message()
        message["From"] = from_adress
        message["To"] = to_adress
        message["Subject"] = subject
        message.attach(
            MIMEText(
                _text=text,
                _subtype="plain"
            )
        )
        cls.smtp.send(
            message=message.as_string(),
            to_adress=to_adress
        )
        cls.smtp.quit()
