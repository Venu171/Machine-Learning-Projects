# Here we might get errors because this is dynamic typing.
def division(x,y):
    return x/y

#Now we write same winction by adding types to the params.
#Now -> is used to hint the return type for a function.
def division_typing(a:float,b:float) -> float:
    return a/b
