import gillespy2

def stochastic_gene_exp(ka, kd, jp, kp, gene_copies=1):
    # First call the gillespy2.Model initializer.
    model = gillespy2.Model(name='StochasticGeneExp')

    # Define parameters for the rates of creation and dissociation.
    k_a = gillespy2.Parameter(name='k_a', expression=ka)
    k_d = gillespy2.Parameter(name='k_d', expression=kd)
    j_p = gillespy2.Parameter(name='j_p', expression=jp)
    k_p = gillespy2.Parameter(name='k_p', expression=kp)
    model.add_parameter([k_a, k_d, j_p, k_p])

    # Define variables for the molecular species representing M and D.
    G = gillespy2.Species(name='deactivatedGene', initial_value=gene_copies)#gene_copies-int(gene_copies/2))
    Gstar = gillespy2.Species(name='activatedGene',   initial_value=0)#int(gene_copies/2))
    p = gillespy2.Species(name='protein', initial_value=0)
    ϕ = gillespy2.Species(name='decayProduct', initial_value=0)
    model.add_species([G, Gstar, p, ϕ])

    # The list of reactants and products for a Reaction object are each a
    # Python dictionary in which the dictionary keys are Species objects
    # and the values are stoichiometries of the species in the reaction.
    r_a = gillespy2.Reaction(name="r_activation", rate=k_a, reactants={G:1}, products={Gstar:1})
    r_d = gillespy2.Reaction(name="r_deactivation", rate=k_d, reactants={Gstar:1}, products={G:1})
    r_p = gillespy2.Reaction(name="r_synthesis", rate=j_p, reactants={Gstar:1}, products={Gstar:1,p:1})
    r_ϕ = gillespy2.Reaction(name="r_decay", rate=k_p, reactants={p:1}, products={ϕ:1})
    model.add_reaction([r_a, r_d, r_p, r_ϕ])

    # Set the timespan for the simulation.
    tspan = gillespy2.TimeSpan.linspace(t=100, num_points=101)
    model.timespan(tspan)
    return model