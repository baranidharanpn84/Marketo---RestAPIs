from marketorestpython.client import MarketoClient
from datetime import datetime
import sys, csv, os, pandas

#datetimeobject = datetime.strptime(sys.argv[1], '%Y-%m-%dT%H:%M:%SZ')
#arg_1 = datetime.strptime(sys.argv[1],'%Y-%m-%d')
#print (arg_1)

export_file = 'D:/Marketo/export/talend_activity_extract.csv'

munchkin_id ="347-IAT-677" # Sunrun -- "935-SWT-917" ### Enter Munchkin ID
client_id = "fadff194-6e4f-4dec-a3fa-bf64b66e3d69" # "87be116a-e24f-43fb-b616-79368441eff7" # Sunrun -- "d71f8506-15bd-4629-a06d-1bdab5e58470" ### enter client ID (find in Admin > LaunchPoint > view details)
client_secret = "a6TnnjDyiVWq6dtFAmabQOfZJcGkLmJW" # "kpd83NdSCKW1mo8s0g9lZ5PmHChbrinr" # Sunrun -- "xWCRpT4awkrhB5FYfbDVUyr7P4VTfvXJ" ### enter client secret (find in Admin > LaunchPoint > view details)

mc = MarketoClient(munchkin_id, client_id, client_secret)

if __name__ == "__main__":
    a=0
    for activities in mc.execute(method='get_lead_activities_yield', activityTypeIds=['41','42','43','44','45','46','47','48','101','102'],
                                 nextPageToken=None, sinceDatetime=sys.argv[1], untilDatetime=sys.argv[2], listId=75364):

        records1 = pandas.DataFrame(index=range(0, len(activities)),
                                    columns=['MarketoGUID', 'Lead ID', 'Activity Date', 'Activity Type ID',
                                             'Primary Attribute Value Id', 'Primary Attribute Value', 'Attributes'])

        for index, item in enumerate(activities):
            if int(item["marketoGUID"]) > int(sys.argv[3]): ##update this
                records1.set_value(index, 'MarketoGUID', item["marketoGUID"])
                records1.set_value(index, 'Lead ID', item["leadId"])
                if 'activityDate' in item:
                    records1.set_value(index, 'Activity Date', item["activityDate"])
                if 'activityTypeId' in item:
                    records1.set_value(index, 'Activity Type ID', item["activityTypeId"])
                if 'primaryAttributeValueId' in item:
                    records1.set_value(index, 'Primary Attribute Value Id', item["primaryAttributeValueId"])
                if 'primaryAttributeValue' in item:
                    records1.set_value(index, 'Primary Attribute Value', item["primaryAttributeValue"])
                if 'attributes' in item:
                    records1.set_value(index, 'Attributes', item["attributes"])

        a = a + len(activities)
        print(a)
        records1.to_csv(export_file, sep=',', header=True, encoding='utf-8-sig', index=False, mode='a')