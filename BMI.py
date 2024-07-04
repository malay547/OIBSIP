import matplotlib.pyplot as plt

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    
    print(f"Your BMI is: {bmi:.2f}")
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    
    print(f"You are categorized as: {category}")
    
    categories = ["Underweight", "Normal weight", "Overweight", "Obese"]
    bmi_values = [0, 0, 0, 0]
    bmi_values[categories.index(category)] = bmi
    
    plt.figure(figsize=(8, 6))
    plt.bar(categories, bmi_values, color=['blue', 'green', 'yellow', 'red'])
    plt.xlabel('BMI Category')
    plt.ylabel('BMI')
    plt.title('Your BMI Category')
    plt.ylim(10, 100)  # Set y-axis scale from 10 to 100
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
