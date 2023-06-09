import json

with open('ex5.json','r') as file:
    ex5=json.load(file)
    
for x in ex5:
    if x['type'] == "donut" and x['name'] == 'Old Fashioned':
        # print(x)
    
        z=x['batters']['batter']
        # print(z)
        z.append({'id': '1003', 'type': 'Coffee'})
        # print(z)
        
with open('ex5.json','w') as file:
    json.dump(ex5,file,indent=4)