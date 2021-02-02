import json 
  
  
# function to add to JSON 
def write_json(data, filename='config.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      
      
with open('config.json') as json_file: 
    data = json.load(json_file) 
      
    temp = data['clients'] 
  
    # python object to be appended 
    y = {"id":'97ecc095-d518-4b15-a4e4-906fa4f49bcb', 
         "level": "0", 
         "email": "nikhil@geeksforgeeks.org"
        } 
  
  
    # appending data to clients  
    temp.append(y) 
      
write_json(data)
