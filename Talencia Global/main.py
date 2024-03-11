"""
Write a program to accept name, empId, basic, special allowances, percentage of bonus and monthly tax saving investments.

The gross monthly salary is basic + special allowances.
The gross annual salary also includes the bonus
 Compute the annual salary.

Compute the annual net salary, by deducting taxes as suggested
a. Income upto 2.5 lakhs – exempted
b. Income from 2.5 lakhs to 5 lakhs – 5%
c. Income from 5 lakhs to 10 lakhs – 20%
d. Income from 10 lakhs onwards – 30%
However, if there is any tax saving investment, then there is further exemption of upto 1.5 lakhs annually. This would mean that by having tax saving investments of about 1.5 lakhs, an income of 4 lakhs is non-taxable.
Display the annual gross, annual net and tax payable.
"""

name = input("enter name: ")
empID = input("enter empID: ")
basic = int(input("enter basic salary: "))
special_allowances = int(input("enter special: "))
perc_of_bonus = int(input("enter perc bonus: "))/100
monthly_tax_saving = int(input("monthly tax saving: "))

#calculating annual
gross_monthly = (basic+special_allowances)
gross_annual = gross_monthly*12 + (gross_monthly*12)*perc_of_bonus
yearly_tax_saving = monthly_tax_saving*12

#tax Excemption
if yearly_tax_saving<=150000:
    gross_annual -= yearly_tax_saving
elif yearly_tax_saving>150000:
    gross_annual = gross_annual-150000+yearly_tax_saving

#tax calulation
if gross_annual<=250000:
    print("gross annual: ", gross_annual)
    print("Tax payable", 0)
    print("net annual pay: ", gross_annual)

elif gross_annual>250000 and gross_annual<=500000:
    print("gross annual: ", gross_annual)
    print("tax payable: ", gross_annual*0.05)
    print("net annual pay: ", gross_annual - (gross_annual*0.05))

elif gross_annual>500000 and gross_annual<=1000000:
    print("gross annual: ", gross_annual)
    print("tax payable: ", gross_annual * 0.2)
    print("net annual pay: ", gross_annual - (gross_annual * 0.2))

elif gross_annual > 1000000:
    print("gross annual: ", gross_annual)
    print("tax payable: ", gross_annual * 0.3)
    print("net annual pay: ", gross_annual - (gross_annual * 0.3))
