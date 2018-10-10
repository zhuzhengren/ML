#!/usr/bin/python
import json
data = {'number': 6, 'name': 'Pythontab'}
jsonData = json.dumps(data, sort_keys=True,indent=4,separators=(',',': '))
print(jsonData)
print(type(jsonData))

str = json.loads(jsonData)
print((str))

d = {'name1' : 'pythontab', 'name2' : '.', 'name3' : 'com'}
for key in d:
    print (key, ' value : ', d[key])


for key, value in d.items():
    print (key, ' value : ', value)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import io
import re
from lxml import etree
def generate_xml(filename, url_list):
  """Generate a new xml file use url_list"""
  root = etree.Element('urlset',
             xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
  for each in url_list:
    url = etree.Element('url')
    loc = etree.Element('loc')
    loc.text = each
    url.append(loc)
    root.append(url)
  header = u'<?xml version="1.0" encoding="UTF-8"?>\n'
  s = etree.tostring(root, encoding='utf-8', pretty_print=True)
  with io.open(filename, 'w', encoding='utf-8') as f:
    f.write(unicode(header+s))
def update_xml(filename, url_list):
  """Add new url_list to origin xml file."""
  f = open(filename, 'r')
  lines = [i.strip() for i in f.readlines()]
  f.close()
  old_url_list = []
  for each_line in lines:
    d = re.findall('<loc>(http:\/\/.+)<\/loc>', each_line)
    old_url_list += d
  url_list += old_url_list
  generate_xml(filename, url_list)
def generatr_xml_index(filename, sitemap_list, lastmod_list):
  """Generate sitemap index xml file."""
  root = etree.Element('sitemapindex',
             xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
  for each_sitemap, each_lastmod in zip(sitemap_list, lastmod_list):
    sitemap = etree.Element('sitemap')
    loc = etree.Element('loc')
    loc.text = each_sitemap
    lastmod = etree.Element('lastmod')
    lastmod.text = each_lastmod
    sitemap.append(loc)
    sitemap.append(lastmod)
    root.append(sitemap)
  header = u'<?xml version="1.0" encoding="UTF-8"?>\n'
  s = etree.tostring(root, encoding='utf-8', pretty_print=True)
  with io.open(filename, 'w', encoding='utf-8') as f:
    f.write(unicode(header+s))
if __name__ == '__main__':
  urls = ['http://www.baidu.com'] * 10
  mods = ['2004-10-01T18:23:17+00:00'] * 10
  generatr_xml_index('index.xml', urls, mods)
