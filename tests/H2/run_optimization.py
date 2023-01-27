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
