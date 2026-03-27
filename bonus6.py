from modules import bonus_utils

feet_inches = input("enter feet and inches:").strip()

f , i  = bonus_utils.splitter(feet_inches)
result = bonus_utils.convert(f, i)

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")


FREEZING_POINT = 0
BOILING_POINT = 100

def water_state(temperature):


    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"
