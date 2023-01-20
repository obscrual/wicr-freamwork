import os
try:
    os.system("pip install requests")
    input("")
except:
    try:
        os.system("python -m pip install requests")
        input("")
    except:
        print("libraries can't downloading \nplase add python path or another problem")
        input("")
