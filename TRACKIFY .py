import csv
import os
from datetime import datetime, timedelta


# ==================== EXPENSE TRACKER ====================
def expense_tracker():
  FILE = "expenses.csv"

#initializing a file
  def initialize_file():
    with open(FILE, "w", newline="") as f:
      writer = csv.writer(f)
      writer.writerow(["Date", "Category", "Amount", "Description"])

#------------------------------------------------------------------------------

#adding new expenses
  def add_expense():
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    date = datetime.now().strftime("%d-%m-%y")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!\n")

#------------------------------------------------------------------------------

#viewing previous expenses
  def view_expenses():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

#------------------------------------------------------------------------------

#calculating total expenses
  def total_expense():
    total = 0
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            total += float(row[2])
    print(f"\nTotal Expense: ₹{total}\n")

#------------------------------------------------------------------------------

#using the app
  def main():
    initialize_file()
    while True:
        print("\n╔════════════════════════════════╗")
        print("║    💰 Expense Tracker 💰       ║")
        print("╚════════════════════════════════╝")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Expense")
        print("4. Back to Main Menu")
        print("5. Exit Application")
        print("─" * 34)

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("\n🔙 Returning to Main Menu...\n")
            return "menu"
        elif choice == "5":
            print("\n👋 Thank you for using Expense Tracker!\n")
            return "exit"
        else:
            print("❌ Invalid choice! Please enter 1-5.\n")
  main()
  initialize_file()

# ==================== FITNESS TRACKER ====================
def fitness_tracker():
  print("Fitness Tracker App!")

# Weekly storage for multiple days
  weekly_data = {}

