import function_library as fl

e = fl.Equat_object('equat','f(x)=x**2')

print(e.object_family)
print(e.equation_string)

e.interpretation_of_string_input() #interpreting the string input

#now I want to print out math operators and their positions

math_object = e.equation_interpretation[0]
print(math_object.obj_type)
print(math_object.symbol)
print(math_object.position_in_string)
print(math_object.object_family)
print(math_object.equation_string)


math_object = e.equation_interpretation
for element in math_object:
    print(element.symbol)
