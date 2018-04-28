class ProgrammingLanguage:
    def __init__(self, name="", typing="", is_dynamic="", year=0):
        self.name = name
        self.typing = typing
        self.is_dynamic = is_dynamic
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.is_dynamic,
                                                                           self.year)

    def __repr__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.is_dynamic,
                                                                           self.year)

    def print_name(self):
        print(self.name)

    def is_dynamic(self):
        if self.is_dynamic() is True:
            return True
        else:
            return False


languages = [ProgrammingLanguage("Ruby", "Dynamic", True, 1995), ProgrammingLanguage("Python", "Dynamic", True, 1991),
             ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

for language in languages:
    print(language)

print("The dynamically typed languages are:")
dynamic_languages = [str(language).split(",")[0] for language in languages if language.is_dynamic]
for language in dynamic_languages:
    print(language)

