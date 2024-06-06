# Module pour le tensiomètre
# tensiometer.py
systolic = 120
diastolic = 80

def measure():
    global systolic, diastolic
    systolic += 5
    diastolic += 2

def get_systolic():
    return systolic

def get_diastolic():
    return diastolic
