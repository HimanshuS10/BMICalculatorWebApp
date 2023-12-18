import streamlit as st


st.header("BMI Calculator")
def calculate_bmi(weight, height, system='imperial'):
    """
    Calculate BMI using weight and height.
    If the system is 'imperial', weight is in pounds and height is in inches.
    If the system is 'metric', weight is in kilograms and height is in meters.
    BMI = weight / (height ** 2)
    """
    if system == 'imperial':
        bmi = (weight / (height ** 2)) * 703
    elif system == 'metric':
        bmi = weight / (height ** 2)
    else:
        return "Error: Invalid system. Use 'imperial' or 'metric'."

    return bmi

def main():
    # Get user input for the system (imperial or metric)
    user_input = st.text_input("Enter 1 for imperial system and 2 for metric system")

    if user_input == '1':
        # If the user chooses imperial, get weight in pounds and height in inches
        weight = st.number_input("Enter weight (in pounds):")
        if weight <= 0:
            st.write("Error")
            st.write("Weight cannot be 0 or less than zero")
            return weight
        height = st.number_input("Enter height (in inches):")
        if height <= 0:
            st.write("Error")
            st.write("Height cannot be 0 or less than zero")
            return height
        system = 'imperial'
    elif user_input == '2':
        # If the user chooses metric, get weight in kilograms and height in meters
        weight = st.number_input("Enter weight (in kilograms):")
        if weight <= 0:
            st.write("Error")
            st.write("Weight cannot be 0 or less than zero")
            return weight
        height = st.number_input("Enter height (in meters):")
        if height <= 0:
            st.write("Error")
            st.write("Height cannot be 0 or less than zero")
            return height
        system = 'metric'
    else:
        # Handle invalid input
        st.write("Invalid input. Please enter 1 for imperial or 2 for metric.")
        return

    # Calculate BMI based on user input and display the result
    if height == 0 and weight == 0:
        return "Error: Height cannot be zero"
    else:
        bmi_result = calculate_bmi(weight, height, system)
        st.write(f"Calculated BMI: {float(bmi_result)}")
        workout_plan = st.button('Get a workout plan')

    if bmi_result >= 30.0:
        st.write("You are: **Obesity**")
    elif 25.0 <= bmi_result <= 29.9:
        st.write("You are: **Overweight**")
    elif 18.5 <= bmi_result <= 24.9:
        st.write("You are: **Normal**")
    else:
        st.write("You are: **Underweight**")

    if workout_plan:
        st.title("Weekly Gym Workout Plan")

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        for day in days:
            st.subheader(f"**{day}**")

            if day == "Monday":
                st.write("Full Body Strength Training")
                st.write("1. Squats: 3 sets of 8-12 reps")
                st.write("2. Bench Press: 3 sets of 8-12 reps")
                st.write("3. Bent-over Rows: 3 sets of 10-15 reps")
                st.write("4. Overhead Press: 3 sets of 10-15 reps")
                st.write("5. Lunges: 2 sets of 12 reps per leg")
                st.write("6. Plank: 3 sets, hold for 30-60 seconds")

            elif day == "Tuesday":
                st.write("Cardiovascular Exercise")
                st.write("- 30 minutes of brisk walking or jogging")
                st.write(
                    "- 20 minutes of high-intensity interval training (HIIT) on a treadmill or stationary bike")
                st.write("- 45 minutes of cycling")

            elif day == "Wednesday":
                st.write("Active Recovery or Rest")
                st.write("Consider light activities like walking, yoga, or stretching to aid recovery.")

            elif day == "Thursday":
                st.write("Upper Body Strength Training")
                st.write("1. Pull-ups or Lat Pulldowns: 3 sets of 8-12 reps")
                st.write("2. Dumbbell Rows: 3 sets of 10-15 reps per arm")
                st.write("3. Push-ups or Chest Flyes: 3 sets of 10-15 reps")
                st.write("4. Tricep Dips: 2 sets of 12-15 reps")
                st.write("5. Bicep Curls: 2 sets of 12-15 reps")
                st.write("6. Russian Twists: 3 sets of 15 reps per side")

            elif day == "Friday":
                st.write("Cardiovascular Exercise")
                st.write("Choose a different activity than Tuesday. Mix it up to keep things interesting.")

            elif day == "Saturday":
                st.write("Lower Body Strength Training")
                st.write("1. Deadlifts: 3 sets of 8-12 reps")
                st.write("2. Leg Press: 3 sets of 10-15 reps")
                st.write("3. Leg Curls: 3 sets of 12-15 reps")
                st.write("4. Calf Raises: 3 sets of 15-20 reps")
                st.write("5. Plank: 3 sets, hold for 30-60 seconds")

            elif day == "Sunday":
                st.write("Rest or Light Activity")
                st.write(
                    "Allow your body to recover. You can engage in light activities like walking or stretching.")

if __name__ == "__main__":
    main()
