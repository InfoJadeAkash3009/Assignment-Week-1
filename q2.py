# q2
current_battery_level = 44;
model_confidence = 0.01 * current_battery_level;

if(model_confidence > 0.5):
    print("CLassification : Positive");
else:
    print("Classification : Negative");
