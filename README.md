build
python3 -m build

distribute
python3 -m twine upload --repository testpypi dist/* --verbose
