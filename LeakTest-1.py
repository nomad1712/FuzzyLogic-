# Thomas Judge Jr
#Installed and imported all libraries for fuzzylogic
import numpy as ny
import skfuzzy as  fl
from skfuzzy import control as ctrl

# Creation of input variables and there value ranges 
# This is the creation of the variable for the pressure along the conduits that run on the flooring there
# will be a total of 3 created one at the front(1)  one in the middle (2) one in the back three of room.

pressure1 = ctrl.Antecedent(ny.arange(0, 11, 1), 'Pressure Along conduit position 1')
pressure2 = ctrl.Antecedent(ny.arange(0, 11, 1), 'Pressure Along conduit position 2')
pressure3 = ctrl.Antecedent(ny.arange(0, 11, 1), 'Pressure Along conduit position 3')
pressure = ctrl.Consequent(ny.arange(0, 11, 1), 'Overall pressure reading')
# these are the different relative humiditys that are gathered from the senosrs listed throughout the data pod 
#overall pressure in room
#pressureO= ctrl.Antecedent(ny.arange(0, 101 , 1), 'Overall Pressure')

#Overall humidity in room 
humidity1 = ctrl.Antecedent(ny.arange(0, 101, 1), 'Relative Humidity CRAH 1')
# CRAH 1 had a location of being at the front right of the pod 
#CRAH 2 is at the right side back corner of the pod 
humidity2= ctrl.Antecedent(ny.arange(0,101, 1) , 'Relative Humidity CRAH 6')
#CRAH 3 is at the left front of the pod 
humidity3 = ctrl.Antecedent(ny.arange(0,101,1) , 'Relative humidity CRAH 8')
#CRAH 4 the humidity at CRAH 16 will be at the back left corner of the pod
#humidity4= ctrl.Antecedent(ny.arange(0,101,1) , 'Relative Humidity Crah 16 ')
# Overall Humidity rating 
humidity= ctrl.Consequent(ny.arange(0,101,1) , 'Overall Humidity Reading')

#temperature= ctrl.Antecedent(ny.arange(0,101,1), ' Overall Temperature in data Center ')
# temperature sensor 1 2 and 3 will be located on the floor while temperature sensors 3-6 will be located hanging from the ceilings.

temperature1= ctrl.Antecedent(ny.arange(0,101,1), 'Temperature 1 in data Center ')
#This is the second temperature sensor that is under floow and is in the middle portion of the under floor in the center of room
temperature2=ctrl.Antecedent(ny.arange(0,101,1), 'Temperature 2 in data Center')
# This is the third temperature sensor that is under the floor and is in the back right corner of the pod
temperature3=ctrl.Antecedent(ny.arange(0,101,1), 'Temperature 3 in data hall')
# Overall Temperature rating 
temperature=ctrl.Consequent(ny.arange(0,101,1), 'Overall temperature rating')

# The overal leak severety of the system and its range from 0-100
# 0 means there is no chance of leak while a 100 signifies a major leak has been detected within the system
leak_severity = ctrl.Consequent(ny.arange(0, 101, 1), 'Leak Severity')

# Define membership functions for input and output variables
#the pressures are all underfloor so the range remains the same for all sensors inputs

# Define membership functions for input and output variables
# the pressures are all underfloor so the range remains the same for all sensors inputs
pressure['Normal Range'] = fl.trimf(pressure.universe, [0, 2.5, 5])
pressure['Locally High Pressure'] = fl.trimf(pressure.universe, [3.5,5 ,7])
pressure['Room High Pressure'] = fl.trimf(pressure.universe, [6.5 , 8, 10])
pressure2['low'] = fl.trimf(pressure2.universe, [0, 2.5, 5])
pressure2['medium'] = fl.trimf(pressure2.universe, [4.5, 6, 7.5])
pressure2['high'] = fl.trimf(pressure2.universe, [7, 9, 10])
pressure3['low'] = fl.trimf(pressure3.universe, [0, 2.5, 5])
pressure3['medium'] = fl.trimf(pressure3.universe, [4, 6, 8])
pressure3['high'] = fl.trimf(pressure3.universe, [7, 9, 10])
pressure1['low'] = fl.trimf(pressure.universe, [0, 2.5, 5])
pressure1['medium'] = fl.trimf(pressure.universe, [4, 6, 8])
pressure1['high'] = fl.trimf(pressure.universe, [7, 9, 10])

