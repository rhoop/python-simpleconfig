import configparser
config = configparser.ConfigParser()


class Section(object):

    """docstring for Sections"""

    def __init__(self, name):
        super(Section, self).__init__()
        self.name = name
        for option in config.options(self.name):
            setattr(self, option, config.get(self.name, option))

    def all(self):
        return


class Config(object):

    """docstring for Config"""
    __sections = []
    __config = None

    def __init__(self, configfile):
        super(Config, self).__init__()
        self.configfile = configfile
        self.__config = config
        self.__config.read(self.configfile)

        for section in self.__config.sections():
            self.__sections.append(section)
            setattr(self, section, Section(section))

    def sections(self):
        return str(self.__sections)

    def __str__(self):
        return str(self.__sections)

    def save(self):

        with open(self.configfile, 'wb') as configfile:
            self.__config.write(configfile)
