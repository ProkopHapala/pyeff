from pyeff_optimizer import * 

# structure 
p_cfg = './structs/H.cfg'
# variables 
emax=0.0000001
fmax=0.0001
steps = 10000
fix_nuc = None
# optimization 
calc = pyeffBFGS(p_cfg,emax,fmax,steps,fix_nuc)
calc.run()
calc.calc.print_results()
# show final structure 
calc.view()
# write final structure as xyz file 
calc.write_xyz()
