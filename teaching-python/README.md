# Introduction to Programming with Python

I wrote these exercise sheets to give a brief introduction to Python. In order to use them you will need to install `jupyter`, which is best done through [miniconda](https://docs.conda.io/en/latest/miniconda.html).

## Installation instructions

Go to the [miniconda website](https://docs.conda.io/en/latest/miniconda.html) and choose the appropriate version. For instance, on a mac you would choose `https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh`.

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh # <- replace this with the right version
chmod +x Miniconda3-latest-MacOSX-x86_64.sh
./Miniconda3-latest-MacOSX-x86_64.sh # this will need you to agree to terms and conditions
conda create -n myenv python=3
conda activate myenv
conda install jupyter numpy pandas matplotlib 
```

Once installed, clone this repository and run the worksheets:

```bash
git clone https://github.com/jack-willturner/notes.git
cd notes/teaching-python
jupyter notebook 
```

Then click on the notebook you want.
