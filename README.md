# Investigating LSST $u$-band strategy

Notebooks to create plots for the paper
`Quantifying the Impact of LSST u-band Survey Strategy on Photometric Redshift Estimation and the Detection of Lyman-break Galaxies`

Installation (from the root directory):

```bash
mamba env create -f environment.yaml
mamba activate u-band-strat
python -m ipykernel install --user --name u-band-strat --display-name "u-band strat"
pip install -e .
```

Then download the zipped `data` directory from the github release.

Finally, run `python bin/create_density_cache.py`.

You can then run the notebooks in any order to create the plots for the paper.
Note that plots related to photo-z modeling are not produced in this directory.
They were produced on USDF and provided by Melissa Graham.