humidity['Dry'] =  fl.trimf(humidity.universe, [0, 25, 50])
humidity['Moderate Humidity'] =  fl.trimf(humidity.universe, [40, 60, 80])
humidity['Room has High Humidity'] =  fl.trimf(humidity.universe, [70, 90, 100])
humidity2['Dry'] =  fl.trimf(humidity2.universe, [0, 25, 50])
humidity2['humid'] =  fl.trimf(humidity2.universe, [40, 60, 80])
humidity2['wet'] =  fl.trimf(humidity2.universe, [70, 90, 100])
humidity3['Dry'] =  fl.trimf(humidity3.universe, [0, 25, 50])
humidity3['humid'] =  fl.trimf(humidity3.universe, [40, 60, 80])
humidity3['wet'] =  fl.trimf(humidity3.universe, [70, 90, 100])

humidity1['Dry']= fl.trimf(humidity1.universe, [0, 25, 50])
humidity1['humid'] =  fl.trimf(humidity1.universe, [40, 60, 80])
humidity1['wet'] =  fl.trimf(humidity1.universe, [70, 90, 100])
 
temperature['Freezing Temperature']= fl.trimf(temperature.universe,[0, 32,50])
#temperature['Low Temperature']= fl.trimf(temperature.universe,[ 30, 47,55])
temperature['Normal Temperature']= fl.trimf(temperature.universe,[40, 60, 82 ])
temperature['High Temperature Range'] =fl.trimf(temperature.universe,[78, 90 ,100 ])
temperature2['Cold']= fl.trimf(temperature2.universe,[0, 30, 56])
temperature2['Normal range']= fl.trimf(temperature2.universe,[43, 60, 82 ])
temperature2['Hot']= fl.trimf(temperature2.universe,[74, 90 ,100 ])
temperature3['Cold']= fl.trimf(temperature3.universe,[0, 30, 56])
temperature3['Normal range']= fl.trimf(temperature3.universe,[43, 60, 82 ])
temperature3['Hot']= fl.trimf(temperature3.universe,[74, 90 ,100 ])
temperature1['Cold']= fl.trimf(temperature1.universe,[0, 30, 56])
temperature1['Normal range']= fl.trimf(temperature1.universe,[43, 60, 82 ])
temperature1['Hot']= fl.trimf(temperature1.universe,[74, 90 , 100 ])

leak_severity['Normal Operation'] =  fl.trimf(leak_severity.universe, [0, 25, 45])
leak_severity['Please Investigate'] =  fl.trimf(leak_severity.universe, [40, 50, 70])
leak_severity['Leak Detected'] =  fl.trimf(leak_severity.universe, [65, 85, 100])


# Pressure Rules
R1 = ctrl.Rule(pressure1['high'] & pressure2['high'] & pressure3['high'], pressure['Room High Pressure'], )
R2 = ctrl.Rule((pressure1['high'] | pressure2['high'] | pressure3['high']), pressure['Locally High Pressure'])
R3 = ctrl.Rule((pressure1['low'] & pressure2['low'] & pressure3['low']) | (pressure1['medium'] & pressure2['medium'] & pressure3['medium']), pressure['Normal Range'])
R4 = ctrl.Rule((pressure1['medium'] | pressure2['medium']) & pressure3['low'], pressure['Normal Range'])

# Humidity Rules
R6 = ctrl.Rule(humidity1['wet'] & humidity2['wet'] & humidity3['wet'], humidity['Room has High Humidity'])
R7 = ctrl.Rule((~humidity1['wet'] & ~humidity2['wet'] & ~humidity3['wet']), humidity['Moderate Humidity'])
R8 = ctrl.Rule((humidity1['Dry'] & humidity2['Dry'] & humidity3['Dry']), humidity['Dry'])
R9 = ctrl.Rule((humidity1['humid'] | humidity2['humid']) & humidity3['humid'], humidity['Moderate Humidity'])
R10 = ctrl.Rule(humidity1['humid'] & humidity2['wet'] & humidity3['wet'], humidity['Room has High Humidity'])

