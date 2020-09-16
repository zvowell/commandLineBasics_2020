# Conda environment with environment.yml

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/zvowell/commandLineBasics_2020/main?urlpath=lab)

A Binder-compatible repo with an `environment.yml` file.

Access this Binder by clicking the blue badge above or at the following URL:

https://mybinder.org/v2/gh/zvowell/commandLineBasics_2020/main?urlpath=lab

## Notes
The `environment.yml` file should list all Python libraries on which your notebooks
depend, specified as though they were created using the following `conda` commands:

```
source activate example-environment
conda env export --no-builds -f environment.yml
```

Note that the only libraries available to you will be the ones specified in
the `environment.yml`, so be sure to include everything that you need!
