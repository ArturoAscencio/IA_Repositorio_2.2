# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install googlesearch-python

from googlesearch import search

# T�rminos de b�squeda
query = "Python programming"

# Realiza una b�squeda en Google en l�nea
for result in search(query, num=5, stop=5, pause=2):
    print(result)
