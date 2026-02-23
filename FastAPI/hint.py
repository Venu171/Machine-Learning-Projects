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

# The typing module is used for annotating 
# the data types of the variables and writing the 
# return types of the functions and expressions

lst_of_str:typing.List[str]=["Hello","World"]
# lst_of_str.append(3)
print(lst_of_str)

#mixed data types using Union.
lst_of_mixed_data_types:typing.Tuple[typing.Union[int,str]]=[1,2,"Hello"]
lst_of_mixed_data_types.append(6)
print(lst_of_mixed_data_types)

# Any type from typing.Any
a:typing.Any=3
a="hello"
print(a)

# Optional type is used for either the data type or None
b=typing.Optional[str]
b=None
print(b)