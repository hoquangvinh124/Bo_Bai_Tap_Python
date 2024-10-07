def BMI(height,weight):
    return weight/(height**2)

def Classify(bmi):
    match bmi:
        case bmi if bmi < 18.5:
            return "Thin"
        case bmi if bmi <= 24.9:
            return "Normal"
        case bmi if bmi <= 29.9:
            return "Slightly Fat"
        case bmi if bmi <= 34.9:
            return "Obesity level 1"
        case bmi if bmi <= 39.9:
            return "Obesity level 2"
        case _:
            return "Obesity level 3"
def RiskOfDisease(bmi):
    match bmi:
        case bmi if bmi < 18.5:
            return "Low"
        case bmi if bmi <= 24.9:
            return "Normal"
        case bmi if bmi <= 29.9:
            return "High"
        case bmi if bmi <= 34.9:
            return "High"
        case bmi if bmi <= 39.9:
            return "Very High"
        case _:
            return "Danger"

height=float(input("Nhập chiều cao:"))
weight=float(input("Nhập cân nặng:"))
bmi=BMI(height,weight)
print("BMI =",bmi)
print("Phân loại =", Classify(bmi))
print("Nguy cơ =", RiskOfDisease(bmi))