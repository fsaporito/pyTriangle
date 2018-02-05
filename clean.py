import os

# Make Clean
os.system("cd triangle && make distclean && cd ..")
os.system("cd proto && make clean && cd ..")
os.system("cd proto && make clean && cd ..")
os.system("cd __pycache__ && rm -f * && cd ..")
os.system("cd protopy && cd __pycache__ && rm -f * && cd .. && cd ..")
os.system("rm -f triangle.bin")
os.system("rm -f showme.bin")