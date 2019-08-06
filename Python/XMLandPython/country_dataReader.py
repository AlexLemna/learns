class country:
    def __init__ (self, name, rank, year, gdppc):
        self.name = name
        self.rank = rank
        self.year = year
        self.gdppc = gdppc

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

for child in root:
    print (child.tag, child.attrib)

for child in root:
    new_country = country( child.get('name'), child.find('rank').text, child.find('year').text, child.find('gdppc').text)
    print (new_country.name)
    print (f"   YEAR: {new_country.year}")
    print (f"   GDPPC: {new_country.gdppc}")
    print (f"   RANK: {new_country.rank}")





pass