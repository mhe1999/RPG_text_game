class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop


    def get_name(self):
        return self.name

    def get_descrption(self):
        return self.description


    def get_type(self):
            return self.type


    def get_prop(self):
        return self.prop
