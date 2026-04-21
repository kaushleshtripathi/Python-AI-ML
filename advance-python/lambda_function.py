# lambda arguments: expression

add = lambda x, y: x + y
print(add(2, 3))

grade = lambda score: "Pass" if score >= 50 else "Fail"
print(grade(60))

multiply = lambda x: lambda y: x * y
double = multiply(2)
print(double(5))