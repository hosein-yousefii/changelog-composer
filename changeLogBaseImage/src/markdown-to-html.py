import markdown2
from jinja2 import Environment
import os
import sys

changeLog_filePath = sys.argv[1]
changeLogHtml_filePath = sys.argv[2]

with open(changeLog_filePath, 'r') as file:
  file_content = file.read()

html_content = markdown2.markdown(file_content)

template_code = """
{{ html_content }}
"""

# Create the Jinja2 environment
env = Environment()

# Render the template code with the data
changeLogHtmlConverted = env.from_string(template_code).render(html_content=html_content)

with open(changeLogHtml_filePath, "w") as file:
  file.write(changeLogHtmlConverted)

print(changeLogHtmlConverted)