# Temperature Rules
R11 = ctrl.Rule(temperature1['Cold'] & temperature2['Cold'] & temperature3['Cold'], temperature['Freezing Temperature'])
R12 = ctrl.Rule(temperature1['Cold'] & temperature2['Normal range'] & temperature3['Normal range'], temperature['Freezing Temperature'])
R13 = ctrl.Rule(temperature1['Normal range'] & temperature2['Normal range'] & temperature3['Normal range'], temperature['Normal Temperature'])
R14 = ctrl.Rule(temperature1['Hot'] & temperature2['Hot'] & temperature3['Hot'], temperature['High Temperature Range'])
R15 = ctrl.Rule(temperature1['Hot'] | temperature2['Hot'] | temperature3['Hot'], temperature['High Temperature Range'])

# Leak Severity Rules
R16 = ctrl.Rule(pressure['Normal Range'] & humidity['Dry'] & temperature['High Temperature Range'], leak_severity['Leak Detected'])
R18 = ctrl.Rule(pressure['Room High Pressure'] & humidity['Room has High Humidity'] & temperature['Normal Temperature'], leak_severity['Please Investigate'])
# Additional Rule for Leak Detection with Wet Humidity and Hot or Warm Temperature
R19 = ctrl.Rule((humidity1['wet'] | humidity2['wet'] | humidity3['wet']) & (temperature1['Hot'] | temperature2['Hot'] | temperature3['Hot'] | temperature1['Cold'] | temperature2['Cold'] | temperature3['Cold']), leak_severity['Leak Detected'])

R20 = ctrl.Rule(((temperature1['Normal range'] & temperature2['Normal range'] & temperature3['Normal range'])|(temperature1['Cold'] & temperature2['Normal range'] & temperature3['Normal range'])|(temperature1['Normal range'] & temperature2['Cold'] & temperature3['Normal range'])|(temperature1['Normal range'] & temperature2['Normal range'] & temperature3['Cold']))&
                ((humidity1['Dry'] & humidity2['Dry'] & humidity3['Dry'])|(~humidity1['wet'] & ~humidity2['wet'] & ~humidity3['wet']))&(~pressure1['high']&~pressure2['high']&~pressure3['high']),
                leak_severity['Normal Operation'],pressure['Normal Range'],humidity['Moderate Humidity'],temperature['Normal Temperature'])
# Rule for Normal Operation based on specific input values
R21 = ctrl.Rule(pressure1['low'] & pressure2['low'] & pressure3['low'] &  # Adjust pressure conditions as needed
                humidity1['Dry'] & humidity2['Dry'] & humidity3['Dry'] &  # Adjust humidity conditions as needed
                temperature1['Normal range'] & temperature2['Normal range'] & temperature3['Normal range'],  # Adjust temperature conditions as needed
                leak_severity['Normal Operation'])

# New Rules

# Rule for Leak Detection when two of pressure, humidity, or temperature are high
R31 = ctrl.Rule(((pressure1['high'] & pressure2['high']) |
                (pressure1['high'] & pressure3['high']) |
                (pressure2['high'] & pressure3['high'])) &
                ((humidity1['wet'] & humidity2['wet']) |
                (humidity1['wet'] & humidity3['wet']) |
                (humidity2['wet'] & humidity3['wet']) )&
                ((temperature1['Hot'] & temperature2['Hot']) |
                (temperature1['Hot'] & temperature3['Hot']) |
                (temperature2['Hot'] & temperature3['Hot'])),
                leak_severity['Leak Detected'],~pressure['Room High Pressure'],temperature['High Temperature Range'], humidity['Room has High Humidity']
                )
R32 = ctrl.Rule((~pressure1['high'] & ~pressure2['high'] & pressure3['low']) &  
              (  ~humidity1['wet'] & humidity2['humid'] &   ~humidity3['wet']) &
               ( temperature1['Normal range'] & temperature2['Normal range'] & temperature3['Normal range']),
                leak_severity['Normal Operation'],temperature['Normal Temperature'],pressure['Locally High Pressure'], humidity['Moderate Humidity'])
