import re

html = open("Suomen_kielen_lyhenteet.html")
abbr_list_output = open("suomilyhenteet3.txt", "w")
output_list = []

for line in html:
    abbr = re.findall('title="(.+\..*)">.+\..*?<', line)
    if len(abbr) > 0:    
        output_list.extend(abbr)

for elem in output_list:

    abbr_list_output.write(elem + "\n")
