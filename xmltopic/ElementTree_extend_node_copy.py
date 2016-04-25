from xml.etree.ElementTree import Element, SubElement, Comment, XML
from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

top = Element('top')

parent_a = SubElement(top, 'parent', id='A')
parent_b = SubElement(top, 'parent', id='B')

# Create children
children = XML('''<root><child num="0" /><child num="1" /><child num="2" /></root> ''')

# Set the id to the Python object id of the node to make duplicates
# easier to spot.
for c in children:
    c.set('id', str(id(c)))

# Add to first parent
parent_a.extend(children)

ElementTree.ElementTree(top).write("elementree.xml")


print ('A:')
print (prettify(top))
print

# Copy nodes to second parent
parent_b.extend(children)

print ('B:')
print (prettify(top))
print
