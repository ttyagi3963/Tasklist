

password = input("Enter your password: ")
result= {}


result["correctLength"]=  len(password) >= 8

result["oneDigit"]=(any(c.isdigit() for c in password))
result["oneUpper"]=(any(c.isupper() for c in password))

print(result)
print(result.values())
print(result.keys())

for k,v in result.items():
    print(f"1 - {k}")


if all(result.values()) :
    print("Password is valid")
else:
    print("Password is not valid")