from store.server_settings import ServerSettings


class Settings:
    def __init__(self):
        self.SERVER = ServerSettings()

        self.__initialize_settings()

    def __initialize_settings(self):
        """
        set up initial values
        :return:
        """
        self.SERVER.initialize()


APP_SETTINGS: Settings


def init_settings_store():
    global APP_SETTINGS
    APP_SETTINGS = Settings()
