import os 

fileName = "README.md"
path = os.getcwd()

for item in os.listdir(path):
    cur = os.path.join(path, item)
    if os.path.isdir(cur) and not item.startswith("."):
        fptr = open(os.path.join(cur, fileName), "w")

        fptr.write("# " + item + "-Solutions\n")
        fptr.write("The solutions of {} are available in this repositry.\n".format(item))