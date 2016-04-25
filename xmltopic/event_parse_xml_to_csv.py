import csv
from xml.etree.ElementTree import iterparse
import sys

#writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
with open('podcasts.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    group_name = ''

    for (event, node) in iterparse('podcasts.opml', events=['start']):
        if node.tag != 'outline':
            # Ignore anything not part of the outline
            continue
        if not node.attrib.get('xmlUrl'):
            # Remember the current group
            group_name = node.attrib['text']
        else:
            # Output a podcast entry
            writer.writerow( (group_name, node.attrib['text'],
                              node.attrib['xmlUrl'],
                              node.attrib.get('htmlUrl', ''),
                              )
                             )