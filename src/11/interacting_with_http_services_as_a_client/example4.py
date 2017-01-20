# Example of a HEAD request

import requests

resp = requests.head('https://www.python.org')

status = resp.status_code
last_modified = resp.headers.get('last-modified')
content_type = resp.headers.get('content-type')
content_length = resp.headers.get('content-length')

print(status)
print(last_modified)
print(content_type)
print(content_length)
