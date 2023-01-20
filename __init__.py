import os
try:
    os.system("pip install requests")
except:
    try:
        os.system("python -m pip install requests")
    except:
        print("libraries can't downloading \nplase add python path or another problem")
        input("")
