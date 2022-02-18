import xml.etree.ElementTree as ET
import pandas as pd
import urllib.request as urllib2

file = urllib2.urlopen('http://weather.cyi.ac.cy/data/met/CyDoM.xml')
xml_data = file.read()
file.close()
root = ET.XML(xml_data)  # Parse XML
data = {}
skato_xml = root.findall('.//observations')
for entries in skato_xml:
    for entry in entries:
        if entry.tag == 'station_code':
            current_name = entry.text
            data[entry.text] = {}
        if entry.tag == 'date_time':
            data[current_name]['data_time'] = entry.text
        if entry.tag == 'observation':
            for famoutin in entry:
                if famoutin.tag == 'observation_name':
                    current_attribute = famoutin.text
                    data[current_name][current_attribute] = ""
                if famoutin.tag == 'observation_value':
                    data[current_name][current_attribute] += famoutin.text
                if famoutin.tag == 'observation_unit':
                    data[current_name][current_attribute] += famoutin.text
print("IME I STILLA HUEHUE")
df = pd.DataFrame.from_dict(data)
df.to_excel('stilla.xlsx')
