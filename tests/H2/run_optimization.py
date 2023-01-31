
import sys
sys.path.append("../../src")
from pyeff_optimizer import * 

# structure 
p_cfg = './structs/H2.cfg'

# variables 
emax=0.0000001
fmax=0.001
steps = 10000
fix_nuc = None




# optimization 
calc = pyeffBFGS(p_cfg,emax,fmax,steps,fix_nuc)
calc.run()
calc.calc.print_results()
factor = 27.2114
Ebind = calc.calc.results['energy']*factor -2*-11.548872606777246
print( "Binding energy :", Ebind, "[eV] ", Ebind*23.060, "[kcal/mol]" )
# show final structure 
calc.view()
# write final structure as xyz file 
calc.write_xyz()

print(
'''
    from http://aip.scitation.org/doi/10.1063/1.3272671
    s = 1.77 [bohr] =  0.9366437 [A]
    bond_lenght(H-H): 1.47 [bohr] = 0.7778905 [A] ( vs 1.4 [bohr] exact SE solution, 1.38 [bohr] HF solution )
    binding energy: 67 [kcal/mol] = 2.91 [eV]  (vs. 109 [kcal/mol] exact 86 [kcal/mol] HF )
        => Etot = 2*-11.5488764245607 - 2.91 = -26.0077528491 eV
'''
)