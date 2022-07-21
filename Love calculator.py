name1 = input("Enter the First name: ").lower()
name2 = input("Enter the Second name: ").lower()
final_name = name1 + name2
t = final_name.count("t")
r = final_name.count("r")
u = final_name.count("u")
e = final_name.count("e")

l = final_name.count("l")
o = final_name.count("o")
v = final_name.count("v")
e2 = final_name.count("e")

true = t + r + u + e
love = l + o + v + e
love_score1 = str(true) + str (love)
love_score = int(love_score1)
if(love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos")
elif(love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"your score is: {love_score}")


