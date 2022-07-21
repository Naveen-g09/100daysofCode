age = input("what is your current age: ")

current_age = 365*int(age)

total_age_days = 32850 - current_age
total_age_weeks = total_age_days/7
total_age_months = total_age_days/30
print(f"You have { total_age_days } days { total_age_weeks} weeks {total_age_months} months left")
