#XML BillionLaughAttack
import xml.etree.ElementTree as ET
#from defusedxml.ElementTree import parse #fix
tree = ET.parse('country_data.xml')
root = tree.getroot()
