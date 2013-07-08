from xml.dom import minidom

xmldoc = minidom.parse('configurable/board.xml')

board = xmldoc.getElementsByTagName('initialBoard')
print board