import os

# Make Clean
os.system("cd triangle && make distclean && cd ..")
os.system("cd proto && make clean && cd ..")
os.system("rm -f triangle.bin")
os.system("rm -f showme.bin")

# Make Triangle
os.system("cd triangle && make all && cp triangle ../triangle.bin && cd ..")

# Compile ProtoBuffers
os.system("cd proto && make all && cd ..")
