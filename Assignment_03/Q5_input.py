#Question 5

C = 12.0107
O = 15.9994
H = 1.00794
carbon_no = int(input("ENter the number of carbon atoms : "))
oxygen_no = int(input("ENter the number of Oxygen atoms : "))
hydrogen_no = int(input("ENter the number of Hydrogen atoms : "))

total_weight = C*carbon_no + O*oxygen_no + H*hydrogen_no
print(total_weight)