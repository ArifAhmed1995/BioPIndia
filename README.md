# BioPIndia
Software for interfacing with the BioP

### Downloading Prototype

Run `git clone https://github.com/ArifAhmed1995/BioPIndia` on a terminal.

### Dependencies

- `Qt5` for `fstl`
- `PyForms` for main GUI

### Building fstl

Download and place `fstl` folder directly in the repo. For clarification, all the unzipped files
should be inside that empty `fstl` folder that's already in the repo.

After that follow the instructions to build the library from [here](https://github.com/mkeeter/fstl/blob/master/README.md#linux)

Later on `cmake` script will be used to automatically download and build any libraries or dependencies.

### Running the prototype

In Linux shell, execute the script by `python3 prototype.py`

`numpy-stl` is also tested. Major lag observed. Not part of the prototype. Existing only for testing purposes.

First load an STL file using the button `Open`.
Then use main toolbar options as required.
