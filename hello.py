import json
import os
import urllib.request

from bs4 import BeautifulSoup

headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Connection': 'keep-alive'
}

comments = []
for i in range(1, 6):
    url = 'https://www.v2ex.com/t/627214?p=' + str(i)
    print("爬取第%d页：%s" % (i, url))
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req, timeout=60)
    contents = response.read()
    contents = contents.decode('utf-8')
    # print(contents.decode('utf-8'))
    soup = BeautifulSoup(contents, "html.parser")
    for tag in soup.find_all('div', class_='cell'):
        if tag.get("id") is not None:
            reply_content_div = tag.find('div', class_='reply_content')
            # 评论内容
            reply_content = reply_content_div.get_text()
            # 用户名，用户首页
            username_ele = tag.find("strong")
            username_ele_a = username_ele.find("a")

            # 组装
            comment = {"id": tag.get("id"), "user_name": username_ele_a.get_text(),
                       "user_home": "https://www.v2ex.com" + username_ele_a.get("href"), "content": reply_content}
            comments.append(comment)

            # print("****************************************************")
            # print(tag.get("id"))
            # print(username_ele_a.get_text())
            # print("https://www.v2ex.com" + username_ele_a.get("href"))
            # print(reply_content)
    print(len(comments))

print(comments[0])
print(comments[-1])
print("总条数：%d" % len(comments))
print("用户目录：" + os.path.expanduser('~'))
print("分隔符：" + os.sep)
with open("comments.json", 'w', encoding='utf-8') as f:
    json.dump(comments, f, indent=4, ensure_ascii=False)
