import pandas as pd

# Status to color mapping (CSS colors for Mermaid)
status_colors = {
    "as-is": "lightblue",
    "to be removed": "red",
    "to be added": "green",
    "to be introduced": "green",
    "to be updated": "yellow",
    "to be upgraded": "yellow",
    "to be retained": "lightblue"
}

# AWS icon mapping for Physical diagram (Iconify icons)
aws_icons = {
    "EC2 Cluster": "aws-ec2",
    "S3 Bucket": "aws-s3",
    "Postgres DB": "aws-rds",
    "APIGEE API Gateway": "aws-api-gateway",
    "CDN": "aws-cloudfront",
    "WAF": "aws-waf"
}

# Read Excel file with multiple sheets
def read_architecture_data(file_path):
    xls = pd.ExcelFile(file_path)
    conceptual = pd.read_excel(xls, sheet_name="Conceptual")
    logical = pd.read_excel(xls, sheet_name="Logical")
    physical = pd.read_excel(xls, sheet_name="Physical")
    return conceptual, logical, physical

# Generate Mermaid syntax for a diagram
def create_mermaid_diagram(data, diagram_type, output_file):
    is_physical = diagram_type == "Physical"
    lines = [f"architecture-beta"]
    lines.append(f"    %% {diagram_type} Architecture")
    
    components = {}
    subgraph_id = 1
    node_id = 1

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
        
        # Create subgraph (cluster)
        safe_main_name = main_name.replace(" ", "_").replace("-", "_")
        lines.append(f"    subsystem {safe_main_name} {{")
        node_name = f"N{node_id}"
        if is_physical and main_name in aws_icons:
            lines.append(f"        {node_name}[[\"aws-{main_name}\" fa:fa-cloud]]:::status_{status.replace(' ', '_')}")
        else:
            lines.append(f"        {node_name}[[\"{main_name}\"]]:::status_{status.replace(' ', '_')}")
        components[main_id] = node_name
        node_id += 1

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
            
            sub_node_name = f"N{node_id}"
            if is_physical and sub_name in aws_icons:
                lines.append(f"        {sub_node_name}[[\"aws-{sub_name}\" fa:fa-cloud]]:::status_{sub_status.replace(' ', '_')}")
            else:
                lines.append(f"        {sub_node_name}[[\"{sub_name}\"]]:::status_{sub_status.replace(' ', '_')}")
            components[sub_id] = sub_node_name
            node_id += 1
        
        lines.append(f"    }}")
        subgraph_id += 1

    # Create connections
    for _, row in data.iterrows():
        component_id = row["ComponentID"]
        connections = row["Connections"]
        
        if pd.notna(connections):
            connected_names = [conn.strip() for conn in connections.split(",")]
            source_node = components.get(component_id)
            
            for conn_name in connected_names:
                target_id = data[(data["Function" if diagram_type == "Conceptual" 
                                     else "Module" if diagram_type == "Logical" 
                                     else "Component"] == conn_name) | 
                                (data["SubFunction" if diagram_type == "Conceptual" 
                                    else "SubModule" if diagram_type == "Logical" 
                                    else "SubComponent"] == conn_name)]["ComponentID"]
                if not target_id.empty:
                    target_node = components.get(target_id.iloc[0])
                    if source_node and target_node:
                        lines.append(f"    {source_node} --> {target_node}")

    # Add CSS styles for status colors
    lines.append("    %% Styles")
    for status, color in status_colors.items():
        safe_status = status.replace(" ", "_")
        lines.append(f"    classDef status_{safe_status} fill:{color},stroke:#333,stroke-width:2px;")

    # Write to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

# Main execution
if __name__ == "__main__":
    excel_file = "architecture.xlsx"
    conceptual_data, logical_data, physical_data = read_architecture_data(excel_file)
    
    # Generate diagrams
    create_mermaid_diagram(conceptual_data, "Conceptual", "conceptual_architecture.mmd")
    create_mermaid_diagram(logical_data, "Logical", "logical_architecture.mmd")
    create_mermaid_diagram(physical_data, "Physical", "physical_architecture.mmd")
    
    print("Mermaid diagrams generated: conceptual_architecture.mmd, logical_architecture.mmd, physical_architecture.mmd")