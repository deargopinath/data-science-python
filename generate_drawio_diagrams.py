import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

# Updated status to color mapping based on user-provided legend
status_colors = {
    "as-is": "#008000",  # Green (to be used as is)
    "to be removed": "#808080",  # Grey
    "to be added": "#FF0000",  # Red
    "to be introduced": "#FF0000",  # Red (mapped to to be added)
    "to be updated": "#FFFF00",  # Yellow
    "to be upgraded": "#FFFF00",  # Yellow (mapped to to be updated)
    "to be retained": "#008000"  # Green (to be used as is)
}

# Legend entries (status and color)
legend_entries = [
    {"status": "to be added", "color": "#FF0000"},
    {"status": "to be removed", "color": "#808080"},
    {"status": "to be updated", "color": "#FFFF00"},
    {"status": "to be used as is", "color": "#008000"}
]

# Shape mapping for Logical and Physical diagrams (using mxgraph.aws4)
shapes = {
    "EC2 Cluster": "shape=mxgraph.aws4.ec2_instance;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "S3 Bucket": "shape=mxgraph.aws4.s3_bucket;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "Postgres DB": "shape=mxgraph.aws4.rds;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "APIGEE API Gateway": "shape=mxgraph.aws4.api_gateway;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "CDN": "shape=mxgraph.aws4.cloudfront;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "WAF": "shape=mxgraph.aws4.waf;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "VPC": "shape=mxgraph.aws4.vpc;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "ELB": "shape=mxgraph.aws4.elastic_load_balancer;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "Auto Scaling": "shape=mxgraph.aws4.auto_scaling;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "Lambda": "shape=mxgraph.aws4.lambda_function;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "Route 53": "shape=mxgraph.aws4.route_53;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "AWS SNS": "shape=mxgraph.aws4.sns;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "Kafka Email Templates": "shape=mxgraph.aws4.msk;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "MongoDB": "shape=mxgraph.aws4.database;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "Oracle DB": "shape=mxgraph.aws4.database;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;",
    "DB2": "shape=mxgraph.aws4.database;fillColor={color};strokeColor=#000000;labelPosition=right;align=left;"
}

# Custom image mappings (base64-encoded placeholders)
custom_images = {
    "Adobe Experience Manager": "image=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAkUlEQVR4nO3WsQnAMAhE0f+7S7tF0F2sO3iG7qF2R7oQBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBD4JfwA4hWTVV3kJusAAAAASUVORK5CYII=;fillColor={color};labelPosition=right;align=left;",
    "Drupal CMS": "image=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAkUlEQVR4nO3WsQnAMAhE0f+7S7tF0F2sO3iG7qF2R7oQBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBD4JfwA4hWTVV3kJusAAAAASUVORK5CYII=;fillColor={color};labelPosition=right;align=left;",
    "Twilio SMS": "image=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAkUlEQVR4nO3WsQnAMAhE0f+7S7tF0F2sO3iG7qF2R7oQBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgUAgEAgEAoFAIBD4JfwA4hWTVV3kJusAAAAASUVORK5CYII=;fillColor={color};labelPosition=right;align=left;"
}

# Read Excel file with multiple sheets
def read_architecture_data(file_path):
    xls = pd.ExcelFile(file_path)
    conceptual = pd.read_excel(xls, sheet_name="Conceptual")
    logical = pd.read_excel(xls, sheet_name="Logical")
    physical = pd.read_excel(xls, sheet_name="Physical")
    return conceptual, logical, physical

