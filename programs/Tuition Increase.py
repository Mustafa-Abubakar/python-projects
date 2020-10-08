tuition_fee = 8000
increase = 0.03
print("This following program displays the projected semester tuition amount for the next 5 years.")
print("-"*90)
print("Nex 5 Years \t\t\t Semester tuition amount")
for year in range(1,6):
    tuition_increase = tuition_fee * increase
    tuition = tuition_increase * year
    total_tuition = tuition_fee + tuition
    print(year, " year/s", "\t\t\t\t", "$",total_tuition)