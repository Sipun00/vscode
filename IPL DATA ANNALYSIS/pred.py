target=int(input("target:"))
ball=int(input("ball thrown till now:"))
run=int(input("run scored:"))
over=int(input("over:"))
runratio=run/ball
totalball=6*over
restball=totalball-ball
achieve=runratio*restball
if achieve>=target:
    print("WIN")
else:
    print("LOST")
