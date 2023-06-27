""" 
This example shows how to simulate a cylindrical thermal storage tank with air and spherical magnetite
stones as the bed material. Same as other tutorial but with lumped stones.
"""

import openterrace

t_end = 10*7200

ot = openterrace.Simulate(t_end=t_end, dt=0.05, sim_name='tutorial5')

ot.fluid = ot.Phase(n=100, type='fluid')
ot.fluid.select_substance(substance='air')
ot.fluid.select_domain_shape(domain='cylinder_1d', D=0.3, H=1)
ot.fluid.select_porosity(phi=0.4)
ot.fluid.select_schemes(diff='central_difference_1d', conv='upwind_1d')
ot.fluid.select_initial_conditions(T=273.15+25, mdot=0.001)
ot.fluid.select_bc(bc_type='dirichlet',
                   parameter='T',
                   position=(slice(None, None, None), 0),
                   value=273.15+500
                   )
ot.fluid.select_bc(bc_type='neumann',
                   parameter='T',
                   position=(slice(None, None, None), -1)
                   )
ot.fluid.select_output(times=range(0, t_end+3600, 3600), parameters=['T'])
 
ot.bed = ot.Phase(n=1, n_other=100, type='bed')
ot.bed.select_substance(substance='magnetite')
ot.bed.select_domain_shape(domain='lumped', A=4*3.14159*0.05**2, V=4/3*3.14159*0.05**3)
ot.bed.select_initial_conditions(T=273.15+25)
ot.bed.select_output(times=range(0, t_end+3600, 3600), parameters=['T'])

ot.select_coupling(fluid_phase=0, bed_phase=1, h_exp='constant', h_value=100)

ot.run_simulation()
ot.generate_plots()