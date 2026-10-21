# Stochastic gene expression in cancer cells with ecDNA
Example code for the paper "Stochastic gene expression quantifies mRNA heterogeneity in cancer cell populations with extrachromosomal DNA". 

## Getting the code

You can download a copy of all the files in this repository by cloning the
[git](https://git-scm.com/) repository:

    git clone https://github.com/poulamisganguly/Stochastic-GE-ecDNA.git


## Dependencies

The required dependencies for this project are specified in the file `env_spec.txt`. We used `conda` for package management.


## Usage

Start by creating a `conda` virtual environment by running

    conda create --name gene-exp --file env_spec.txt
    
Activate the conda environment

    conda activate gene-exp
    
Install `pyreadr` and `gillespy2`
```
pip install pyreadr
pip install gillespy2
```
Start a JupyterLab instance and navigate to the generated link to access the interactive notebook

    jupyter lab --no-browser --port=5678 --ip=127.0.0.1


## License

All source code is made available under an MIT license.

## Issues and Contributions

If you have any trouble running the code, please open an issue here or contact me at p[dot]ganguly[at]qmul[dot]ac[dot]uk. Thank you for your interest!
