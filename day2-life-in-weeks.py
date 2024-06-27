#Calculate life in weeks, with presuming max age is 90 years old
age=input("What is your current age? ")
max_age=90
age_int=int(age)
years_left=max_age-age_int

days_left=years_left*365
weeks_left=years_left*52
months_left=years_left*12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")


