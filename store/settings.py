class Settings:
    def __init__(self):
        pass


APP_SETTINGS: Settings


def init_settings():
    global APP_SETTINGS
    APP_SETTINGS = Settings()
