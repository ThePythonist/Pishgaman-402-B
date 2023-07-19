students = [
    {"name": "sajad", "age": 22, "job": "backend dev"},
    {"name": "amir", "age": 15, "job": "db admin"},
    {"name": "sarina", "age": 16, "job": "frontend dev"},
    {"name": "elisa", "age": 16, "job": "project manager"},
    {"name": "zahra", "age": 23, "job": "frontend dev"},
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Consolas, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #ad2351;
  color: white;
}
</style>
</head>
<body>

<h1>Students</h1>

<table id="customers">
  <tr>
    <th>Student Name</th>
    <th>Student Age</th>
    <th>Student Job</th>
  </tr>
  
"""

for i in students:
    html += f"""
      <tr>
        <td>{i['name']}</td>
        <td>{i['age']}</td>
        <td>{i['job']}</td>
      </tr>
    """

html += """
</table>
</body>
</html>
"""

open("table.html", "w").write(html)
print("done")
