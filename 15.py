word = input("Enter any word to check if its a mirror word : ")

if word == word[::-1]:
	print("Mirror Word")
else :
	print("Not a Mirror Word")
