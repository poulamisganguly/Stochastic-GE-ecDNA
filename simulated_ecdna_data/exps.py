import numpy as np
import scipy
import gillespy2
from matplotlib import pyplot as plt
from tqdm import tqdm
import funcs
import os
import gc

def run_exp(gene_dist_file, ka, kd, jp, kp, output_file, no_traj=1):
    """
    Function that runs stochastic gene expression simulations for a population of cells
    
    Arguments:
    gene_dist_file (str)  : file containing final ecDNA copy numbers in each cell (obtained from C++ code)
    ka (float)            : gene activation rate
    kd (float)            : gene deactivation rate
    jp (float)            : mRNA/protein production rate
    kp (float)            : mRNA/protein decay rate
    output_file (str)     : file to save output of simulation to
    no_traj (int)         : number of realisations (default 1)
    
    Returns:
    The function returns None if run successfully. Saves output to output_file
    """
    # load ecDNA copy numbers in final population of cells
    final_dist = np.loadtxt(gene_dist_file)
    final_dist_flat = final_dist[:100].flatten() # take first 100 runs
    g = final_dist_flat[final_dist_flat!=0].astype('int').tolist()

    with open(output_file, 'w+') as file:
        for j in tqdm(range(len(g))):
            model = funcs.stochastic_gene_exp(ka=ka, kd=kd, jp=jp, kp=kp, gene_copies=g[j])
            solver = gillespy2.SSACSolver(model)
            # change number of trajectories to 1 and for each traj insert 
            # a different gene copy number drawn from the ecdna distribution
            res = model.run(solver=solver, number_of_trajectories=no_traj)#, seed=)
            for i in range(no_traj): file.write("%i " % res[i]['protein'][-1])
            file.write("\n")
    return None

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Run stochastic gene expression simulations')
    parser.add_argument('--gene_dist_file', required=True,
                        help='file containing final ecDNA copy numbers')
    parser.add_argument('--ka', required=True, type=float, default=0.1, 
                        help='gene activation rate')
    parser.add_argument('--kd', required=True, type=float, default=0.1, 
                        help='gene deactivation rate')
    parser.add_argument('--jp', required=True, type=float, default=1000.0, 
                        help='mRNA/protein production rate')
    parser.add_argument('--kp', required=True, type=float, default=1.0, 
                        help='mRNA/protein decay rate')
    parser.add_argument('--output_file', required=True,
                        help='output file')
    parser.add_argument('--no_traj', required=False, type=int, default=1,
                        help='number of realisations')
    args = parser.parse_args()
    run_exp(gene_dist_file=args.gene_dist_file, ka=args.ka, kd=args.kd, jp=args.jp, kp=args.kp, output_file=args.output_file, no_traj=args.no_traj)