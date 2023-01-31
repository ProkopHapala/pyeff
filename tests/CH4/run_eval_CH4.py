import sys
sys.path.append("../../src")
from pyeff_calculator import *
import pyeff_energy_force as eff
eff.verbosity = 3


print("########### DEBUG 1")
#calc = pyeff(p_cfg='./structs/CH4_lmps_opt.cfg', factor=const_bohr )
calc = pyeff(p_cfg='./structs/CH4_lmps_opt-.cfg', factor=const_bohr )
print("########### DEBUG 2")
calc.initialize()
#print("########### DEBUG 3")
#calc.get_energy()
#print("########### DEBUG 4")
calc.print_results()
