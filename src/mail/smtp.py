import smtplib

from src.config import settings
from src.logs.log import logger


class SMTPServer:
    _smtp: smtplib.SMTP_SSL = None

    def __init__(self) -> None:
        self._smtp = smtplib.SMTP_SSL(
            local_hostname=settings.smtp.adress,
            port=settings.smtp.port
        )
        # self._smtp.ehlo()
        self._smtp.starttls()

    def connect(self) -> None:
        self._smtp.connect(
            host=settings.smtp.adress,
            port=settings.smtp.port
        )
        self._smtp.ehlo()
        self._smtp.starttls()

    def login(self) -> None:
        try:
            self._smtp.login(
                user=settings.email_auth.adress,
                password=settings.email_auth.password
            )
        except Exception as _ex:
            logger.warning(_ex)

    def send(
            self,
            message: str,
            to_adress: str,
            from_adress: str = settings.email_auth.adress
    ) -> None:
        self._smtp.sendmail(
            from_addr=from_adress,
            to_addrs=to_adress,
            msg=message
        )

    def quit(self) -> None:
        self._smtp.close()
        self._smtp.ehlo()
        self._smtp.quit()

