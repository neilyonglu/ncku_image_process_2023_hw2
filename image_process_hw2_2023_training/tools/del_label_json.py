import os
import json

src_folder = 'demo_test9' # 原始資料夾路徑
dest_folder = 'test_json' # 輸出資料夾路徑

for root, dirs, files in os.walk(src_folder):
  for filename in files:
    if not filename.endswith('.json'):
      continue  
      
    file_path = os.path.join(root, filename)
    
    with open(file_path) as f:
      data = json.load(f)
      
    shapes = data['shapes']
    data['shapes'] = [shape for shape in shapes if shape['label'] not in ['mix', 'cancer', 'warthin']]

    relative_path = os.path.relpath(file_path, src_folder)
    output_dir = os.path.join(dest_folder, os.path.dirname(relative_path))
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, filename)
    with open(output_path, 'w') as f:
      json.dump(data, f)