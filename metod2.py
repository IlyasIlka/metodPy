import sys
#1
a = [2,'text',4.5, None]
for i in a:
    print(type(i))
#2

num = int(input())
obmen_list = []
for i in range(0, num):
    obmen_list.append(i)

if len(obmen_list) >= 2:
    for i in range(0, len(obmen_list) - 1, 2):
        obmen_list[i], obmen_list[i + 1] = obmen_list[i + 1], obmen_list[i]

print(obmen_list)
#3
ses_dect = {
    1: "зима",
    2: "зима",
    3: "весна",
    4: "весна",
    5: "весна",
    6: "лето",
    7: "лето",
    8: "лето",
    9: "осень",
    10: "осень",
    11: "осень",
    12: "зима"
}
ses_list = ["зима", "весна", "лето", "осень"]
month = int(input())
ses = ses_dect.get(month,"netu")
if month in [12, 1, 2]:
    sees = ses_list[0]  
elif month in [3, 4, 5]:
    sees = ses_list[1]  
elif month in [6, 7, 8]:
    sees = ses_list[2]  
elif month in [9, 10, 11]:
    sees = ses_list[3]  
else:
    sees = "netu"
print(ses, sees)
#4
strk = str(input())
strk = strk.split()
n = 0
if len(strk) >= 10:
    for j in strk:
        n+=1
        if(n <= 10):
            print(n,j,'\n')
        else:
            sys.exit()
else:
    for j in strk:
        n+=1
        print(n,j,'\n')
#5
my_list = [7, 5, 3, 3, 2]
index_insert=0
numer = int(input())
while index_insert < len(my_list) and my_list[index_insert] >=numer:
    index_insert+=1
my_list.insert(index_insert,numer)

print(my_list)
#6
my_Tovar =[
    (1, {"Hазвание": "компьютеp", "цена": 20000, "количество": 5, "eд": "500шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "200шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "300шт."})
]
number = int(input())

