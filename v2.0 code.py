import time
name=input("Как тебя зовут?")
print(f"Привет, {name}")
age=int(input("Сколько тебе лет?"))
print(f"Целых {age} лет")
time.sleep(3)
money=float(input("Сколько у тебя с собой денег?"))
print(f"{money} достаточно")
time.sleep(2)
print(f"Ты пошёл в магазин чтобы купить чипсы, и с собой у тебя {money} рублей")
time.sleep(7)
price = 199.99
discount = 0.2
final = price * (1 - discount)
print(f"Цена чипсов: {price}, со скидкой {discount * 100:.0f}% будет {final:.2f} руб.")
time.sleep(5)
print("Но ты не решился купить чипсы, а решил купить колу")
time.sleep(5)
print("Однако, ты ничего не купил потому что решил сэкономить")
time.sleep(5)
print("После того как ты вышел из магазина, ты пошёл домой")
time.sleep(5)
food=input("Доширак или бутерброды с чаем?")
if food=="доширак"or food=="дошик":
 time.sleep(1)
 print("Острый и вкусный как лето")
elif food=="бутерброды с чаем"or food=="бутики с чаем":
 time.sleep(1)
 print("Тепло и вкусно, хороший выбор")
else:
 print('Я тебя не понял, напиши снова')
time.sleep (2)
print("Так незаметно и проходит беззаботное Лето")