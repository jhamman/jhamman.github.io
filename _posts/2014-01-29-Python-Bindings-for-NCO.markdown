---
layout:     post
title:      "Python Bindings for NCO"
date:       2014-01-29 12:00:00
author:     "Joe Hamman"
header-img: "img/home-bg.jpg"
comments: true
---

Like many in the geophysical sciences these days, my preferred data format is [netCDF](http://www.unidata.ucar.edu/software/netcdf/) (Network Common Data Form).  netCDF offers "a set of software libraries and self-describing, machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data."  The fact that the format is self-describing and machine-independent has allowed for the development generic processing tools.  Considerable work has gone into developing some very nice and quite advanced netCDF file operators.  The two libraries I find myself using on a daily basis are [NCO (netCDF Operators)](http://nco.sourceforge.net/) and [CDO (Climate Data Operators)](https://code.zmaw.de/projects/cdo/wiki/Cdo#Documentation).

Both NCO and CDO were developed for use on the command line or in the shell (e.g. bash).  While the shell is really nice for doing basic operations, I still don't find it convenient for more complicated file handling operations.  In walks Python.  Python has been my scripting language of choice and I have found that it offers some nice solutions for file handling.  A few years back, Ralf Mueller introduced a set of Python bindings to CDO.  `cdo.py` allows the user to call any of the CDO operators from within python.  As far as I know, no one has done this for NCO, so I gave it a go.  

### pynco
[pynco](https://github.com/nco/pynco) is a clone of the [cdo-bindings](https://github.com/Try2Code/cdo-bindings) Python module.  It follows basically the same syntax as `cdo.py` with a few adjustments.  The biggest difference is in its handling of keyword arguments.  If you have used NCO before, you know that there are dozens of keyword arguments.  In `nco.py`, any long name (e.g. `--append`) command line argument can be passed to nco.py as a keyword argument (e.g. `append=True`). Here are some examples:

* Everything starts with initializing a `nco` object

        from nco import Nco
        nco = Nco()

* Append two files:

    On the command line it would look like this:

        ncks -A foo.nc bar.nc

    With nco.py we can do the same thing in one of many ways:

        nco.ncks(input='foo.nc', output='bar.nc', options='-A')
        nco.ncks(input='foo.nc', output='bar.nc', append=True)

* Subset using NCO hyperslabs:
    On the command line it would look like this:

        ncks -F -d lon,1,2 in.nc out.nc
        ncks -d lon,1,2 in.nc out.nc

    With nco.py we can do the same thing in one of many ways:

        nco.ncks(input='in.nc', output='out.nc', fortran=True,
             dimension='lon,1,2')
        nco.ncks(input='in.nc', output='out.nc',
             dimension='lon,1,2')

The module also supplies easy temporary file handling.  For example,

        temporary_file1 = nco.ncrcat(input=a_long_list_of_files)
        temporary_file2 = nco.ncrcat(input=b_long_list_of_files)
        nco.ncra(input=[temporary_file1, temporary_file2], output='my_favorite_file_name.nc')

A particularly nice feature of both the CDO and NCO python modules is their ability to return open netCDF file objects or numpy arrays.  For example, here I take the ensemble average of a list of files and return:

* netCDF file object (either scipy or netCDF4-python)

        testCdf = nco.ncea(input=['foo.nc', 'bar.nc', 'spam.nc'], returnCdf=True)

* numpy array

        temps = nco.ncea(input=['foo.nc', 'bar.nc', 'spam.nc'], returnArray='temperature')

* numpy masked array

        masked_temps = nco.ncea(input=['foo.nc', 'bar.nc', 'spam.nc'], returnMaArray='temperature')


The module is still in beta development phase but it's passing all its tests (Python 2.6, 2.7, and 3.3) so I thought I would mention it here.  I've been using it for the last few weeks in my processing scripts and have really liked its functionality.  All NCO operators are available including

`['ncap2', 'ncatted', 'ncbo', 'nces', 'ncecat', 'ncflint', 'ncks', 'ncpdq', 'ncra', 'ncrcat', 'ncrename', 'ncwa', 'ncea', 'ncdump']`  

The code can be found on [github](https://github.com/nco/pynco)

Instructions for installation along with a few more examples are listed in the readme file.
