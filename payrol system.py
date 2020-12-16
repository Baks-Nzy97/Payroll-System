"""This program calculates the nate income then generates a payslip from that information
Company: Kenbright Limited"""


NSSF_RATE = 0.05
INSURANCE_RELIEF = 0.15
TAX_RELIEF = 1408
PERIOD_NAME = "12th 2020 calender month"
PAY_DATE = "29th December 2020"
PERIOD_START_DATE = "01 - DEC - 2020"
PERIOD_END_DATE = "31 - DEC - 2020"


# calculates the basic pay from the normal hours and overtime hours
def b_pay(emp_grade, hours_worked, overtime_hours):
    if emp_grade == "A":
        pay = hours_worked * 1000
        overtime = overtime_hours * 700
    elif emp_grade == "B":
        pay = hours_worked * 700
        overtime = overtime_hours * 500
    else:
        pay = hours_worked * 500
        overtime = overtime_hours * 400

    basic_pay = pay + overtime
    return basic_pay


# states the NHIF contribution depending on the gross pay
def nhif_calculation(gross_pay):
    if 1 >= gross_pay < 6000:
        nhif_contribution = 150
    elif 6000 >= gross_pay < 8000:
        nhif_contribution = 300
    elif 8000 >= gross_pay < 12000:
        nhif_contribution = 400
    elif 12000 >= gross_pay < 15000:
        nhif_contribution = 500
    elif 15000 >= gross_pay < 20000:
        nhif_contribution = 600
    elif 20000 >= gross_pay < 25000:
        nhif_contribution = 750
    elif 25000 >= gross_pay < 30000:
        nhif_contribution = 850
    elif 30000 >= gross_pay < 35000:
        nhif_contribution = 900
    elif 35000 >= gross_pay < 40000:
        nhif_contribution = 950
    elif 40000 >= gross_pay < 45000:
        nhif_contribution = 1000
    elif 45000 >= gross_pay < 50000:
        nhif_contribution = 1100
    elif 50000 >= gross_pay < 60000:
        nhif_contribution = 1200
    elif 60000 >= gross_pay < 70000:
        nhif_contribution = 1300
    elif 70000 >= gross_pay < 80000:
        nhif_contribution = 1400
    elif 80000 >= gross_pay < 90000:
        nhif_contribution = 1500
    elif 90000 >= gross_pay < 100000:
        nhif_contribution = 1600
    else:
        nhif_contribution = 1700

    return int(nhif_contribution)


# sums up the total deductions
def deduction_calculations(gross_pay):
    mortgage = int(input(" Is there any mortgage? If yes; type the value, If No; type a zero: "))
    hosp = int(input(" Is there any HOSP? If yes; type the value, If No; type a zero: "))
    pension = int(input(" Please enter the pension amount: "))
    nhif = nhif_calculation(gross_pay)
    nssf = NSSF_RATE * gross_pay
    helb = int(input(" Please enter the HELB amount to be deducted: "))
    other_deductions = int(input("Please enter any other amount to be deducted: "))

    total_deductions = mortgage + hosp + pension + nhif + nssf + helb + other_deductions
    return total_deductions


# calculates the tax according to the Kenyan Graduated scale
def taxation(taxable_income):
    if 0 >= taxable_income <= 12298:
        tax = 0.1 * 12298
    elif 12298 < taxable_income <= 23885:
        tax = (taxable_income - 12298) * 0.15 + (12298 * 0.1)
    elif 23885 < taxable_income <= 35472:
        tax = (taxable_income - 23885) * 0.2 + (11587 * 0.15) + (12298 * 0.1)
    elif 35472 < taxable_income <= 47059:
        tax = (taxable_income - 35472) * 0.25 + (11587 * 0.2) + (11587 * 0.15) + (12298 * 0.1)
    else:
        tax = (taxable_income - 47059) * 0.3 + (11587 * 0.25) + (11587 * 0.2) + (11587 * 0.15) + (12298 * 0.1)

    total_tax = tax - INSURANCE_RELIEF - TAX_RELIEF

    return total_tax


def main():
    employee_totals = int(input("Enter the total number of employees: "))
    for i in range(employee_totals):
        emp_name = input("Enter the employee's name: ")
        emp_id = input("Enter the employee's ID: ")
        emp_grade = input("Enter employees grade: ")
        while emp_grade not in ('A', 'B', 'C'):
            print("Invalid input")
            emp_grade = input("Enter employees grade: ")
        hours_worked = int(input("Enter the hours_worked: "))
        overtime_hours = float(input("Enter the overtime hours: "))
        TA = int(input("Enter the Transport Allowance: "))
        HA = int(input("Enter the house allowance: "))

        basic_pay = b_pay(emp_grade, hours_worked, overtime_hours)
        gross_pay = basic_pay + TA + HA
        deductions = deduction_calculations(gross_pay)
        taxable_income = gross_pay - deductions
        PAYE = taxation(taxable_income)
        net_pay = taxable_income - PAYE
        
        # Payslip Information
        print("")
        print("Kenbright Payslip")
        print("Employee name: {}".format(emp_name))
        print("Employee ID: {}".format(emp_id))
        print("Employee grade: {}".format(emp_grade))
        print("")
        print("Payroll Processing Information")
        print("Period name: {}".format(PERIOD_NAME))
        print("Pay date: {}".format(PAY_DATE))
        print("Period start date: {}".format(PERIOD_START_DATE))
        print("period end date: {}".format(PERIOD_END_DATE))
        print("")
        print("Earnings")
        print("Basic salary: {}".format(basic_pay))
        print("House Allowance: {}".format(HA))
        print("Transport Allowance: {}".format(TA))
        print("Totals: {}".format(gross_pay))
        print("")
        print("Deductions")
        print("Total Deductions: {}".format(deductions))
        print("")
        print("Net earnings: {}".format(net_pay))
        print("")


if __name__ == '__main__':
    main()
