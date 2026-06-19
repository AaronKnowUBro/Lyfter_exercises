class Student:
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.spanish = float(spanish)
        self.english = float(english)
        self.social = float(social)
        self.science = float(science)
        self.average = self.calculate_average()

    def calculate_average(self):
        return (self.spanish + self.english + self.social + self.science) / 4

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social Studies": self.social,
            "science": self.science,
            "average": self.average
        }