cuisine=["mukimo","githeri","njahi","mahamri","avocado"]
while True:
    lunch=input("what cuisine would you like to order :").lower()
    if lunch in cuisine:
       print("welcome,you can have your lunch")
       break
    else:
        print("sorry,please choose another dish,that's unavailable at the moment!..")
        continue








