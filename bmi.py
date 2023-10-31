def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI using the formula
    bmi = weight / (height * height)

    # Display calculated BMI
    print("BMI = " + str(bmi))

    # Determine weight classification based on BMI value
    if bmi < 18.5:
        print("Weight Classification: -1")
    elif 18.5 <= bmi <= 25.0:
        print("Weight Classification: 0")
    else:
        print("Weight Classification: 1")


calculate_bmi(weight=57, height=1.73)
