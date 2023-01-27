import sys
sys.path.append("../../src")
from pyeff_calculator import *

#calc = pyeff(p_cfg='./structs/H2.cfg' )
calc = pyeff(p_cfg='./structs/H2_new.cfg', factor=const_bohr )
calc.initialize()
calc.get_energy()

calc.print_results()
