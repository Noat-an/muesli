import yaml


class Person(yaml.YAMLObject):

    yaml_tag = "!Person"
    yaml_loader = yaml.SafeLoader

    def __init__(self, age, first_name, last_name):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"
