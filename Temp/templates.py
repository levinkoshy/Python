#accespt the path to a template

import os

#path -"/" for mac; "\" for windows
#To have a single code, os helps

def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid template path %s"%(file_path))
    return file_path

file_ = 'Templates/email_message.txt'

print(get_template_path(file_))

def get_template(path):
	file_path = get_template_path(path)
	return open(file_path).read()

def render_context(template_string,context):
	return template_string.format(**context)

template= get_template(file_)
context = {
	"name": "Justin",
	"date": None,
	"total": None
}
