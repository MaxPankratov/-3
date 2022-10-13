yearsOfObserving = int(input("Сколько лет человек будет просматривать экспонаты: "))
resultAmount = yearsOfObserving * 365 * 8 * 60 // 5

print("Будет просмотрено", resultAmount, "экспоната(ов)")

exhibits = int(input("Сколько экспонатов в музее: "))

allMinutes = 5 * exhibits

days = allMinutes // 60 // 8

minutes = allMinutes - days * 60 * 8

years = days // 365

days %= 365

print("На просмотр будет затрачено", years, "лет,", days, "дня,", minutes, "минут")