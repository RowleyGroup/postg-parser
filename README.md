# postg-parser
**postg-parser** is a python parser for the XDM calculation code, [postg](https://github.com/aoterodelaroza/postg).

# Development
post-parser depends on [openbabel](https://github.com/openbabel/openbabel) and pybel (Python bindings for openbabel). Before installing the dependencies, you need to install openbabel individually. As there are a few problems with pybel and the stable versions of openbabel, clone the master branch and compile it:
```
git clone https://github.com/openbabel/openbabel.git
mkdir build
cd build
cmake ../openbabel -DPYTHON_BINDINGS=ON
make
make install
```

Clone the postg-parser and cd in to it:

```
git clone https://github.com/RowleyGroup/postg-parser.git
cd postg-parser
```

Then you can use [pip](https://pip.pypa.io/en/stable/) to install the dependencies needed for developing the package.

```
pip install -r requirements-dev.txt
```
