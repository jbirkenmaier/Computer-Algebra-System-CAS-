math_operators = {'+', '-', '*', '/', '**', '%', '//'}
math_object_declarations = {'equat'}
attribute_declarations = {'var', 'const'}

'''
object types (obj_type):
    equat -> math object, this object is an equation
    math_op -> math operator, mathematical operator inside an equation
'''

class Equat_object: #math objects can be for example equations
    def __init__(self,object_family, equation_string):
        self.object_family = object_family
        self.equation_string = equation_string
        self.equation_interpretation = []

    #def attribute_type:
    #    pass

    def interpretation_of_string_input(self):
        for position, element in enumerate(self.equation_string):   #the attributes of the math objects are variables, constants and mathematical operators
            if element in math_operators:
                element = Math_operator('math_op',element,position)
                self.equation_interpretation.append(element)
                
class Math_operator:
    #The math operator is now a subclass of Equat_object.
    #The math operator belongs to the object family, for example "equation1"
    #We now have to give this object the corresponding mathematical symbol, and save its position in the string
    def __init__(self, obj_type, element_str, position_in_string):
        self.obj_type = 'math_op'
        self.symbol = element_str
        self.position_in_string = position_in_string
        

class Equat_attribute(Equat_object):
    pass
    
