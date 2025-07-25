html_content = """
<html>
  <head><title>My Page</title></head>
  <body>
    <h1>Hello from Python-generated HTML!</h1>
    <p>Dhruv was here 😎</p>
  </body>
</html>
"""

with open("my_page.html", "w", encoding="utf-8") as f:
    f.write(html_content)

import webbrowser
webbrowser.open("my_page.html")