# Generate Draw.io XML for a diagram
def create_drawio_diagram(data, diagram_type, output_file):
    is_conceptual = diagram_type == "Conceptual"
    
    # XML root
    root = ET.Element("mxfile", host="app.diagrams.net", modified="2025-04-28T12:00:00Z", 
                     agent="Grok3", version="21.0.0")
    diagram = ET.SubElement(root, "diagram", name=f"{diagram_type} Architecture", id="diagram_1")
    mxGraphModel = ET.SubElement(diagram, "mxGraphModel", dx="800", dy="600", grid="1", 
                                gridSize="10", guides="1", tooltips="1", connect="1", 
                                arrows="1", fold="1", page="1", pageScale="1", 
                                pageWidth="850", pageHeight="1100", background="#ffffff")
    rootGraph = ET.SubElement(mxGraphModel, "root")

    # Default cells
    cell0 = ET.SubElement(rootGraph, "mxCell", id="0")
    cell1 = ET.SubElement(rootGraph, "mxCell", id="1", parent="0")

    components = {}
    y_offset = 50
    cluster_id = 2
    node_id = 100

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
        color = status_colors.get(status, "#FFFFFF")

        # Create cluster (swimlane) with increased height to avoid overlaps
        cluster = ET.SubElement(rootGraph, "mxCell", id=str(cluster_id), value=main_name, 
                               style=f"swimlane;fillColor={color};strokeColor=#000000;rounded=0;fontSize=14;fontStyle=1;", 
                               vertex="1", parent="1")
        cluster_geo = ET.SubElement(cluster, "mxGeometry", x="50", y=str(y_offset), 
                                   width="400", height="400", **{"as": "geometry"})
        components[main_id] = str(cluster_id)
        cluster_id += 1

        # Add subcomponents with adjusted spacing
        subcomponents = data[(data["ComponentID"] != main_id) & 
                            ((data["Function" if diagram_type == "Conceptual" 
                                 else "Module" if diagram_type == "Logical" 
                                 else "Component"] == main_name))]
        sub_y = y_offset + 50
        for _, sub_row in subcomponents.iterrows():
            sub_id = sub_row["ComponentID"]
            sub_name = sub_row["SubFunction" if diagram_type == "Conceptual" 
                              else "SubModule" if diagram_type == "Logical" 
                              else "SubComponent"]
            sub_status = sub_row["Status"]
            sub_color = status_colors.get(sub_status, "#FFFFFF")

            # Use custom images, AWS shapes, or generic shapes
            if not is_conceptual and sub_name in custom_images:
                style = custom_images[sub_name].format(color=sub_color)
            elif not is_conceptual and sub_name in shapes:
                style = shapes[sub_name].format(color=sub_color)
            else:
                style = f"rounded=1;fillColor={sub_color};strokeColor=#000000;fontSize=12;labelPosition=right;align=left;"
            
            node = ET.SubElement(rootGraph, "mxCell", id=str(node_id), value=sub_name, 
                                style=style, vertex="1", parent=str(cluster_id-1))
            node_geo = ET.SubElement(node, "mxGeometry", x="80", y=str(sub_y-y_offset), 
                                    width="250", height="60", **{"as": "geometry"})
            components[sub_id] = str(node_id)
            node_id += 1
            sub_y += 80  # Increased spacing between nodes
        
        y_offset += 450  # Increased spacing between swimlanes

    # Create connections
    for _, row in data.iterrows():
        component_id = row["ComponentID"]
        connections = row["Connections"]
        
        if pd.notna(connections):
            connected_names = [conn.strip() for conn in connections.split(",")]
            source_id = components.get(component_id)
            
            for conn_name in connected_names:
                target_id = data[(data["Function" if diagram_type == "Conceptual" 
                                     else "Module" if diagram_type == "Logical" 
                                     else "Component"] == conn_name) | 
                                (data["SubFunction" if diagram_type == "Conceptual" 
                                    else "SubModule" if diagram_type == "Logical" 
                                    else "SubComponent"] == conn_name)]["ComponentID"]
                if not target_id.empty:
                    target_component = components.get(target_id.iloc[0])
                    if source_id and target_component:
                        edge = ET.SubElement(rootGraph, "mxCell", id=str(node_id), value="", 
                                            style="edgeStyle=orthogonalEdgeStyle;rounded=0;endArrow=block;endFill=1;strokeColor=#000000;fontSize=10;", 
                                            edge="1", source=source_id, target=target_component, parent="1")
                        edge_geo = ET.SubElement(edge, "mxGeometry", relative="1", **{"as": "geometry"})
                        node_id += 1

    # Add legend box at the bottom
    legend_y = y_offset + 50
    legend_id = node_id
    legend = ET.SubElement(rootGraph, "mxCell", id=str(legend_id), value="Legend", 
                           style="swimlane;fillColor=#FFFFFF;strokeColor=#000000;rounded=0;fontSize=14;fontStyle=1;", 
                           vertex="1", parent="1")
    legend_geo = ET.SubElement(legend, "mxGeometry", x="50", y=str(legend_y), 
                               width="400", height="100", **{"as": "geometry"})
    node_id += 1

    # Add legend entries (colored rectangles with labels)
    legend_x = 80
    for entry in legend_entries:
        status = entry["status"]
        color = entry["color"]
        # Rectangle for color
        rect = ET.SubElement(rootGraph, "mxCell", id=str(node_id), value="", 
                             style=f"shape=rectangle;fillColor={color};strokeColor=#000000;", 
                             vertex="1", parent=str(legend_id))
        ET.SubElement(rect, "mxGeometry", x=str(legend_x), y=str(40), 
                      width="30", height="20", **{"as": "geometry"})
        node_id += 1
        # Label for status
        label = ET.SubElement(rootGraph, "mxCell", id=str(node_id), value=status, 
                              style="text;strokeColor=none;fillColor=none;align=left;fontSize=12;", 
                              vertex="1", parent=str(legend_id))
        ET.SubElement(label, "mxGeometry", x=str(legend_x + 40), y=str(40), 
                      width="100", height="20", **{"as": "geometry"})
        node_id += 1
        legend_x += 120

    # Write XML to file
    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(xml_str)

# Main execution
if __name__ == "__main__":
    excel_file = "architecture.xlsx"
    try:
        conceptual_data, logical_data, physical_data = read_architecture_data(excel_file)
        
        # Generate diagrams
        create_drawio_diagram(conceptual_data, "Conceptual", "conceptual_architecture.xml")
        create_drawio_diagram(logical_data, "Logical", "logical_architecture.xml")
        create_drawio_diagram(physical_data, "Physical", "physical_architecture.xml")
        
        print("Draw.io diagrams generated: conceptual_architecture.xml, logical_architecture.xml, physical_architecture.xml")
    except Exception as e:
        print(f"Error: {e}")