import sys
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree

top = Element('top')

comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child')
child.text = 'This child contains text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has regular text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'

empty_child = SubElement(top, 'empty_child')

ElementTree(top).write("elementree.xml")
#sys.stdout.write(str(ElementTree(top)))


for method in [ 'xml', 'html', 'text' ]:
    print (method)
    #ElementTree(top).write(sys.stdout, method=method)
    #sys.stdout.write(str(ElementTree(top)), method=method)
    ElementTree(top).write("elementree.xml")
    print ('\n')
