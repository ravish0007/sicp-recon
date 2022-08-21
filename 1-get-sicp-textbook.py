
SICP_TEXTBOOK_URL = 'https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/c975ee8b62d01f5edb5ed01cd99e08d1_SICP_fulltext.zip'

import requests
request = requests.get(SICP_TEXTBOOK_URL)

with open('SICP_FULLTEXT.zip', 'wb') as file:
    file.write(request.content)

