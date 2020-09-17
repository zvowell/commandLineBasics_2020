# Intro to Command Line Workshop

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/zvowell/commandLineBasics_2020/main?urlpath=lab)

A Binder-compatible repo with an `environment.yml` file.

Access this Binder by clicking the blue badge above or at the following URL:

https://mybinder.org/v2/gh/zvowell/commandLineBasics_2020/main?urlpath=lab

## Notes
The `environment.yml` file lists all Python libraries that will be imported into this notebook, specified as though they were created using the following `conda` commands:

```
source activate example-environment
conda env export --no-builds -f environment.yml
```

The `apt.txt` file lists all the Bash apt packages that will be installed when the notebook is launched.

The folder workshop-resources contains text files, image files, scripts, and other data that is used in the workshop.
