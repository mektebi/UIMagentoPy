import names

class MainParameter:

    def namegenerator(self):
        name = names.get_first_name()
        return name

    def surnamegenerator(self):
        surname = names.get_last_name()
        return surname

    def emailgenerator(self):
        email= self.namegenerator() + self.surnamegenerator() + "@yopmail.com"
        return email