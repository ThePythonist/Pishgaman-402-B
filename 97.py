header = input("Type header : ")
par = input("Type content : ")

content = f"""
<h1>{header}</h1>
<p>{par}</p>
"""
open("home.html", "w").write(content)
print('Done')
