from FormulaList import *

#Loop:
Continue = True
while(Continue == True):
    #Menu:
    print("Option 1: Potential/Kinetic Energy")
    print("Option 2: Calculate Work Done")
    print("Option 3: Calculate Max Turn Speed")
    print("Option 4: Calculate Force of Gravity")
    print("Or, Press 'Q' to Quit.")
    selection = str(input("Select Option: "))
    
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
    elif(selection == "2"):
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
    elif(selection == "3"):
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
    
    #Force of Gravity
    elif(selection == "4"):
        #Variables:
        print()
        mass = float(input("Enter Mass: "))
        print()

        #Calculations:
        ForceGravityCalc = float(ForceGravity(mass))

        #Print Calculations To CLI:
        print("Force of Gravity = " + str(ForceGravityCalc) + " Newtons")

    #Quit
    elif(selection == "Q" or selection == "q"):
        Continue = False
        break
    
    #Error #1
    else:
        print("\nError #1: Unrecognized number selected. Please select recognized number.")
    
    #Space
    print()

