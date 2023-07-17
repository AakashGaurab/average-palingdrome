def palling(n):
   if int(n)==n:
       a = ""
       a = a+str(n)
       b = ""
       for x in a:
          b = x+b
       if a==b:
          return True
       else:
          return False
   else:
      return"Not an integer"
    




# print(palling(121))
# print(palling("545454"))



def average_age(data):
   average = 0
   sum = 0
   count = 0
   for x in data.values():
      if x["job_title"][0]=="S":
         sum = sum+x["age"]
         count = count+1
    
   print(float(sum/count))


average_age({"john":{"age":45,"job_title":"S"},"annu":{"age":12,"job_title":"Sen"}})