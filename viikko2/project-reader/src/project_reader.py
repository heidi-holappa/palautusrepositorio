from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_object = toml.loads(content)
        # print("Print in ProjectReader")
        # print(content)
        # print("TOML OBJECT:")
        # print(toml_object)
        name = toml_object['tool']['poetry']['name']
        description = toml_object['tool']['poetry']['description']
        if not description:
            description = "-"
        dependencies = []
        for key in toml_object['tool']['poetry']['dependencies']:
            dependencies.append(key)
        dev_dependencies = []
        for key in toml_object['tool']['poetry']['dev-dependencies']:
            dev_dependencies.append(key)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
