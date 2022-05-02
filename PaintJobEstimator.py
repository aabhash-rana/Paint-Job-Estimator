import math

#  input variables
square_feet = "Enter the wall space in square feet: "
paint_price = "Enter the paint price per gallon: "
gallon_of_paint = "Enter the feet per gallon: "
labor_hours_per_gallon = "Enter how many labor hours per gallon: "
labor_charge_per_hour = "Enter labor charge per hour: "


# function to convert the prompt into float data type
def getFloatInput(s_user_input):
    num = 0
    while num <= 0:
        try:
            reference_var = float(input(s_user_input))

            if reference_var < 0:
                print("Please enter the positive numeric value.")
            elif reference_var >= 0:
                return reference_var
        except ValueError:
            print("Enter the valid number.")


# function to change the string data type into float data type
fsquare_feet = getFloatInput(square_feet)
fpaint_price = getFloatInput(paint_price)
ffeet_per_gallon_of_paint = getFloatInput(gallon_of_paint)
flabor_hours_per_gallon = getFloatInput(labor_hours_per_gallon)
fpainting_labor_charge_per_hour = getFloatInput(labor_charge_per_hour)

# inputstate
user_state = input("Enter the state name: ").upper()


#  function to find total number of gallons for painting
def getGallonsOfPaint(sq_ft_of_wall, ft_per_gallon_of_paint):
    itotal_gallons = sq_ft_of_wall / ft_per_gallon_of_paint

    return int(math.ceil(itotal_gallons))


iGallons_needed = getGallonsOfPaint(fsquare_feet, ffeet_per_gallon_of_paint)


# function to find total labor hours that is number of gallon times the  time required to paint a gallon
def getLaborHours(labor_hour_per_gallon, iGallons):
    ftotal_hours = labor_hour_per_gallon * iGallons
    return ftotal_hours


# print(getLaborHours(flabor_hours_per_gallon))
flabor_hours = getLaborHours(flabor_hours_per_gallon, iGallons_needed)


# function to find labor cost
def getLaborCost(labor_hrs_per_gallon, paint_charge, iGallons):
    ftotal_labor_cost = labor_hrs_per_gallon * paint_charge * iGallons
    return ftotal_labor_cost


# print(getLaborCost(flabor_hours_per_gallon, fpainting_labor_charge_per_hour))
flabor_cost = getLaborCost(flabor_hours_per_gallon, fpainting_labor_charge_per_hour, iGallons_needed)


# function to find paint price by multiplying total hours and number of gallons
def getPaintCost(price, iGallons):
    ffinal_price = iGallons * price
    return ffinal_price


# print(getPaintCost(fpaint_price))

fpaint_cost = getPaintCost(fpaint_price, iGallons_needed)


# function to find the sales tax of paint and labor cost
def getSalesTax(state):
    if state == "CT":
        ftax_rate = 0.06
    elif state == "MA":
        ftax_rate = 0.0625
    elif state == "ME":
        ftax_rate = 0.085
    elif state == "NH":
        ftax_rate = 0.0
    elif state == "VT":
        ftax_rate = 0.06
    elif state == "RI":
        ftax_rate = 0.07
    else:
        ftax_rate = 0

    ftax_amount = ftax_rate * (fpaint_cost + flabor_cost)
    return ftax_amount


# print(getSalesTax(s_user_state))

# function to print all the function's return values
def showCostEstimate():
    print("State job is in: ", user_state)
    print("Gallons of paint:", iGallons_needed)
    print("Hours of labor:", "{:,.1F}".format(flabor_hours, ))
    print("Paint charges: $", "{:,.2F}".format(fpaint_cost, ))
    print("Labor charges: $", "{:,.2F}".format(flabor_cost))
    print("Tax : $", "{:,.2F}".format(getSalesTax(user_state)))
    print("Total Cost: $", "{:,.2F}".format(fpaint_cost + getSalesTax(user_state) + flabor_cost))


def showCostEstimate_file():
    with open("PainJobOutput.txt", "w") as out:  # opening the file
        out.write("State job is in: " + user_state + "\n")
        # writing in the file and breaking the line.
        out.write("Gallons of paint:" + " {:,}".format(iGallons_needed) + "\n")
        out.write("Hours of labor:" + " {:,.1F}".format(flabor_hours, ) + "\n")
        out.write("Paint charges: $ " + "{:,.2F}".format(fpaint_cost) + "\n")
        out.write("Labor charges: $ " + "{:,.2F}".format(flabor_cost) + "\n")
        out.write("Tax : $" + format(getSalesTax(user_state), '.2f') + "\n")
        out.write("Total Cost: $ " + "{:,.2F}".format(fpaint_cost + getSalesTax(user_state) + flabor_cost) + "\n")


def main():
    return showCostEstimate(), showCostEstimate_file()


main()
