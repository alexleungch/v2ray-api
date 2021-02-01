import json 
  
  
# function to add to JSON 
def write_json(data, filename='data.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      
      
with open('data.json') as json_file: 
    data = json.load(json_file) 
      
    temp = data['emp_details'] 
  
    # python object to be appended 
    y = {"emp_name":'Nikhil', 
         "email": "nikhil@geeksforgeeks.org", 
         "job_profile": "Full Time"
        } 
  
  
    # appending data to emp_details  
    temp.append(y) 
      
write_json(data)
