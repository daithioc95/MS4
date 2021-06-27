import json

iterationOneIds = [
    35697, 36077, 36461, 36462,36463, 36464, 36465, 36466, 36467, 36468, 
    36469, 36470, 36471, 36472, 36473, 36474, 36475, 36476, 36477, 36478
]

with open('products/fixtures/output.json') as f:
    data = json.load(f, strict=False)
    out_data = []
    for i in data:
        for x in iterationOneIds:
            if i["Object ID"] == x:
                out_data.append(i)

with open('output2.json', 'w') as filehandle:
    json.dump(out_data, filehandle)

f.close()

# with open('products/fixtures/output.json') as data_file:    
#     data = json.load(data_file)
#     y = json.dumps(data[1])
#     print(y)