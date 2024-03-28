math_operators = {'+', '-', '*', '/', '**', '%', '//'}
math_object_declarations = {'equat'}
attribute_declarations = {'var', 'const'}

'''
object types (obj_type):
    equat -> math object, this object is an equation
    math_op -> math operator, mathematical operator inside an equation
'''


def classify_line(string_input, object_number): #the beginning of a line (first 2 strings)should indicate what kind of input is given
#The object number determines the family of the object.
#It will be created when a new line is entered and is unique to that object
    if string_input[0] == '=': #calculation
        calc_obj = Calc_object(object_number, string_input)
        #calc_obj.interpretation_of_string_input()
        #last line has still some issues to be solved, see Calc_object class comment
        
    if string_input[0:1]=='eq': #equation object
        eq_obj = Equat_object(object_number, string_input)
        eq_obj.interpretation_of_string_input()
        #last two lines might be pulled out of the condition, lets check this later
        
class Calc_object:
    def __init__(self,object_family, equation_string):
        self.object_family = object_family
        self.calculation_string = equation_string
        self.calculation_interpretation = []

    def calculate():
        return eval(equation_string[1:])

    def interpretation_of_string_input(self):
        for position, element in enumerate(self.calculation_string):   #the attributes of the math objects are variables, constants and mathematical operators
            if element in math_operators:
                element = Math_operator('math_op',element,position,self.object_family, self.equation_string)
                self.equation_interpretation.append(element)
            if element.isdigit():
                pass
                #element = Digit()
                #Problem here is that Digit class has to be subclass of both equation and calculation class
                
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
                element = Math_operator('math_op',element,position,self.object_family, self.equation_string)
                self.equation_interpretation.append(element)
                
class Math_operator(Equat_object):
    #The math operator is now a subclass of Equat_object.
    #The math operator belongs to the object family, for example "equation1"
    #We now have to give this object the corresponding mathematical symbol, and save its position in the string
    def __init__(self, obj_type, element_str, position_in_string,object_family, equation_string):
        super().__init__(object_family, equation_string) #every math operator is used within an equation. Therefore the math operators will inherit the particular equation and the equation in string format from the Equat_object class
        self.obj_type = 'math_op'
        self.symbol = element_str
        self.position_in_string = position_in_string
        

class Digit(Equat_object):
    pass
    
