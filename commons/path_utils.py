import os
from pathlib import Path


class PathUtils:

    def __get_project_root(self):
        try:
            project_root_path = Path(os.path.dirname(os.path.abspath(__file__))).parent
            return project_root_path
        except Exception as e:
            raise Exception("Exception occurred while getting the project root path -->", e)

    def get_config_path(self):
        try:
            config_path = os.path.join(self.__get_project_root(), "config.json")
            return config_path
        except Exception as e:
            raise Exception("Exception occrred while getting the config path -->", e)
