"""
    Profile
    ----------
    Author : Baku - Stark
    Info   : Application logger.
"""
import socket
import os
from api.Colors import Colors
from datetime import datetime

class Logger:
    _DEBUG = f"{Colors.GREEN}[DEBUG]{Colors.END}"
    _INFO = f"{Colors.CYAN}[INFO]{Colors.END}"
    _WARNING = f"{Colors.BLUE}[WARNING]{Colors.END}"
    _ERROR = f"{Colors.RED}[ERROR]{Colors.END}"

    def __init__(self, process_name="python"):
        self.process_name = process_name
        self.hostname = socket.gethostname()

    def _log(self, color_code, message):
        now = datetime.now().strftime("%b %d %Y - %H:%M:%S |")
        pid = os.getpid()
        # Exemplo de saída:
        # Sep 25 13:44:37 hostname process[pid]: level_label: mensagem
        print(f"{now} {self.hostname} {self.process_name} [{pid}] -> {color_code}{Colors.END}: {message}")

    def debug(self, message):
        self._log(color_code=self._DEBUG, message=message)

    def info(self, message):
        self._log(color_code=self._INFO, message=message)

    def warning(self, message):
        self._log(color_code=self._WARNING, message=message)

    def error(self, message):
        self._log(color_code=self._ERROR, message=message)