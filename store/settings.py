from models.settings.application_properties_model import ApplicationProperties
from models.settings.programs_manager import ProgramManager
from store.configuration_settings import ConfigurationSettings
from store.server_settings import ServerSettings


class Settings:
    def __init__(self):
        self.SERVER = ServerSettings()
        self.PROGRAMS = ProgramManager()
        self.CONFIGURATION = ConfigurationSettings()

        self.__initialize_settings()

    def __initialize_settings(self):
        """
        set up initial values
        :return:
        """

        props = self.__loadApplicationProperties()

        self.SERVER.initialize()
        self.CONFIGURATION.initialize(props.configuration())

    @staticmethod
    def __loadApplicationProperties():
        """
        instantiates a class that loads application props and return them to be used in setting up the application
        :return:
        """
        props = ApplicationProperties()
        props.initialize()
        return props


APP_SETTINGS: Settings


def init_settings_store():
    global APP_SETTINGS
    APP_SETTINGS = Settings()
