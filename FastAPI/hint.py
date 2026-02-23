import typing

# Here we might get errors because this is dynamic typing.
def division(x,y):
    return x/y

#Now we write same winction by adding types to the params.
#Now -> is used to hint the return type for a function.

def division_typing(a:float,b:float) -> float:
    return a/b

l1:list=[12,23,45,"Hello"]
print(l1)

le:typing.List[int]=[12,56,78]
print(le)
le.append(3.0)
print(le)# Here it won't raise any error at all.