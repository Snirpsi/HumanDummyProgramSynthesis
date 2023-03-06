class ProgramStats:
    def __init__(self):
        self.executable = None
        self.returnValue = None
        self.endless = None 
        self.ports = None
        self.codeCoverage = None
        self.error_line = None
    def __str__(self):
        attributes = vars(self)
        attribute_strings = [f"{key}: {value}" for key, value in attributes.items()]
        return f"{type(self).__name__}(\n{', '.join(attribute_strings)}\n)"