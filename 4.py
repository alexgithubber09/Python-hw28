from jinja2 import Template

listName = {
    'Mike': 'Mike@gmail.com',
    'Alex': 'Alex@gmail.com',
    'Bob': 'Bob@gmail.com'
}

with open("template.html.j2", "r") as file:
    template = Template(file.read())

outputName = template.render(listName=listName.items())


with open("template.html", "w") as file:
    file.write(outputName)



