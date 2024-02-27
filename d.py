from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class LoguruLogger(Logger):
    def log(self, message):
        # Implement logging logic using Loguru
        print("Logging message using Loguru:", message)

class GoogleAuthLogger(Logger):
    def log(self, message):
        # Implement logging logic using Google Auth
        print("Logging message using Google Auth:", message)
class Logging(Logger):
    def log(self, message):
        # Implement logging logic using Logging
        print("Logging message using Logging:", message)
class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def perform_action(self):
        # Perform some action
        self.logger.log("Action performed successfully")

app = Application(LoguruLogger())
app.perform_action()  # Logs using Loguru

app = Application(GoogleAuthLogger())
app.perform_action()  # Logs using Google Auth

app = Application(Logging())
app.perform_action() # Logs using Logging