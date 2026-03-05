donor=input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
patient=input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()
if donor == "I" and (patient == "I" or patient == "II" or patient == "III" or patient == "IV"):
    print("Совместимо")
elif donor == "II" and (patient == "II" or patient == "IV"):
    print("Совместимо")
elif donor == "III" and (patient == "III" or patient == "IV"):
    print("Совместимо")
elif donor == "IV" and (patient == "IV"):
    print("Совместимо")
else:
    print("Не совместимо")