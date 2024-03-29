math_operators = {'+', '-', '*', '/', '**', '%', '//', '='}
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
        return Calc_object(object_number, string_input)
        #calc_obj.interpretation_of_string_input()
        #above line has still some issues to be solved, see Calc_object class comment
    
    if string_input[0:1]=='eq': #equation object
        eq_obj = Equat_object(object_number, string_input)
        eq_obj.interpretation_of_string_input()
        #last two lines might be pulled out of the condition, lets check this later
        
class Calc_object:
    def __init__(self,object_family, calculation_string):
        self.object_family = object_family
        self.calculation_string = calculation_string
        self.calculation_interpretation = []

    def calculate(self):
        self.result = eval(self.calculation_string[1:])

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
        self.operators=[]
        self.terms = []
        self.equation_syntax_correct = True
    #def attribute_type:
    #    pass

    def interpretation_of_string_input(self):
        for operator in math_operators:
            self.operator_positions = self.equation_string.find(operator)
            if self.operator_positions != -1:
                operator = Math_operator('math_op',operator,position,self.object_family, self.equation_string)
                operator.position_in_string = self.equation_string.find(operator)
                self.operators.append(operator)
            else:
                self.equation_syntax_correct = False
                print('Not an equation')

        self.operators.sort(lambda = x : x.position_in_string) #Making sure that the operators are in correct order

        current_read = 0 #read the string input starting from zero
        
        for index, element in enumerate(self.operators):
            if self.operators[index].position_in_string >= current_read:
                term = self.equation_string[current_read:self.operators[index].position_in_string]
            else:
                term = self.equation_string[self.operators[index].position_in_string+len(operators[index].symbol):] #the last term
            print(term)
            if term != "":
                self.terms.append(term)
            current_read=operators[index].position_in_string #setting the current reading position to the operator position inside the string
            current_read+=len(operators[index].symbol)#skip the operators

'''
To do:
I have to introduce a subclass "term" to the Equat object class so that I can manipulate terms and store information about them.
'''            

        
        for position, element in enumerate(operator_positions):
            if position == 0 and operator_positions[0] != 0: #if the equation does not start with an operator (like a sum for example)
                term = self.string_input[0:element]
            elif position == 0 and operator_positions[0] == 0: #if the equation starts with an operator
                term = self.string_input[len():operator_positions[1]]
        for position, element in enumerate(self.equation_string):   #the attributes of the math objects are variables, constants and mathematical operators
            if element.isdigit():
                self.equation_interpretation.append(element)
                .insert(2, 'x')


#                self.equation_interpretation.append(element)




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
    
