from subprocess import call
import os
import glob
from os import remove,rename
import shutil
class Compiler:
    def __init__(self) -> None:
        self.enableCythonBool =False
    def compile(self):
        if self.enableCythonBool:
            path = os.getcwd().split("PyGE")[0]+"PyGE//"
            print(path)
            files = []
            dist = ""
            for i in range(0, 5):
                targetPattern = path + "//" + dist + "*.py"
                files = files + glob.glob(targetPattern)
                dist = dist + "**//"

            for file in files:
                print("Rename:", end="")
                print(file)

                pathAnterior = os.getcwd()

                name = file.split("\\")[-1]
                print(name)
                if name not in ["compiler.py","setupAll.py","run.py"]:

                    simpleName = name.replace(".py", "")
                    path = file.replace(name, "")
                    os.chdir(path)
                    rename(name,simpleName+".pyx")
                    # remove(simpleName+".c")
                    # remove(simpleName + ".**.pyd")
                    # remove(simpleName + ".html")
                    os.chdir(pathAnterior)
                    print(
                        "-------------------------------------------------------------------------------------------------------------")
            #setupAll
            pathAnterior=os.getcwd()
            path=pathAnterior.split("PyGE")[0]+"PyGE//"
            os.chdir(path)
            call("python setupAll.py build_ext --inplace")
            os.chdir(pathAnterior)

        else:
            path = os.getcwd().split("PyGE")[0]+"PyGE//"

            print(path)
            files = []
            dist = ""
            for i in range(0, 5):
                targetPattern = path + "//" + dist + "*.pyx"
                files = files + glob.glob(targetPattern)
                dist = dist + "**//"

            for file in files:
                print("Rename:", end="")
                print(file)

                pathAnterior = os.getcwd()

                name = file.split("\\")[-1]
                print(name)


                simpleName = name.replace(".pyx", "")
                path = file.replace(name, "")
                os.chdir(path)
                if not os.path.exists(simpleName+".py"):
                    rename(name,simpleName+".py")
                else:
                    remove(simpleName+".pyx")
                if os.path.exists(simpleName+".c"):
                    remove(simpleName+".c")

                path1 = os.getcwd()
                filesPyx=[]
                dist1 = ""
                for i in range(0, 5):
                    targetPattern = path1 + "//" + dist1 + "*.pyd"
                    filesPyx = filesPyx + glob.glob(targetPattern)
                    dist = dist + "**//"
                    for f in filesPyx:
                        if os.path.exists(f):
                            remove(f)
                if os.path.exists(simpleName + ".html"):
                    remove(simpleName + ".html")
                if os.path.isdir("build"):
                    shutil.rmtree("build")
                os.chdir(pathAnterior)
                print(
                    "-------------------------------------------------------------------------------------------------------------")

    def enableCython(self):
        self.enableCythonBool=True

#comp=Compiler()
#comp.enableCython()
#comp.compile()