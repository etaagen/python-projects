##### some cheat sheet basics
# starting a new project and virtual environment in VS Code
# 1) open a new folder in VS Code
# 2) create main.py
# 3) in the terminal run: python3 -m venv .my_venv
# 4) install packages in the virtual environment
# pip install numpy
# pip install pandas
# pip install scipy
# pip install matplotlib
# pip install seaborn
# pip install scikit-learn

##### some basics that feel different from R
x = input("Tell me a number:")
x = int(x)
print(x)

y = [1, 2, 3, 4, 5]
y.append(6)
y.insert(0, 0)
y.remove(5) # no index
print(y)