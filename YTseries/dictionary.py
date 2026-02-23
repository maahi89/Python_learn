dict={"name":"mahitha",
        "age":22,
        "id":12,
        "course":"python"
      }
dict2={1:"one",
       2:"two",
       3:"three"}
print(dict)
print(dict["name"])
dict["age"]=23
print(dict)
dict.get("age")
total={**dict,**dict2}  #adds 2 dictionaries together
print(total)
