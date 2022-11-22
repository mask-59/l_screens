import os
import subprocess

def cleanchrome():
    try:
        os.chmod("cleanchrome.sh", 509)
        rc = subprocess.call("./cleanchrome.sh")
    except print("Error cleaning chrome"):
        pass
    
