from rpy2.robjects.packages import importr
import rpy2.robjects.packages as r_packages
from rpy2.robjects.vectors import StrVector
# import rpy2's package module

# import R's utility package
utils = r_packages.importr('utils')

# import R's "base" package
base = importr('base')

# select a mirror for R packages
utils.chooseCRANmirror(ind=1)  # select the first mirror in the list

# R package names
packnames = ('pdftools', 'stringi')


# Selectively install what needs to be install.
# We are fancy, just because we can.
names_to_install = list()
for package in packnames:
    if not r_packages.isinstalled(package):
        names_to_install.append(package)

if len(names_to_install) > 0:
    utils.install_packages(StrVector(names_to_install))
