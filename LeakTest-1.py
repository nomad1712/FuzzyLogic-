# Thomas Judge Jr
#Installed and imported all libraries for fuzzylogic
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the input variables
pressure = ctrl.Antecedent(np.arange(0, 101, 1), 'Pressure')
flow_rate = ctrl.Antecedent(np.arange(0, 101, 1), 'Flow Rate')


# Define the output variable
leak_severity = ctrl.Consequent(np.arange(0, 101, 1), 'Leak Severity')

# Define membership functions for input and output variables
pressure['low'] = fuzz.trimf(pressure.universe, [0, 25, 50])
pressure['medium'] = fuzz.trimf(pressure.universe, [40, 60, 80])
pressure['high'] = fuzz.trimf(pressure.universe, [70, 90, 100])

flow_rate['low'] = fuzz.trimf(flow_rate.universe, [0, 25, 50])
flow_rate['medium'] = fuzz.trimf(flow_rate.universe, [40, 60, 80])
flow_rate['high'] = fuzz.trimf(flow_rate.universe, [70, 90, 100])

leak_severity['low'] = fuzz.trimf(leak_severity.universe, [0, 25, 50])
leak_severity['medium'] = fuzz.trimf(leak_severity.universe, [40, 60, 80])
leak_severity['high'] = fuzz.trimf(leak_severity.universe, [70, 90, 100])

# Define the fuzzy rules
rule1 = ctrl.Rule(pressure['low'] & flow_rate['low'], leak_severity['low'])
rule2 = ctrl.Rule(pressure['medium'] & flow_rate['medium'], leak_severity['medium'])
rule3 = ctrl.Rule(pressure['high'] & flow_rate['high'], leak_severity['high'])

# Create the control system
leak_detection_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Create a simulation
leak_detection = ctrl.ControlSystemSimulation(leak_detection_ctrl)

# Input values (you can change these values to test the system)
leak_detection.input['Pressure'] = 45
leak_detection.input['Flow Rate'] = 70

# Compute the output
leak_detection.compute()

# Print the result
print("Leak Severity:", leak_detection.output['Leak Severity'])

# Visualization (optional)
pressure.view(sim=leak_detection)
flow_rate.view(sim=leak_detection)
leak_severity.view(sim=leak_detection)

# Show the plots
import matplotlib.pyplot as plt
plt.show()