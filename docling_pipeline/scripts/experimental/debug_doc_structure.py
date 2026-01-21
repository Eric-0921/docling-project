
import json
from pathlib import Path
from docling_core.types.doc import DoclingDocument

path = Path("output/demo_scpi/demo_remote_control.json")
with open(path) as f:
    data = json.load(f)

doc = DoclingDocument.model_validate(data)

print(f"Body type: {type(doc.body)}")
print(f"Children count: {len(doc.body.children)}")
if doc.body.children:
    first_child = doc.body.children[0]
    print(f"First child type: {type(first_child)}")
    print(f"First child repr: {first_child}")
    
    # Check if we can access text directly
    if hasattr(first_child, 'text'):
        print(f"Text: {first_child.text}")
    elif hasattr(first_child, 'data'):
        print(f"Ref Data: {first_child.data}")
