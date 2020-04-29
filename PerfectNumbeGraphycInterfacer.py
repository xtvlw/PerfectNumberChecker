from tkinter import Label, Button, Entry, Tk

root = Tk()

def click():
	try:
		num, nums = int(box.get()), []
	except:
		return 0
	for i in range(1, num):
		if num%i == 0:
			nums +=[i]
	resu = sum(nums)
	if resu == num and num != 0:
		label["text"] = (f"{num} is perfect")
	else:
		label["text"] = (f"{num} is not perfect")
	nums = []


box = Entry(root, width=25, font="arial 15")
box.place(x=5, y=10)

butn = Button(root, width=28, font="arial 12", text="check", relief="solid", command=click)
butn.place(x=5, y=65)

label = Label(root, width=25, font="arial 15", text="perfect number", relief="solid")
label.place(x=5, y=120)



root.title("perfect number")
root.geometry("300x300")
root.mainloop()