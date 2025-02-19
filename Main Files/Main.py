from FormulaList import *
from Settings import *
import time

# Enable Delay:
if(enableDelay == False):
    shortDelay = 0
    regDelay = 0
    longDelay = 0

# Loop:
Continue = True
while(Continue == True):
    # Menu:
    print("Option 1: Potential/Kinetic Energy")
    time.sleep(shortDelay)
    print("Option 2: Calculate Work Done")
    time.sleep(shortDelay)
    print("Option 3: Calculate Max Turn Speed")
    time.sleep(shortDelay)
    print("Option 4: Calculate Force of Gravity")
    time.sleep(shortDelay)
    print("Option 5: Calculate Momentum")
    time.sleep(shortDelay)
    print("Or, Press 'Q' to Quit.")
    time.sleep(shortDelay)
    selection = str(input("Select Option: "))

    #Delay - Enter Custom Delay in Seconds (Default: 0.25)
    time.sleep(regDelay)
    
    #Potential/Kinetic Energy
    if(selection == "1"):
        #Variables:
        print()
        mass = float(input("Enter Mass: "))
        velocity = float(input("Enter Velocity: "))
        height = float(input("Enter Height: "))
        print()

        #Delay:
        time.sleep(regDelay)

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

        #Delay:
        time.sleep(regDelay)

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

        #Delay:
        time.sleep(regDelay)

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

        #Delay:
        time.sleep(regDelay)

        #Calculations:
        ForceGravityCalc = float(ForceGravity(mass))

        #Print Calculations To CLI:
        print("Force of Gravity = " + str(ForceGravityCalc) + " Newtons")

    #Calculate Momentum 
    elif(selection == "5"):
        #Variables:
        print()
        mass = float(input("Enter Mass: "))
        velocity = float(input("Enter Velocity: "))
        print()

        #Delay:
        time.sleep(regDelay)

        #Calculations:
        MomentumCalc = float(Momentum(mass, velocity))

        #Print Calculations To CLI:
        print("Momentum = " + str(MomentumCalc) + " Kg * m/s")
    
    #Easter Egg
    elif(selection.lower() == "quit"):
        print("Congrats! You have quit the program!")
        Continue = False
        break

    #Quit
    elif(selection == "Q" or selection == "q"):
        Continue = False
        break
    
    #Error #1
    else:
        print("\nError #1: Unrecognized number selected. Please select recognized number.")
    
    #Space
    print()

    #End of Loop Delay
    time.sleep(longDelay)

