import pandas as pd
import json
import meilisearch

with open("allitems.json", "r") as f:
    cve = json.load(f)
    print(cve.keys())

cve_list = []
for i in range(len(cve)):
    k = str(i)
    cve_info = {
        "Name": cve["ï»¿Name"][k],
        "Status": cve["Status"][k],
        "Description": cve["Description"][k],
        "References": cve["References"][k],
        "Phase": cve["Phase"][k],
        "Votes": cve["Votes"][k],
        "Comments": cve["Comments"][k],
    }
    cve_list.append(cve_info)


client = meilisearch.Client('http://ais3.shiya.site/meili')
for i in range(len(cve_list)):
    # print(cve_list[i])
    # client.index('movies').search('botman')

    client.index('cve').add_documents([cve_list[i]])
    break
