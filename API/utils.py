from configparser import ConfigParser
import os

class Utils:
    @staticmethod    
    def config(filename=os.path.join(os.path.dirname(__file__), 'database.ini'),section='postgresql'):
        parser = ConfigParser()
        parser.read(filename)
        dic = {}
        if parser.has_section(section):
            dic = {x:y for (x,y) in parser.items(section)}
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section,filename))
        return dic