# Calories per step constant
  CALORIES_PER_STEP = 0.04

  while True:

    print("\n===============================")
    print("📌 Fitness Tracker Main Menu")
    print("1. Start Daily Tracking")
    print("2. View Weekly Summary")
    print("3. Exit")
    print("===============================")

    main_choice = input("Enter your choice: ")

    if main_choice == "1":

        date = input("\n📅 Enter today's date (YYYY-MM-DD): ")

        # Initialize daily values
        steps_today = 0
        water_today = 0
        calories_today = 0
        workouts_today = []
        bmi_value = None

        while True:
            print("\n-------------------------")
            print(f"📆 Daily Menu ({date})")
            print("1. Add Steps")
            print("2. Add Water Intake")
            print("3. Log Workout")
            print("4. Calculate BMI")
            print("5. View Daily Progress")
            print("6. Save Day & Return to Main Menu")
            print("-------------------------")

            choice = input("Enter your choice: ")

            # -----------------------------
            # Add Steps
            # -----------------------------
            if choice == "1":
                steps = int(input("Enter steps to add: "))
                steps_today += steps
                calories_today += steps * CALORIES_PER_STEP
                print("✔ Steps updated!")

            # -----------------------------
            # Add Water
            # -----------------------------
            elif choice == "2":
                water = int(input("Enter glasses of water: "))
                water_today += water
                print("✔ Water intake updated!")

            # -----------------------------
            # Log Workout
            # -----------------------------
            elif choice == "3":
                print("\n🏋️ Log Workout")
                name = input("Workout name: ")
                duration = float(input("Duration (minutes): "))
                calories = float(input("Calories burned: "))

                workouts_today.append({
                    "name": name,
                    "duration": duration,
                    "calories": calories
                })

                calories_today += calories
                print("💪 Workout logged!")

            # -----------------------------
            # BMI Calculation
            # -----------------------------
            elif choice == "4":
                weight = float(input("Enter weight (kg): "))
                height = float(input("Enter height (meters): "))
                bmi_value = weight / (height ** 2)
                print(f"📏 Your BMI is {round(bmi_value, 2)}")

            # -----------------------------
            # View Daily Progress
            # -----------------------------
            elif choice == "5":
                print("\n===== 📊 Daily Summary =====")
                print(f"📅 Date: {date}")
                print(f"🏃 Steps: {steps_today}")
                print(f"💧 Water: {water_today} glasses")
                print(f"🔥 Total Calories Burned: {round(calories_today)} kcal")

                print("\n🏋️ Workouts:")
                if workouts_today:
                    for w in workouts_today:
                        print(f" - {w['name']} | {w['duration']} min | {w['calories']} kcal")
                else:
                    print("   No workouts recorded.")

                if bmi_value is not None:
                    print(f"\n📏 BMI: {round(bmi_value, 2)}")
                else:
                    print("\n📏 BMI: Not calculated yet.")

            # -----------------------------
            # Save Day & Exit to Main Menu
            # -----------------------------
            elif choice == "6":
                weekly_data[date] = {
                    "steps": steps_today,
                    "water": water_today,
                    "calories": calories_today,
                    "workouts": workouts_today,
                    "bmi": bmi_value
                }
                print(f"💾 Day saved for {date}! Returning to main menu...")
                break

            else:
                print("❌ Invalid choice. Try again.")

    # =====================================
    # WEEKLY SUMMARY
    # =====================================
    elif main_choice == "2":
        print("\n===== 📅 Weekly Summary =====")

        if not weekly_data:
            print("No daily records available yet!")
        else:
            total_steps = 0
            total_water = 0
            total_calories = 0

            for date, day in weekly_data.items():
                total_steps += day["steps"]
                total_water += day["water"]
                total_calories += day["calories"]

            print(f"🏃 Total Steps: {total_steps}")
            print(f"💧 Total Water Intake: {total_water} glasses")
            print(f"🔥 Total Calories Burned: {round(total_calories)} kcal")

            print("\n📌 Daily Breakdown:")
            for date, day in weekly_data.items():
                print(f"\n📅 {date}")
                print(f"  Steps: {day['steps']}")
                print(f"  Water: {day['water']} glasses")
                print(f"  Calories Burned: {round(day['calories'])} kcal")
                print("  Workouts:")
                if day["workouts"]:
                    for w in day["workouts"]:
                        print(f"    - {w['name']} | {w['duration']} min | {w['calories']} kcal")
                else:
                    print("    No workouts recorded.")

                if day["bmi"] is not None:
                    print(f"  BMI: {round(day['bmi'], 2)}")

    # =====================================
    # EXIT
    # =====================================
    elif main_choice == "3":
        print("👋 Exiting... Stay fit and consistent!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
# ==================== DAILY TRACKER ====================
def daily_tracker():
    print("🏋️ Welcome to the Daily Tracker App!")

    steps_goal = int(input("Enter your daily step goal: "))
    water_goal = int(input("Enter your daily water intake goal (in glasses): "))
    sleep_goal = float(input("Enter your daily sleep goal (hours): "))
    study_goal = float(input("Enter your daily study goal (hours): "))
    screen_goal = float(input("Enter your maximum allowed screen time (hours): "))

    steps_today = 0
    water_today = 0
    sleep_today = 0
    study_today = 0
    screen_today = 0
    calories_today = 0

    CALORIES_PER_STEP = 0.04

    while True:
        print("\n-------------------------")
        print("📌 Daily Tracker Menu")
        print("1. Add Steps")
        print("2. Add Water Intake")
        print("3. Add Sleep Hours")
        print("4. Add Study Hours")
        print("5. Add Screen Time")
        print("6. View Progress")
        print("7. Back to Main Menu")
        print("8. Exit Application")
        print("-------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            steps = int(input("Enter steps to add: "))
            steps_today += steps
            calories_today = steps_today * CALORIES_PER_STEP
            print("✔ Steps updated and calories recalculated!")

        elif choice == "2":
            water = int(input("Enter glasses of water: "))
            water_today += water
            print("✔ Water intake updated!")

        elif choice == "3":
            sleep = float(input("Enter hours of sleep: "))
            sleep_today += sleep
            print("😴 Sleep logged!")

        elif choice == "4":
            study = float(input("Enter hours studied: "))
            study_today += study
            print("📚 Study hours updated!")

        elif choice == "5":
            screen = float(input("Enter screen time (hours): "))
            screen_today += screen
            print("📱 Screen time updated!")

        elif choice == "6":
            print("\n===== 📊 Progress Summary =====")
            print(f"🏃 Steps:        {steps_today} / {steps_goal}")
            print(f"🔥 Calories:     {round(calories_today)} kcal burned")
            print(f"💧 Water:        {water_today} / {water_goal} glasses")
            print(f"😴 Sleep:        {sleep_today} / {sleep_goal} hours")
            print(f"📚 Study:        {study_today} / {study_goal} hours")
            print(f"📱 Screen Time:  {screen_today} / {screen_goal} hours (max allowed)")

            print("\n===== 🎯 Goal Status =====")
            if steps_today >= steps_goal:
                print("🏃 Steps Goal ✔")
            if calories_today >= (steps_goal * CALORIES_PER_STEP):
                print("🔥 Calories Goal ✔")
            if water_today >= water_goal:
                print("💧 Water Goal ✔")
            if sleep_today >= sleep_goal:
                print("😴 Sleep Goal ✔")
            if study_today >= study_goal:
                print("📚 Study Goal ✔")
            if screen_today <= screen_goal:
                print("📱 Screen Time Under Control ✔")
            elif screen_today > screen_goal:
                print("⚠ Too Much Screen Time!")

        elif choice == "7":
            print("\n🔙 Returning to Main Menu...\n")
            return "menu"

        elif choice == "8":
            print("👋 Exiting... Stay healthy and productive!")
            return "exit"

        else:
            print("❌ Invalid choice. Please try again.")


# ==================== HEALTH TRACKER ====================
def health_tracker():
    USER_FILE = "user_info.csv"
    TABLETS_FILE = "tablets.csv"
    APPOINTMENTS_FILE = "appointments.csv"
    LAB_RESULTS_FILE = "lab_results.csv"
    VACCINATIONS_FILE = "vaccinations.csv"
    ALLERGIES_FILE = "allergies.csv"
    MEDICAL_HISTORY_FILE = "medical_history.csv"
    PERIOD_DATES_FILE = "period_dates.csv"

    def load_user_info():
        if os.path.exists(USER_FILE):
            with open(USER_FILE, 'r') as f:
                reader = csv.reader(f)
                data = list(reader)
                if len(data) > 0:
                    age = data[0][0]
                    gender = data[0][1]
                    return age, gender
        return None, None

    def save_user_info(age, gender):
        with open(USER_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([age, gender])

    def load_tablets():
        tablets = []
        if os.path.exists(TABLETS_FILE):
            with open(TABLETS_FILE, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 2:
                        tablets.append(row)
        return tablets

    def save_tablets(tablets):
        with open(TABLETS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            for tablet in tablets:
                writer.writerow(tablet)

    def load_appointments():
        appointments = []
        if os.path.exists(APPOINTMENTS_FILE):
            with open(APPOINTMENTS_FILE, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 6:
                        appointments.append(row)
        return appointments

    def save_appointments(appointments):
        with open(APPOINTMENTS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            for apt in appointments:
                writer.writerow(apt)

    def load_lab_results():
        results = []
        if os.path.exists(LAB_RESULTS_FILE):
            with open(LAB_RESULTS_FILE, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 5:
                        results.append(row)
        return results

    def save_lab_results(results):
        with open(LAB_RESULTS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            for result in results:
                writer.writerow(result)

    def load_vaccinations():
        vaccinations = []
        if os.path.exists(VACCINATIONS_FILE):
            with open(VACCINATIONS_FILE, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 5:
                        vaccinations.append(row)
        return vaccinations

    def save_vaccinations(vaccinations):
        with open(VACCINATIONS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            for vac in vaccinations:
                writer.writerow(vac)

    def load_allergies():
        allergies = []
        if os.path.exists(ALLERGIES_FILE):
            with open(ALLERGIES_FILE, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 3:
                        allergies.append(row)
        return allergies

    def save_allergies(allergies):
        with open(ALLERGIES_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            for allergy in allergies:
                writer.writerow(allergy)

    def load_medical_history():
        history = []
        if os.path.exists(MEDICAL_HISTORY_FILE):
            with open(MEDICAL_HISTORY_FILE, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 5:
                        history.append(row)
        return history

    def save_medical_history(history):
        with open(MEDICAL_HISTORY_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            for record in history:
                writer.writerow(record)

    def load_period_dates():
        dates = []
        if os.path.exists(PERIOD_DATES_FILE):
            with open(PERIOD_DATES_FILE, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 1:
                        dates.append(row[0])
        return dates

    def save_period_dates(dates):
        with open(PERIOD_DATES_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            for date in dates:
                writer.writerow([date])

    def setup():
        age, gender = load_user_info()

        if age is None:
            print("\n--- First Time Setup ---")
            age = input("Enter your age: ")

            if int(age) > 40:
                choice = input("Check diabetes risk? (y/n): ")
                if choice.lower() == 'y':
                    check_diabetes()

            gender = input("Enter gender (male/female): ").lower()
            save_user_info(age, gender)

            if gender == 'female':
                add_period_dates()
        else:
            print(f"\nWelcome back! Age: {age}, Gender: {gender}")

        return age, gender

    def check_diabetes():
        print("\n--- Diabetes Risk Check ---")
        score = 0

        weight = input("Weight (kg): ")
        height = input("Height (m): ")

        try:
            bmi = float(weight) / (float(height) * float(height))
            print(f"BMI: {bmi:.2f}")
            if bmi > 25:
                score = score + 1
        except:
            pass

        fam = input("Family history of diabetes? (y/n): ")
        if fam.lower() == 'y':
            score = score + 1

        thirst = input("Excessive thirst? (y/n): ")
        if thirst.lower() == 'y':
            score = score + 1

        tired = input("Very tired? (y/n): ")
        if tired.lower() == 'y':
            score = score + 1

        peeing = input("Frequent urination? (y/n): ")
        if peeing.lower() == 'y':
            score = score + 1

        sugar = input("Random sugar level (mg/dL): ")
        try:
            if float(sugar) > 200:
                score = score + 2
        except:
            pass

        print("\n--- Risk Level ---")
        if score >= 4:
            print("HIGH RISK - Consult a doctor")
        elif score >= 2:
            print("MEDIUM RISK - Monitor regularly")
        else:
            print("LOW RISK - Stay healthy!")

    def add_period_dates():
        print("\nEnter last 3 period dates (YYYY-MM-DD)")
        dates = []

        for i in range(3):
            date = input(f"Date {i + 1}: ")
            dates.append(date)

        save_period_dates(dates)
        print("Dates saved!")

    def show_period_info(gender):
        if gender != 'female':
            print("Not applicable")
            return

        dates = load_period_dates()

        print("\n--- Period Dates ---")
        if len(dates) == 0:
            print("No dates recorded")
            return

        for date in dates:
            print(date)

        if len(dates) >= 2:
            date1 = datetime.strptime(dates[-2], "%Y-%m-%d").date()
            date2 = datetime.strptime(dates[-1], "%Y-%m-%d").date()
            cycle = (date2 - date1).days
            next_date = date2 + timedelta(days=cycle)
            print(f"Next estimated period: {next_date}")

    def check_bp():
        print("\n--- Blood Pressure Check ---")
        sys = input("Systolic (upper): ")
        dia = input("Diastolic (lower): ")

        try:
            sys = int(sys)
            dia = int(dia)

            if sys < 120 and dia < 80:
                print("Status: Normal")
            elif sys < 130:
                print("Status: Elevated")
            elif sys < 140 or dia < 90:
                print("Status: Hypertension Stage 1")
            else:
                print("Status: Hypertension Stage 2")
        except:
            print("Invalid input")

    def manage_tablets():
        while True:
            tablets = load_tablets()

            print("\n--- Tablets ---")
            if len(tablets) == 0:
                print("No tablets added")
            else:
                for i in range(len(tablets)):
                    print(f"{i + 1}. {tablets[i][0]} at {tablets[i][1]}")

            print("\n1. Add  2. Remove  3. Back")
            choice = input("Choose: ")

            if choice == '1':
                name = input("Tablet name: ")
                time = input("Time (HH:MM): ")
                tablets.append([name, time])
                save_tablets(tablets)
                print("Added!")

            elif choice == '2':
                num = input("Tablet number: ")
                try:
                    num = int(num)
                    if num > 0 and num <= len(tablets):
                        tablets.pop(num - 1)
                        save_tablets(tablets)
                        print("Removed!")
                    else:
                        print("Invalid number")
                except:
                    print("Invalid input")

            elif choice == '3':
                break

    def manage_appointments():
        while True:
            appointments = load_appointments()

            print("\n--- Doctor Appointments ---")
            if len(appointments) == 0:
                print("No appointments")
            else:
                for i in range(len(appointments)):
                    apt = appointments[i]
                    status = "Done" if apt[5] == "True" else "Pending"
                    print(f"{i + 1}. [{status}] {apt[0]} - Dr. {apt[2]} ({apt[3]})")
                    print(f"   Reason: {apt[4]}")

            print("\n1. Add  2. Mark Done  3. Remove  4. Back")
            choice = input("Choose: ")

            if choice == '1':
                date = input("Date (YYYY-MM-DD): ")
                time = input("Time (HH:MM): ")
                doctor = input("Doctor name: ")
                specialty = input("Specialty: ")
                reason = input("Reason: ")
                appointments.append([date, time, doctor, specialty, reason, "False"])
                save_appointments(appointments)
                print("Appointment added!")

            elif choice == '2':
                num = input("Appointment number: ")
                try:
                    num = int(num)
                    if num > 0 and num <= len(appointments):
                        appointments[num - 1][5] = "True"
                        save_appointments(appointments)
                        print("Marked done!")
                    else:
                        print("Invalid number")
                except:
                    print("Invalid input")

            elif choice == '3':
                num = input("Appointment number: ")
                try:
                    num = int(num)
                    if num > 0 and num <= len(appointments):
                        appointments.pop(num - 1)
                        save_appointments(appointments)
                        print("Removed!")
                    else:
                        print("Invalid number")
                except:
                    print("Invalid input")

            elif choice == '4':
                break

    def manage_lab_results():
        while True:
            results = load_lab_results()

            print("\n--- Lab Results ---")
            if len(results) == 0:
                print("No lab results")
            else:
                for i in range(len(results)):
                    result = results[i]
                    print(f"{i + 1}. {result[0]} - {result[1]}")
                    print(f"   Result: {result[2]} | Lab: {result[3]}")
                    if result[4]:
                        print(f"   Notes: {result[4]}")

            print("\n1. Add  2. Remove  3. Back")
            choice = input("Choose: ")

            if choice == '1':
                date = input("Test date (YYYY-MM-DD): ")
                test_name = input("Test name: ")
                result = input("Result: ")
                lab_name = input("Lab name: ")
                notes = input("Notes (optional): ")
                results.append([date, test_name, result, lab_name, notes])
                save_lab_results(results)
                print("Lab result added!")

            elif choice == '2':
                num = input("Result number: ")
                try:
                    num = int(num)
                    if num > 0 and num <= len(results):
                        results.pop(num - 1)
                        save_lab_results(results)
                        print("Removed!")
                    else:
                        print("Invalid number")
                except:
                    print("Invalid input")

            elif choice == '3':
                break

    def manage_vaccinations():
        while True:
            vaccinations = load_vaccinations()

            print("\n--- Vaccination Records ---")
            if len(vaccinations) == 0:
                print("No vaccination records")
            else:
                for i in range(len(vaccinations)):
                    vac = vaccinations[i]
                    print(f"{i + 1}. {vac[0]} - {vac[1]}")
                    print(f"   Batch: {vac[2]} | Location: {vac[3]}")
                    if vac[4]:
                        print(f"   Next dose: {vac[4]}")

            print("\n1. Add  2. Remove  3. Back")
            choice = input("Choose: ")

            if choice == '1':
                date = input("Vaccination date (YYYY-MM-DD): ")
                vaccine_name = input("Vaccine name: ")
                batch_no = input("Batch number: ")
                location = input("Location/Hospital: ")
                next_dose = input("Next dose date (optional): ")
                vaccinations.append([date, vaccine_name, batch_no, location, next_dose])
                save_vaccinations(vaccinations)
                print("Vaccination added!")

            elif choice == '2':
                num = input("Vaccination number: ")
                try:
                    num = int(num)
                    if num > 0 and num <= len(vaccinations):
                        vaccinations.pop(num - 1)
                        save_vaccinations(vaccinations)
                        print("Removed!")
                    else:
                        print("Invalid number")
                except:
                    print("Invalid input")

            elif choice == '3':
                break

    def manage_allergies():
        while True:
            allergies = load_allergies()

            print("\n--- Allergies ---")
            if len(allergies) == 0:
                print("No allergies recorded")
            else:
                for i in range(len(allergies)):
                    allergy = allergies[i]
                    print(f"{i + 1}. {allergy[0]} - {allergy[1]}")
                    print(f"   Reaction: {allergy[2]}")

            print("\n1. Add  2. Remove  3. Back")
            choice = input("Choose: ")

            if choice == '1':
                allergen = input("Allergen: ")
                severity = input("Severity (Mild/Moderate/Severe): ")
                reaction = input("Reaction type: ")
                allergies.append([allergen, severity, reaction])
                save_allergies(allergies)
                print("Allergy added!")

            elif choice == '2':
                num = input("Allergy number: ")
                try:
                    num = int(num)
                    if num > 0 and num <= len(allergies):
                        allergies.pop(num - 1)
                        save_allergies(allergies)
                        print("Removed!")
                    else:
                        print("Invalid number")
                except:
                    print("Invalid input")

            elif choice == '3':
                break

    def manage_medical_history():
        while True:
            history = load_medical_history()

            print("\n--- Medical History ---")
            if len(history) == 0:
                print("No medical history")
            else:
                for i in range(len(history)):
                    record = history[i]
                    print(f"{i + 1}. {record[0]} - {record[1]}: {record[2]}")
                    print(f"   Hospital: {record[3]}")
                    if record[4]:
                        print(f"   Notes: {record[4]}")

            print("\n1. Add  2. Remove  3. Back")
            choice = input("Choose: ")

            if choice == '1':
                date = input("Date (YYYY-MM-DD): ")
                record_type = input("Type (Surgery/Condition/Injury): ")
                condition = input("Condition/Procedure name: ")
                hospital = input("Hospital/Clinic: ")
                notes = input("Notes (optional): ")
                history.append([date, record_type, condition, hospital, notes])
                save_medical_history(history)
                print("Medical record added!")

            elif choice == '2':
                num = input("Record number: ")
                try:
                    num = int(num)
                    if num > 0 and num <= len(history):
                        history.pop(num - 1)
                        save_medical_history(history)
                        print("Removed!")
                    else:
                        print("Invalid number")
                except:
                    print("Invalid input")

            elif choice == '3':
                break

    age, gender = setup()

    while True:
        print("\n========================================")
        print("      HEALTH TRACKER MENU")
        print("========================================")
        print("1. Manage Tablets")
        print("2. Period Info")
        print("3. Check BP")
        print("4. Doctor Appointments")
        print("5. Lab Results")
        print("6. Vaccination Records")
        print("7. Allergies")
        print("8. Medical History")
        print("9. Back to Main Menu")
        print("10. Exit Application")

        choice = input("\nChoose: ")

        if choice == '1':
            manage_tablets()
        elif choice == '2':
            show_period_info(gender)
        elif choice == '3':
            check_bp()
        elif choice == '4':
            manage_appointments()
        elif choice == '5':
            manage_lab_results()
        elif choice == '6':
            manage_vaccinations()
        elif choice == '7':
            manage_allergies()
        elif choice == '8':
            manage_medical_history()
        elif choice == '9':
            print("\n🔙 Returning to Main Menu...\n")
            return "menu"
        elif choice == '10':
            print("\nGoodbye! Stay healthy!")
            return "exit"
        else:
            print("Invalid choice")


# ==================== MAIN MENU ====================
def main_menu():
    while True:
        print("\n" + "=" * 60)
        print("         🎯 TRACKIFY UNIFIED TRACKER APPLICATION 🎯")
        print("=" * 60)
        print("\nSelect which tracker to use:")
        print("1. 💰 Expense Tracker")
        print("2. 🏋️  Fitness Tracker")
        print("3. 📊 Daily Tracker")
        print("4. 🏥 Health Tracker")
        print("5. ❌ Exit Application")
        print("-" * 60)

        choice = input("\nEnter your choice (1-5): ").strip()

        result = None

        if choice == '1':
            print("\n🔄 Loading Expense Tracker...\n")
            result = expense_tracker()
        elif choice == '2':
            print("\n🔄 Loading Fitness Tracker...\n")
            result = fitness_tracker()
        elif choice == '3':
            print("\n🔄 Loading Daily Tracker...\n")
            result = daily_tracker()
        elif choice == '4':
            print("\n🔄 Loading Health Tracker...\n")
            result = health_tracker()
        elif choice == '5':
            print("\n" + "=" * 60)
            print("   👋 Thank you for using TRACKIFY Unified Tracker Application!")
            print("        Stay healthy, stay productive! 💪")
            print("=" * 60 + "\n")
            break
        else:
            print("\n❌ Invalid choice! Please enter 1-5.")

        if result == "exit":
            print("\n" + "=" * 60)
            print("   👋 Thank you for using TRACKIFY Unified Tracker Application!")
            print("        Stay healthy, stay productive! 💪")
            print("=" * 60 + "\n")
            break


# ==================== RUN APPLICATION ====================
if __name__ == "__main__":
    main_menu()