# Rule for Leak Detection when all three temperature inputs are hot and three humidity inputs are wet
R33 = ctrl.Rule(
    (temperature1['Hot'] & temperature2['Hot'] & temperature3['Hot']) &
    (humidity1['wet'] & humidity2['wet'] & humidity3['wet']),
    leak_severity['Leak Detected'])
R34 = ctrl.Rule( humidity1['wet']& humidity2['wet']& humidity3['wet'], humidity['Room has High Humidity'])
# Rule for Please Investigate when pressure is locally high, temperature is freezing, and humidity is moderate
R35 = ctrl.Rule(
    (pressure1['medium'] & pressure2['medium'] & pressure3['medium']) &
    (temperature1['Cold'] & temperature2['Cold'] & temperature3['Cold']) &
    (humidity1['humid'] & humidity2['humid'] & humidity3['humid']),
    leak_severity['Please Investigate']
)
R36 = ctrl.Rule(
    pressure1['high'] & pressure2['high'] & pressure3['high'], pressure['Room High Pressure']
)

R37 = ctrl.Rule(pressure1['high'] & pressure2['high'] & pressure3['high'], pressure['Room High Pressure'])

# Rule for high humidity
R38 = ctrl.Rule(humidity1['wet'] & humidity2['wet'] & humidity3['wet'], humidity['Room has High Humidity'])

# Rule for normal temperature
R39 = ctrl.Rule(temperature1['Normal range'] & temperature2['Normal range'] & temperature3['Normal range'], temperature['Normal Temperature'])
# Rule for a specific scenario considering all antecedents
R40 = ctrl.Rule(
    pressure1['high'] & pressure2['high'] & pressure3['high'] &
    humidity1['wet'] & humidity2['wet'] & humidity3['wet'] &
    temperature1['Hot'] & temperature2['Hot'] & temperature3['Hot'],
    leak_severity['Leak Detected']
)

# Adding the new rule to the control system


# Adding the new rule to the control system


# ...


# Adding all rules to the control system
#add all rules

leak_detection_ctrl = ctrl.ControlSystem([
    R1, R2, R3, R4,  R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,  R18, R19,R20,R21 , R31,R32, R33,R34,R35,R36,R37, R38, R39,R40
])

# Replicating inputs that would be taken from sensors 
leak_detection = ctrl.ControlSystemSimulation(leak_detection_ctrl)
import random

# ... (your existing code)

# Run the system until a leak is detected
#random.uniform(0, 10)
#random.uniform(0, 100)
x= random.uniform(0, 10)
print(x)
    # Set random input values within the range
leak_detection.input['Pressure Along conduit position 1'] = x
x= random.uniform(0, 10)
print(x)
leak_detection.input['Pressure Along conduit position 2'] = x
x= random.uniform(0, 10)
print(x)
leak_detection.input['Pressure Along conduit position 3'] = x
x= random.uniform(0, 100)
print(x)
leak_detection.input['Relative Humidity CRAH 1'] =x
x= random.uniform(0, 100)
print(x)
leak_detection.input['Relative Humidity CRAH 6'] = x
x= random.uniform(0, 100)
print(x)
leak_detection.input['Relative humidity CRAH 8'] = x
x= random.uniform(0, 100)
print(x)
leak_detection.input['Temperature 1 in data Center '] = x
x= random.uniform(0, 100)
print(x)
leak_detection.input['Temperature 2 in data Center'] = x
x= random.uniform(0, 100)
print(x)
leak_detection.input['Temperature 3 in data hall'] = x

    # Compute the system
leak_detection.compute()

    # Print the results
print("Leak Severity:", leak_detection.output['Leak Severity'],"Temp" ,leak_detection.output['Overall temperature rating'],"Humidity " ,leak_detection.output['Overall Humidity Reading'], "pressure", leak_detection.output['Overall pressure reading'])


# Visualization 
pressure.view(sim=leak_detection)
humidity.view(sim=leak_detection)
temperature.view(sim=leak_detection)
leak_severity.view(sim=leak_detection)

# plots for each set
import matplotlib.pyplot as plt
plt.show()