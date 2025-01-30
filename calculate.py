import sys

_, a, b, c = sys.argv

body = "<html>\n<head>\n<title>Assignment 4</title>\n</head>\n<body>\n<h1>Assignment 4</h1>\n<br/>\n"

if not a.isnumeric() or not b.isnumeric() or not c.isnumeric():
    body += "a, b, c must be a number\n<br/>\n"
else:
    a, b, c = float(a), float(b), float(c)
    if a < 1:
        body += "a is too small\n<br/>\n"
    elif b == 0:
        body += "b won't effect the result\n</br>\n"
    elif c < 0:
        body += "c can't be negative\n</br>\n"
    else:
        result = c**3
        if result > 1000:
            result = (result**0.5) * 10
        else:
            result = (result**0.5) / a
        result += b
        body += "Result: {}\n<br/>\n".format(result)
body += '<a href="/">Back to home<a/>\n</body>\n</html>'
# I use / as home path because I config apache to serve form.php as index
print(body)
