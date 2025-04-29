import pandas as pd

# Data for Conceptual sheet (unchanged)
conceptual_data = [
    {"ComponentID": 1, "Function": "Web Channel", "SubFunction": "", "Status": "to be updated", "Connections": "Banking Engine", "Notes": "Faces customers"},
    {"ComponentID": 2, "Function": "Web Channel", "SubFunction": "Mobile Banking", "Status": "to be removed", "Connections": "", "Notes": ""},
    {"ComponentID": 3, "Function": "Web Channel", "SubFunction": "Responsive Website", "Status": "to be updated", "Connections": "", "Notes": ""},
    {"ComponentID": 4, "Function": "Customer Messaging", "SubFunction": "", "Status": "to be retained", "Connections": "Relationship Management", "Notes": ""},
    {"ComponentID": 5, "Function": "Customer Messaging", "SubFunction": "Campaign Messaging", "Status": "to be upgraded", "Connections": "", "Notes": ""},
    {"ComponentID": 6, "Function": "Customer Messaging", "SubFunction": "Automated Notifications", "Status": "to be added", "Connections": "", "Notes": ""},
    {"ComponentID": 7, "Function": "Banking Engine", "SubFunction": "", "Status": "as-is", "Connections": "Customer Data Platform", "Notes": ""},
    {"ComponentID": 8, "Function": "Relationship Management", "SubFunction": "", "Status": "to be updated", "Connections": "Customer Messaging", "Notes": "Sends email templates"},
    {"ComponentID": 9, "Function": "Customer Data Platform", "SubFunction": "", "Status": "to be added", "Connections": "", "Notes": ""}
]

# Data for Logical sheet (unchanged)
logical_data = [
    {"ComponentID": 1, "Module": "Web Channel", "SubModule": "", "Status": "to be updated", "Connections": "Banking Engine", "Notes": ""},
    {"ComponentID": 2, "Module": "Web Channel", "SubModule": "Adobe Experience Manager", "Status": "to be introduced", "Connections": "", "Notes": ""},
    {"ComponentID": 3, "Module": "Web Channel", "SubModule": "Drupal CMS", "Status": "to be removed", "Connections": "", "Notes": ""},
    {"ComponentID": 4, "Module": "Banking Engine", "SubModule": "", "Status": "as-is", "Connections": "Customer Data Platform,Relationship Management", "Notes": "Via APIGEE"},
    {"ComponentID": 5, "Module": "Banking Engine", "SubModule": "APIGEE API Gateway", "Status": "to be updated", "Connections": "", "Notes": ""},
    {"ComponentID": 6, "Module": "Customer Messaging", "SubModule": "", "Status": "to be retained", "Connections": "Relationship Management", "Notes": ""},
    {"ComponentID": 7, "Module": "Customer Messaging", "SubModule": "Adobe Campaign", "Status": "to be upgraded", "Connections": "", "Notes": ""},
    {"ComponentID": 8, "Module": "Customer Messaging", "SubModule": "AWS SNS", "Status": "to be introduced", "Connections": "", "Notes": ""},
    {"ComponentID": 9, "Module": "Customer Messaging", "SubModule": "Twilio SMS", "Status": "to be retained", "Connections": "", "Notes": ""},
    {"ComponentID": 10, "Module": "Relationship Management", "SubModule": "", "Status": "to be updated", "Connections": "Customer Messaging", "Notes": ""},
    {"ComponentID": 11, "Module": "Relationship Management", "SubModule": "MQ Email Templates", "Status": "to be removed", "Connections": "", "Notes": ""},
    {"ComponentID": 12, "Module": "Relationship Management", "SubModule": "Kafka Email Templates", "Status": "to be introduced", "Connections": "", "Notes": ""},
    {"ComponentID": 13, "Module": "Customer Data Platform", "SubModule": "", "Status": "to be added", "Connections": "", "Notes": ""},
    {"ComponentID": 14, "Module": "Customer Data Platform", "SubModule": "Oracle DB", "Status": "to be removed", "Connections": "", "Notes": "On-premise"},
    {"ComponentID": 15, "Module": "Customer Data Platform", "SubModule": "Postgres DB", "Status": "to be introduced", "Connections": "", "Notes": "On AWS"},
    {"ComponentID": 16, "Module": "Customer Data Platform", "SubModule": "DB2", "Status": "to be retained", "Connections": "", "Notes": "Mainframe"},
    {"ComponentID": 17, "Module": "Customer Data Platform", "SubModule": "MongoDB", "Status": "to be added", "Connections": "", "Notes": "For 360 analytics"}
]

