from xml.dom import minidom

xmldoc = minidom.parse('configurable/board.xml')

#board = xmldoc.getElementsByTagName('initialBoard')
list =  xmldoc.childNodes
#print list[1]
board = xmldoc.getElementsByTagName('initialBoard')

print board[0].toxml()