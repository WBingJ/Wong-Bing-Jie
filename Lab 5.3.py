# Student Name: Wong Bing Jie
# Student Id: 1201200237

# Display the menu
# Ask the user to enter their choice [1 to 2]
# Using a switch-case statement:
# If choice is 1 call function get_cm().
# If choice is 2 call function get_meter().
# Else print "Avail choice"
# In get_cm()
# Get the value of contimetre from the user.
# Call function cm_to_meter(...) and pass centimeter to calculate meter.
# Display the centimeter and meter.
    

def get_cm():
    cm = float(input("Enter centimeter : "))
    m = cm_to_meter(cm)
    print("{:.2f} centimeters is equals to {:.2f} meters".format(cm,m))

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_meter():
    m = float(input("Enter meter : "))
    cm = meter_to_cm(m)
    print("{:.2f} meters is equals to {:.2f} centimeters".format(m,cm))

def meter_to_cm(meter):
    centimeter = meter * 100
    return centimeter

print("======================")
print("         Menu         ")
print("======================")
print("1. Centimeter to meter")
print("2. Meter to centimeter")
print("======================")

choice =int(input("Enter your choice [1 or 2]: "))

if choice == 1:
    get_cm()

elif choice == 2:
    get_meter()

else:
    print("Invalid choice") 