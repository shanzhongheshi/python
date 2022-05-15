import sys

print(type(sys.argv))       #<class 'list'>
print(sys.argv[1])          #hello
print(sys.argv[2])          #python
print(sys.argv[3])          #1\
print(type(sys.argv[1]))          #hello
print(type(sys.argv[2]))          #python
print(type(sys.argv[3]))          #1