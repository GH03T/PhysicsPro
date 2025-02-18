from FormulaList import *

#Menu:
print("Option 1: Potential/Kinetic Energy")
print("Option 2: Calculate Work Done")
print("Option 3: Calculate Max Turn Speed")
selection = str(input("Select Option #: "))

#Potential/Kinetic Energy
if(selection == "1"):
    #Variables:
    print()
    mass = float(input("Enter Mass: "))
    velocity = float(input("Enter Velocity: "))
    height = float(input("Enter Height: "))
    print()

    #Calculations:
    PotentialEnergyCalc = float(PotentialEnergy(mass, height))
    KineticEnergyCalc = float(KineticEnergy(mass, velocity))

    #Print Calculations To CLI:
    print("Potential Energy = " + str(PotentialEnergyCalc) + " Joules")
    print("Kinetic Energy = " + str(KineticEnergyCalc) + " Joules")

#Calculate Work Done
if(selection == "2"):
    #Variables
    print()
    force = float(input("Enter Force: "))
    displacement = float(input("Enter Displacement: "))
    angle = float(input("Enter Angle: "))
    print()

    #Calculation:
    WorkCalc = float(Work(force, displacement, angle))

    #Print Calculation To CLI:
    print("Work = " + str(WorkCalc) + " Joules")

#Calculate Max Turn Speed
if(selection == "3"):
    #Variables:
    print()
    frictionCo = float(input("Enter Coefficent of Friction: "))
    radius = float(input("Enter Radius: "))
    print()

    #Calculation:
    MaxTurnSpeedCalc = float(MaxSpeedCurve(frictionCo, radius))
    MaxTurnSpeedCalcMPH = float(MaxTurnSpeedCalc * 2.23694)

    #Print Calculation To CLI:
    print("Max Turn Speed = " + str(MaxTurnSpeedCalc) + " m/s")
    print("Max Turn Speed = " + str(MaxTurnSpeedCalcMPH) + " Mi/h")
