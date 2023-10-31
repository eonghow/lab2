def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI using the formula
    bmi = weight / (height * height)

    # Display calculated BMI
    print("BMI = " + str(bmi))

    # Determine weight classification based on BMI value
    if bmi < 18.5:
        print("Under weight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("Normal weight")
        return 0
    else:
        print("Over weight")
        return 1

if __name__== "__main__":
    calculate_bmi(weight=60, height=1.53)
