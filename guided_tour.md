# Guided Tour: Generating Cloud Architecture Diagrams from Excel

This document provides a comprehensive guide to generating cloud architecture diagrams from an Excel file using open-source tools (Diagrams, Draw.io, Mermaid.js). It covers the requirements, tool comparisons, code implementations, and sample data for a 3-tier web application for a bank.

## Step 1: Define Requirements
- **Input**: Excel file with three sheets (Conceptual, Logical, Physical).
  - **Conceptual**: Business functions (e.g., Web Channel) and hierarchy.
  - **Logical**: Technical modules (e.g., Adobe Experience Manager) and interconnections.
  - **Physical**: Cloud components (e.g., EC2, S3), VPCs, firewalls, etc.
  - Each sheet includes a "Status" column (e.g., "as-is", "to be removed") for color coding.
- **Output**: Three diagrams (Conceptual, Logical, Physical) as PNG or other formats.
- **Functionality**:
  - Read Excel using Python (pandas).
  - Map data to diagram elements (nodes, edges, clusters).
  - Apply status-based colors (e.g., green for "to be added").
  - Support AWS icons for Physical diagram.
- **Tools**: Open-source, Python-based, supporting AWS/Azure/GCP.

## Step 2: Explore Open-Source Tools
### Diagrams
- **Description**: Python-based "Diagrams as Code" for cloud architectures.
- **Pros**: Seamless Python integration, native AWS/Azure/GCP icons, easy automation.
- **Cons**: Static diagrams, limited custom icons.
- **Suitability**: High for automation and cloud diagrams.

### Draw.io (Diagrams.net)
- **Description**: Web-based diagramming with XML-based programmatic support.
- **Pros**: Extensive AWS icon library, interactive editing, versatile.
- **Cons**: Complex XML generation, manual refinement needed.
- **Suitability**: Moderate, best for flexibility and manual edits.

### Mermaid.js
- **Description**: Text-based diagramming with Markdown-like syntax.
- **Pros**: Simple, Git-friendly, supports Iconify icons.
- **Cons**: Limited cloud icons, architecture diagrams in beta.
- **Suitability**: Moderate, best for simple diagrams in documentation.

### PlantUML and Graphviz
- **PlantUML**: Text-based UML with cloud extensions, but complex setup for AWS icons.
- **Graphviz**: Graph-based, lacks cloud icons.
- **Suitability**: Low, not optimal for cloud architectures.

**Decision**: Diagrams chosen for initial implementation due to Python automation and cloud support. Draw.io and Mermaid.js explored as alternatives.

## Step 3: Sample Excel File
- **File**: `architecture.xlsx` with three sheets:
  - **Conceptual**: Business functions (e.g., Web Channel > Mobile Banking).
  - **Logical**: Technical modules (e.g., Web Channel > Adobe Experience Manager).
  - **Physical**: Cloud components (e.g., Web Channel > EC2 Cluster).
  - Columns: ComponentID, Function/Module/Component, SubFunction/SubModule/SubComponent, Status, Connections, Notes.
- **Status Colors**:
  - as-is/to be retained: Light blue
  - to be removed: Red
  - to be added/to be introduced: Green
  - to be updated/to be upgraded: Yellow

## Step 4: Diagrams Implementation
- **Script**: `generate_diagrams.py`
- **Features**:
  - Reads Excel using pandas.
  - Creates clusters for main components, nodes for subcomponents.
  - Uses AWS icons (EC2, S3, etc.) for Physical diagram.
  - Applies status colors via Graphviz attributes.
  - Outputs PNGs: `conceptual_architecture.png`, `logical_architecture.png`, `physical_architecture.png`.
- **Dependencies**: `diagrams`, `pandas`, `openpyxl`, Graphviz.
- **Pros**: Easy automation, native AWS icons.
- **Cons**: Requires Graphviz setup, static output.

## Step 5: Draw.io Implementation
- **Script**: `generate_drawio_diagrams.py`
- **Features**:
  - Generates XML files for Draw.io.
  - Creates swimlanes for main components, nodes for subcomponents.
  - Uses AWS19 shapes (e.g., `mxgraph.aws19.ec2_instance`) for Physical diagram.
  - Applies status colors via `fillColor`.
  - Outputs XMLs: `conceptual_architecture.xml`, `logical_architecture.xml`, `physical_architecture.xml`.
- **Dependencies**: `pandas`, `openpyxl`.
- **Pros**: AWS icons, interactive editing post-import.
- **Cons**: Complex XML, manual layout adjustments.

## Step 6: Mermaid.js Implementation
- **Script**: `generate_mermaid_diagrams.py`
- **Features**:
  - Generates Mermaid syntax (`.mmd`) using `architecture-beta`.
  - Creates subsystems for main components, nodes for subcomponents.
  - Uses Iconify AWS icons (e.g., `aws-ec2`) for Physical diagram.
  - Applies status colors via CSS `classDef`.
  - Outputs `.mmd` files: `conceptual_architecture.mmd`, `logical_architecture.mmd`, `physical_architecture.mmd`.
- **Dependencies**: `pandas`, `openpyxl`, Mermaid CLI.
- **Pros**: Text-based, Git-friendly.
- **Cons**: Limited AWS icons, beta syntax.

## Step 7: Comparative Analysis
| Criteria             | Diagrams                     | Draw.io                      | Mermaid.js                   |
|----------------------|------------------------------|------------------------------|------------------------------|
| **Ease of Automation** | High (Python)               | Moderate (XML)               | Moderate (Text)              |
| **Cloud Support**     | Strong (AWS/GCP/Azure)      | Strong (AWS libraries)      | Limited (Iconify)            |
| **Coloring**          | Graphviz attributes         | XML fillColor               | CSS classDef                 |
| **Output**            | PNG/SVG/PDF                 | PNG/SVG/XML                 | SVG/PNG (via CLI)            |
| **Suitability**       | High (automation, cloud)    | Moderate (flexibility)      | Moderate (simplicity)        |

**Recommendation**: Diagrams for automation and cloud support; Draw.io for flexibility; Mermaid.js for documentation.

## Step 8: Best Practices
- **Version Control**: Use Git for scripts and Excel.
- **Modular Code**: Separate Excel reading, diagram generation.
- **Error Handling**: Validate Excel structure, handle missing data.
- **Rendering**: Use Mermaid CLI or Draw.io for Mermaid; import XML for Draw.io.

## Step 9: Resources
- Diagrams: [mingrammer/diagrams](https://diagrams.mingrammer.com/)
- Draw.io: [diagrams.net](https://app.diagrams.net/)
- Mermaid.js: [mermaid-js.github.io](https://mermaid-js.github.io/)
- Pandas: [pandas.pydata.org](https://pandas.pydata.org/)
- Graphviz: [graphviz.org](https://graphviz.org/)

## Step 10: Next Steps
- Test scripts with `architecture.xlsx`.
- Refine layouts or add more AWS icons.
- Integrate into CI/CD for automated diagram updates.