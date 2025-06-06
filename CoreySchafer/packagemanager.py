print("Package Manager Commands")
# pip search Pympler
# pip install Pympler
# pip list
# pip uninstall {package name}
# pip list -o
# pip list -outdated
# pip install -U setuptools
# pip list
# pip freeze

# pip freeze > requirements.txt ....sending to someone the package file
# pip install -r r_test.txt   ....
# pip list
# pip list --outdated 
# pip freeze ...outputs all the requirements for the package that we have 
# pip freeze --local | grep -v '^\-e' | cut -d = =f 1 | xargs -nl pip install -U
# pip freeze --local | grep -v '^\-e' |

print()
print(f'==================================================')
# pip install virtualenv  ...separate different python environments
#       projects make be using different versions or dependencies of django or flask
# pip list
# mkdir Environments
# cd Environments
# ls 
# virtualenv project1_env
# .\project1_env\Scripts\activate  # Use this command to activate the virtual environment in Windows PowerShell

# which python
# which pip
# pip install numpy
# pip install pytz
# pip install psutil
# pip freeze --local > requirements.txt
# cat requirements.txt
# deactivates ....deactivates virtual environment
# ls
# rm -rf project1_env/ ....removes the virtual environment
# ls requirements.txt

# virtualenv -p usr/bin/python2.6 py26_env
# ls
# source py_26/env/bin/activate
# which python
# python --version
# ls 
# pip install -r requirements.txt
# pip list


