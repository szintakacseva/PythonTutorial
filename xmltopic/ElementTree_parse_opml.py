from xml.etree import ElementTree

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)
print (tree)

for node in tree.iter():
    print (node.tag, node.attrib)

for node in tree.iter('outline'):
    name = node.attrib.get('text')
    url = node.attrib.get('xmlUrl')
    if name and url:
        print ('  %s :: %s' % (name, url))
    else:
        print (name)

for node in tree.findall('.//outline'):
    url = node.attrib.get('xmlUrl')
    if url:
        print (url)

for node in tree.findall('.//outline/outline'):
    url = node.attrib.get('xmlUrl')
    print (url)

with open('data.xml', 'rt') as f:
    tree = ElementTree.parse(f)

node = tree.find('./with_attributes')
print (node.tag)
for name, value in sorted(node.attrib.items()):
    print ('  %-4s = "%s"' % (name, value))

for path in [ './child', './child_with_tail' ]:
    node = tree.find(path)
    print (node.tag)
    print ('  child node text:', node.text)
    print ('  and tail text  :', node.tail)