# Data for Physical sheet (unchanged)
physical_data = [
    {"ComponentID": 1, "Component": "Web Channel", "SubComponent": "", "Status": "to be updated", "Connections": "Banking Engine", "Notes": ""},
    {"ComponentID": 2, "Component": "Web Channel", "SubComponent": "Adobe Experience Manager", "Status": "to be introduced", "Connections": "", "Notes": ""},
    {"ComponentID": 3, "Component": "Web Channel", "SubComponent": "WAF", "Status": "to be introduced", "Connections": "Adobe Experience Manager", "Notes": ""},
    {"ComponentID": 4, "Component": "Web Channel", "SubComponent": "CDN", "Status": "to be introduced", "Connections": "Adobe Experience Manager", "Notes": ""},
    {"ComponentID": 5, "Component": "Web Channel", "SubComponent": "EC2 Cluster", "Status": "to be updated", "Connections": "APIGEE API Gateway", "Notes": "9 EC2s, 3 AZs, eu-west"},
    {"ComponentID": 6, "Component": "Web Channel", "SubComponent": "S3 Bucket", "Status": "as-is", "Connections": "EC2 Cluster", "Notes": "Static assets"},
    {"ComponentID": 7, "Component": "Banking Engine", "SubComponent": "", "Status": "as-is", "Connections": "Customer Data Platform", "Notes": ""},
    {"ComponentID": 8, "Component": "Banking Engine", "SubComponent": "APIGEE API Gateway", "Status": "to be updated", "Connections": "Customer Data Platform", "Notes": ""},
    {"ComponentID": 9, "Component": "Customer Data Platform", "SubComponent": "", "Status": "to be added", "Connections": "", "Notes": ""},
    {"ComponentID": 10, "Component": "Customer Data Platform", "SubComponent": "Postgres DB", "Status": "to be introduced", "Connections": "", "Notes": "On AWS"},
    {"ComponentID": 11, "Component": "Customer Data Platform", "SubComponent": "MongoDB", "Status": "to be added", "Connections": "", "Notes": "For 360 analytics"},
    {"ComponentID": 12, "Component": "Relationship Management", "SubComponent": "", "Status": "to be updated", "Connections": "Customer Messaging", "Notes": ""},
    {"ComponentID": 13, "Component": "Relationship Management", "SubComponent": "Kafka Email Templates", "Status": "to be introduced", "Connections": "", "Notes": "Streaming for email templates"}
]

# Data for Legend sheet (new)
legend_data = [
    {"Status": "to be added", "Colour code": "Red", "Hex Code": "#FF0000"},
    {"Status": "to be removed", "Colour code": "Grey", "Hex Code": "#808080"},
    {"Status": "to be updated", "Colour code": "Yellow", "Hex Code": "#FFFF00"},
    {"Status": "to be used as is", "Colour code": "Green", "Hex Code": "#008000"}
]

# Create DataFrames
conceptual_df = pd.DataFrame(conceptual_data)
logical_df = pd.DataFrame(logical_data)
physical_df = pd.DataFrame(physical_data)
legend_df = pd.DataFrame(legend_data)

# Write to Excel
with pd.ExcelWriter("architecture.xlsx", engine="openpyxl") as writer:
    conceptual_df.to_excel(writer, sheet_name="Conceptual", index=False)
    logical_df.to_excel(writer, sheet_name="Logical", index=False)
    physical_df.to_excel(writer, sheet_name="Physical", index=False)
    legend_df.to_excel(writer, sheet_name="Legend", index=False)

print("Sample architecture.xlsx generated successfully with Legend sheet.")