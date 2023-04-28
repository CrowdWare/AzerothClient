# BUILD

## Create the ressources for the client
pyside6-rcc main.qrc -o main_rc.py
pyside6-rcc resources.qrc -o resources.py

## Build the wheel
cd build
cmake ..
cd ..

change versionnumber in setup.py at the end
setup(
    name="azerothlib",
    version="0.0.2",

python setup.py bdist_wheel

## Install
Use the wheel with the highest version like in setup.py.

pip install dist/azerothlib-0.0.1-cp39-cp39-win_amd64.whl

