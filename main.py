import datetime

#calculate age
def age(date):
    datenow = datetime.datetime.today()
    date = datenow.year - date.year - ((datenow.month, datenow.day) < (date.month, date.day))
    return date

#check if date is invalid then return true
def invalidDate(birth):
    datelist = birth.split("-")
    #year = int(datelist[2])
    #month = int(datelist[1])
    #day = int(datelist[0])
    todaydate = datetime.datetime.today()
    return len(datelist) != 3 or not (1 <= int(datelist[0]) <= 31) or not (1 <= int(datelist[1]) <= 12) or not (
            1900 < int(datelist[2]) <= todaydate.year) or \
            datetime.datetime.strptime(birth, "%d-%m-%Y").date() >= todaydate.date()

#receive new entries until it's null then return dict
def entry():
    newdict = {}
    name = input("enter name:")
    while name != "":
        birth = input("enter birthdate (d-m-y):")

        #if invalidDate true pass this round
        if invalidDate(birth):
            print("invalid date,", name)
            continue
        birth = datetime.datetime.strptime(birth, "%d-%m-%Y").date()
        newdict[name] = age(birth), birth.strftime("%A")
        name = input("enter name:")
    return newdict


mydict = entry()


if len(mydict) == 1:
    key = list(mydict.keys())
    print("{}".format(key[0]), "is", mydict.get(key[0])[0], "years old and she/he was born on", mydict.get(key[0])[1])
    print("there is no oldest or youngest person")
else:
    for i in mydict.keys():
        print("{}".format(i), "is", mydict.get(i)[0], "years old and she/he was born on", mydict.get(i)[1])
        if mydict.get(i) == max(mydict.values()):
            maxname = i
        if mydict.get(i) == min(mydict.values()):
            minname = i
    print("the oldest person is", maxname, max(mydict.values())[0])
    print("the youngest person is", minname, min(mydict.values())[0])

print("total people: {}".format(len(mydict)))
