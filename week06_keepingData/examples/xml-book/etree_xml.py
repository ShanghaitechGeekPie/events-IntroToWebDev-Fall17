try:
    import xml.etree.cElementTree as xet
except ImportError:
    import xml.etree.ElementTree as xet

def xmlBasicExample(path_to_xml_file):
    """
    Read XML sample and demonstrates how `xml.etree` library works.
    """
    
    catalog = xet.ElementTree(file=path_to_xml_file)

    cat_root = catalog.getroot()
    print(cat_root)

    for book_node in cat_root:
        print(book_node.tag, book_node.attrib, sep=' -> ')
        for sub_node in book_node.getchildren():
            print(sub_node.tag, sub_node.text, sep='\t\t')


if __name__ == '__main__':
    xmlBasicExample('books.xml')
