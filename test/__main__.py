import sys
from .simulations import sims

# Starts simulation object
filename = sys.argv[1]
script = sims()

if filename == "sim1":
    script.simulation_1()
if filename == "sim2":
    script.simulation_2()
if filename == "sim3":
    script.simulation_3()
if filename == "sim4":
    script.simulation_4()
if filename == "sim5":
    script.simulation_5()
if filename == "sim6":
    script.simulation_6()
if filename == "sim7":
    script.simulation_7()


