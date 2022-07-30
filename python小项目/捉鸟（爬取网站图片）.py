import requests
import re
import time
for number in range(1,11):
    url = ''+'/'+str(number)
    resp=requests.get(url)
    resp.encoding='utf-8'
    page_content=resp.text
    obj=re.compile(r'<p><img loading="lazy" class="aligncenter .*?src="(?P<name>.*?)"',re.S)
    result=obj.finditer(page_content)
    for it in result:
        img_resp=requests.get(it.group("name"))
        name1=it.group("name").split('/')[-1]
        with open(name1,mode='wb') as f:
            f.write(img_resp.content)
        print("over",name1)
        time.sleep(1)