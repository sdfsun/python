# encoding=utf-8
import time

str1 = '华为科技有限公司'
str2 = str(str1.encode('unicode_escape').upper()).replace(r"\\U", r"\u").split("'")[1]
print(str2)

print(time.time() - 1E3)

print(b'\\u2011'.decode('unicode_escape'))
