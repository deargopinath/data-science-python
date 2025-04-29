import pandas as pd
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway, CloudFront
from diagrams.aws.security import WAF
from diagrams.custom import Custom

# Status to color mapping
status_colors = {
    "as-is": "lightblue",
    "to be removed": "red",
    "to be added": "green",
    "to be introduced": "green",
    "to be updated": "yellow",
    "to be upgraded": "yellow",
    "to be retained": "lightblue"
}

# Component mapping for Physical diagram
physical_component_mapping = {
    "EC2 Cluster": EC2,
    "S3 Bucket": S3,
    "Postgres DB": RDS,
    "APIGEE API Gateway": APIGateway,
    "CDN": CloudFront,
    "WAF": WAF
}

# Read Excel file with multiple sheets
def read_architecture_data(file_path):
    xls = pd.ExcelFile(file_path)
    conceptual = pd.read_excel(xls, sheet_name="Conceptual")
    logical = pd.read_excel(xls, sheet_name="Logical")
    physical = pd.read_excel(xls, sheet_name="Physical")
    return conceptual, logical, physical

# Generate diagram for a given sheet
def create_diagram(data, diagram_type, output_file):
    # Determine node type based on diagram type
    is_physical = diagram_type == "Physical"
    title = f"{diagram_type} Architecture"
    
    with Diagram(title, show=False, filename=output_file, outformat="png", direction="LR"):
        components = {}
        
        # Group components by main component for clustering
        main_components = data[data["SubFunction"].isna() if diagram_type == "Conceptual" 
                              else data["SubModule"].isna() if diagram_type == "Logical" 
                              else data["SubComponent"].isna()]
        
        for _, row in main_components.iterrows():
            main_id = row["ComponentID"]
            main_name = row["Function" if diagram_type == "Conceptual" 
                          else "Module" if diagram_type == "Logical" 
                          else "Component"]
            status = row["Status"]
            color = status_colors.get(status, "white")
            
            with Cluster(main_name):
                # Create main component node
                if is_physical and main_name in physical_component_mapping:
                    component_class = physical_component_mapping[main_name]
                    components[main_id] = component_class(main_name, fillcolor=color, style="filled")
                else:
                    components[main_id] = Custom(main_name, "./custom.png", fillcolor=color, style="filled")
                
                # Add subcomponents
                subcomponents = data[(data["ComponentID"] != main_id) & 
                                   ((data["Function" if diagram_type == "Conceptual" 
                                        else "Module" if diagram_type == "Logical" 
                                        else "Component"] == main_name))]
                for _, sub_row in subcomponents.iterrows():
                    sub_id = sub_row["ComponentID"]
                    sub_name = sub_row["SubFunction" if diagram_type == "Conceptual" 
                                     else "SubModule" if diagram_type == "Logical" 
                                     else "SubComponent"]
                    sub_status = sub_row["Status"]
                    sub_color = status_colors.get(sub_status, "white")
                    
                    if is_physical and sub_name in physical_component_mapping:
                        component_class = physical_component_mapping[sub_name]
                        components[sub_id] = component_class(sub_name, fillcolor=sub_color, style="filled")
                    else:
                        components[sub_id] = Custom(sub_name, "./custom.png", fillcolor=sub_color, style="filled")
        
        # Create connections
        for _, row in data.iterrows():
            component_id = row["ComponentID"]
            connections = row["Connections"]
            
            if pd.notna(connections):
                connected_names = [conn.strip() for conn in connections.split(",")]
                source_component = components.get(component_id)
                
                for conn_name in connected_names:
                    # Find target component by name or subcomponent name
                    target_id = data[(data["Function" if diagram_type == "Conceptual" 
                                          else "Module" if diagram_type == "Logical" 
                                          else "Component"] == conn_name) | 
                                   (data["SubFunction" if diagram_type == "Conceptual" 
                                       else "SubModule" if diagram_type == "Logical" 
                                       else "SubComponent"] == conn_name)]["ComponentID"]
                    if not target_id.empty:
                        target_component = components.get(target_id.iloc[0])
                        if source_component and target_component:
                            source_component >> Edge(color="black") >> target_component
                        else:
                            print(f"Warning: Connection to '{conn_name}' not found in {diagram_type}")

# Main execution
if __name__ == "__main__":
    excel_file = "architecture.xlsx"
    conceptual_data, logical_data, physical_data = read_architecture_data(excel_file)
    
    # Generate diagrams
    create_diagram(conceptual_data, "Conceptual", "conceptual_architecture")
    create_diagram(logical_data, "Logical", "logical_architecture")
    create_diagram(physical_data, "Physical", "physical_architecture")
    
    print("Diagrams generated: conceptual_architecture.png, logical_architecture.png, physical_architecture.png")