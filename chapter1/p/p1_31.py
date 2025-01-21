def change(given, charged):
    bills={}
    i = given-charged
    if i//200:
        bills["200"]=i//200
        i=i%200
    if i//100:
        bills["100"]=i//100
        i=i%100
    if i//50:
        bills["50"]=i//50
        i=i%50
    if i//20:
        bills["20"]=i//20
        i=i%20
    if i//10:   
        bills["10"]=i//10
        i=i%10
    if i//5:
        bills["5"]=i//5
        i=i%5
    if i//1:
        bills["1"]=i//1
        i=i%1
    return bills

print(change(1000, 500))