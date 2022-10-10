import os
import re

# 重新生成_sidebar.md
# os.remove("_sidebar.md")
# os.system("docsify generate .")

re_compile = re.compile(r']\((?P<rout>.*?)\)')

bookNames = []
bookRoutes = []
with open('_sidebar.md', 'r', encoding='utf-8') as router:
    n = 0
    for readline in router:
        if readline.startswith("-") and readline != '- [ABook](ABook.md)\n':
            bookNames.append(readline.replace("- ", ""))
            n = n + 1
            continue
        if n == 1:
            finditer = re_compile.finditer(readline)
            for r in finditer:
                group = r.group("rout")
                bookRoutes.append(group)
            n = 0

# 覆写Abook.md文件
with open("ABook.md", "w", encoding='utf-8') as readme:
    readme.write("# A-Book\n")
    for a in range(len(bookRoutes)):
        readme.write(f"{a + 1}. [{bookNames[a].strip()}]({bookRoutes[a]})\n")
