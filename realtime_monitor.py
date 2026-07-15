import joblib
import random
import time

model = joblib.load("predictive_model.pkl")

print("Real-Time Equipment Monitoring Started...\n")

while True:

    temperature = random.randint(45,65)
    vibration = round(random.uniform(2.0,6.0),2)
    pressure = random.randint(110,130)
    humidity = random.randint(55,70)

    sample = [[temperature,vibration,pressure,humidity]]

    prediction = model.predict(sample)[0]

    print("--------------------------")
    print("Temperature :",temperature)
    print("Vibration   :",vibration)
    print("Pressure    :",pressure)
    print("Humidity    :",humidity)

    if prediction==1:
        print("ALERT: Equipment Failure Predicted!")
        print("Recommendation: Schedule Maintenance Immediately.\n")

    else:
        print("Equipment Healthy.\n")

    time.sleep(5)
