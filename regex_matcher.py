import sys
import re

file_path = sys.argv[1]

with open(file_path, "r") as file:
    file_content = file.readlines()
    
    file_content_str = ""
    for line in file_content:
        file_content_str += line
    
    file_content_str = file_content_str.replace("\n", "").replace("\r", "").replace("3D", "")
    # print(file_content_str)
    regex_pattern = "https://medium\.com/m/callback/email\?token=(\w+)=&operation=login&state=medium"
    
    result = re.search(regex_pattern, file_content_str)
    
    # print(f"result : {result.group()}")
    
    result = result.group()
    
    counter = 0
    result_str = ""
    for char in result:
        if char == "=":
            if counter == 1:
                counter += 1
                continue
            counter += 1
        result_str += char
        
    print(f"result : {result_str}")