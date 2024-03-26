import function_library as fl

e = fl.Equat_object('equat','f(x)=x**2')

print(e.object_family)
print(e.equation_string)

e.interpretation_of_string_input() #interpreting the string input

#now I want to print out math operators and their positions

math_object = e.equation_interpretation[0]
print(math_object.obj_type,math_object.symbol, math_object.position_in_string)
