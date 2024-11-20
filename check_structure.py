# # check_structure.py

# import os
# import sys
# from pathlib import Path

# def check_project_structure():
#     current_dir = Path.cwd()
    
#     # Required files and directories
#     required_structure = {
#         'app': {
#             'type': 'directory',
#             'children': {
#                 '__init__.py': 'file',
#                 'main.py': 'file'
#             }
#         },
#         'requirements.txt': 'file',
#         'render.yaml': 'file',
#         'Dockerfile': 'file'
#     }
    
#     issues = []
    
#     # Check each required item
#     for item_name, item_type in required_structure.items():
#         item_path = current_dir / item_name
        
#         if isinstance(item_type, dict) and item_type['type'] == 'directory':
#             if not item_path.is_dir():
#                 issues.append(f"❌ Missing directory: {item_name}")
#             else:
#                 print(f"✅ Found directory: {item_name}")
#                 # Check children
#                 for child_name, child_type in item_type['children'].items():
#                     child_path = item_path / child_name
#                     if not child_path.exists():
#                         issues.append(f"❌ Missing file: {item_name}/{child_name}")
#                     else:
#                         print(f"✅ Found file: {item_name}/{child_name}")
#         else:
#             if not item_path.exists():
#                 issues.append(f"❌ Missing file: {item_name}")
#             else:
#                 print(f"✅ Found file: {item_name}")
    
#     # Print issues if any
#     if issues:
#         print("\n🚨 Issues found:")
#         for issue in issues:
#             print(issue)
#         print("\nPlease create the missing files/directories to fix these issues.")
#     else:
#         print("\n✨ All required files and directories are present!")
        
#     # Check main.py location
#     main_files = list(current_dir.rglob("main.py"))
#     if main_files:
#         print("\n📍 Found main.py in these locations:")
#         for main_file in main_files:
#             print(f"   {main_file.relative_to(current_dir)}")
#     else:
#         print("\n❌ No main.py file found in the project!")

# if __name__ == "__main__":
#     check_project_structure()