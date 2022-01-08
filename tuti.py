from random import randint

player = str(input())
computer = randint(0,2)

if computer == 0:
	computer = "DAM"
if computer == 1:
	computer = "KEO"
if computer == 2:
	computer = "LA"

print("computer choose " + computer)

if player == "KEO":
	if computer =="KEO":
		print("Draw")
	if computer =="DAM":
		print("computer chat: tuong the lao cui vc  <LOSE>")
	if computer =="LA":
		print("computer chat: duoc lam van nua   <WIN>")

if player == "DAM":
	if computer =="KEO":
		print("computer chat: duoc lam van nua   <WIN>")
	if computer =="DAM":
		print("Draw")
	if computer =="LA":
		print("computer chat: tuong the lao cui vc  <LOSE>")

if player == "LA":
	if computer =="KEO":
		print("computer chat: tuong the lao cui vc  <LOSE>")
	if computer =="DAM":
		print("computer chat: duoc lam van nua   <WIN>")
	if computer =="LA":
		print("Draw")

print("tuti voi computer den day la ket thuc")		