def ptbn(a, b):
    if a == 0:
        if b == 0:
            return "Vô số nghiệm"
        else:
            return "Vô nghiệm"
    else:
        x = -b / a
        return f"Nghiệm x = {x}"

a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))

print(ptbn(a,b))
