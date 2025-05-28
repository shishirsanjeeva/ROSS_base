
from pathlib import Path
import ross as rs
import numpy as np
 
# uncomment the lines below if you are having problems with plots not showing
import plotly.io as pio
pio.renderers.default = "browser"
#======================================================================================
path=  "rotorModels/testRotor3.toml"
 
if not Path(path).exists():
    print(f"File {path} does not exist. Please create the rotor model first.")
    exit()
else:
    rotor1 = rs.Rotor.load(path)
    print(f"Rotor model loaded from {path}")
print("Rotor total mass = ", np.round(rotor1.m, 2))
print("Rotor center of gravity =", np.round(rotor1.CG, 2))
 
# plotting the rotor model
fig =rotor1.plot_rotor()
fig.show()