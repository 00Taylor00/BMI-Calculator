print("\033c")

#BMI calculator body
def bmi(weight_kgs, height_ms):
    if height_ms < 1.0 or height_ms > 2.5 or \
    weight_kgs < 20 or weight_kgs > 200:
        return None

    return weight_kgs / height_ms ** 2
#conversion tool for weight lbs to kilograms  
def lbs_to_kg(lbs):
    weight_kgs = lbs * 0.45359
    return weight_kgs
#conversion tool for imperial to metric height   
def footinches_to_m(feet, inch):
    height_ms = (feet*30.34 +inch*2.54)/100
    return height_ms
#allowed response list 
preferred_measurement_allowed = ["kg and m", "kilogram and metres", "kg/m"]


def BMI_start():
    print("Welcome to the BMI calculator")


BMI_start()

valid_age = input("\nAre you over 18 years old? (BMI is not valid for use under this age range)..Y/N   ")
if valid_age.lower() in ["yes", "y"]:

    terminate = False 

    while not terminate:
        cont = input("\n\nWould you like to calculate your BMI!")
        if cont.lower() in ["yes", "y", "yes please", "please"]:
            preferred_measurement = input("""
            Would you like to use Kg and Metres (Kg/M)or 
            Feet/Inches and pounds (Ft/In/Lbs)?""")
            
            if preferred_measurement.lower() in preferred_measurement_allowed:
                weight_kgs = float(input("\nPlease enter your weight in Kgs.."))
                height_ms = float(input("\nPlease enter your height in metres..."))
            else:
                feet = float(input("\nPlease enter your height in feet.."))
                inch = float(input("\nand how many inches?..."))
                height_ms = footinches_to_m(feet, inch)
                lbs = float(input("\nPlease enter your weight in lbs...."))
                weight_kgs = lbs_to_kg(lbs)
        
            calculated_bmi = float(bmi(weight_kgs, height_ms))
            if calculated_bmi <= 18.5:
                print("\nYou are defined as underweight")
                print(bmi(weight_kgs, height_ms))

            elif calculated_bmi > 18.5 and calculated_bmi < 24.9:
                print("'\nYou are defined as having a healthy weight")
                print(bmi(weight_kgs, height_ms))

            elif calculated_bmi >= 25 and calculated_bmi < 29.9:
                print("\nYou are defined as overweight")
                print(bmi(weight_kgs, height_ms))

            elif calculated_bmi >= 30 and calculated_bmi < 39.9:
                print("\nYou are defined as obese")
                print(bmi(weight_kgs, height_ms))

            elif calculated_bmi >= 40:
                print("\nYou are defined as severly obese")
                print(bmi(weight_kgs, height_ms))

        else:
            print("\n\nThank you!")
            terminate = True
else:
    print("\nCome back when you are a little bit older!")
