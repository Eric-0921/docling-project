
import json
from pathlib import Path
from docling_core.types.doc import DoclingDocument, TableItem

path = Path("output/demo_scpi/demo_remote_control.json")
with open(path) as f:
    data = json.load(f)

doc = DoclingDocument.model_validate(data)

print(f"Total tables: {len(doc.tables)}")
if doc.tables:
    table = doc.tables[0]
    print(f"Table Type: {type(table)}")
    print(f"Table Keys: {table.__dict__.keys()}")
    
    # Check for export methods
    if hasattr(table, 'export_to_markdown'):
        print("Has export_to_markdown")
        print(table.export_to_markdown())
    else:
        print("No export_to_markdown method found.")
