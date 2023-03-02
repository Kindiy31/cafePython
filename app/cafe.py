from app.errors import checkVaccine


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        response = checkVaccine(visitor)
        if response is True:
            return (f"Welcome to {self.name}")
        else:
            return (response)
