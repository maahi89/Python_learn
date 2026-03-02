"""
**kwargs allows a function to accept any number of keyword arguments.
 ** → collects keyword arguments into dictionary
 ** → key-value pairs → dictionar
"""


def profile(**kwargs):
    print(kwargs)
profile(name="mahitha" , age=24, role="developer")



def profile(**name):
    for key, value in name.items():
        print(f"{key}: {value}")
name=input("Enter your name: ")
age=int(input("Enter your age: "))  
role=input("Enter your role: ")
profile(name=name, age=age, role=role)




def create_user(**data):
    required_fields = ["name", "age", "email"]
    for field in required_fields:
        if field not in data:
            print(f"Error: Missing required field '{field}'")
            return
    print("User created successfully", data)
create_user(name="mahitha", age=24, email="mahitha@example.com")



def add_items(items):
    items.append(100)
    return items
new_list=[1,2,3,4]  
print(add_items(new_list))   #[1, 2, 3, 4, 100]


