from ..print_util import print_aligning


class BookoutItem:
    def __init__(self):
        self.category = "BookoutItem"
        self.subitems = []

    def __str__(self):
        output = print_aligning("left",self.category)
        for subitem in self.subitems:
            if subitem.value > 0:
                output += subitem.__str__()
        return output
    
    def get_total(self):
        return sum([subitem.value for subitem in self.subitems])

    def get_total_variable(self, total):
        if total > 1:
            return self.category.lower() + "s"
        return self.category.lower()

    def update(self):
        return "implement in your class"

class BookoutSubItem:
    def __init__(self, name, on_bookout = True, value = 0):
        self.name = name
        self.value = value
        self.on_bookout = on_bookout

    def __str__(self):
        quantifier = print_aligning("left", self.get_quantifier())
        subitem = print_aligning("right",self.get_grammar_name())
        return "\n" + quantifier + subitem[len(quantifier):] + "\n"

    def get_quantifier(self):
        return f"{self.value}x"

    def get_grammar_name(self):
        if self.value > 1:
            if self.name[-1].lower() == "y":
                return self.name + "ies"
            return self.name + "s"
        else:
            return self.name
        
    def set_value(self, value):
        self.value = value