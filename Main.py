from FormulaList import *

#Menu:
print("Option 1: Potential/Kinetic Energy")
print("Option 2: Calculate Work Done")
selection = str(input("Select Option #: "))

#Potential/Kinetic Energy
if(selection == "1"):
    #Variables:
    print()
    mass = float(input("Enter Mass: "))
    velocity = float(input("Enter Velocity: "))
    height = float(input("Enter Height: "))
    print()

    #Calculations
    PotentialEnergyCalc = float(PotentialEnergy(mass, height))
    KineticEnergyCalc = float(KineticEnergy(mass, velocity))

    #Print Calculations To CLI
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

    #Calculation
    WorkCalc = float(Work(force, displacement, angle))

    #Print Calculation To CLI
    print("Work = " + str(WorkCalc) + " Joules")
