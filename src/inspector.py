import os
import importlib.util
import inspect

def list_src_folder_contents():
    # 1. Target the 'src' folder specifically
    # This finds the absolute path to your 'src' directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(current_dir, 'src')
    
    # If you are already running this from inside 'src', use this instead:
    if not os.path.exists(src_path):
        src_path = current_dir

    files = [f for f in os.listdir(src_path) if f.endswith('.py') and f != os.path.basename(__file__)]

    print(f"🔍 Scanning folder: {src_path}\n")

    for file_name in files:
        module_name = file_name[:-3]
        print(f"--- File: {file_name} ---")
        
        try:
            # 2. Load the module from the src path
            spec = importlib.util.spec_from_file_location(module_name, os.path.join(src_path, file_name))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # 3. Filter for your variables and functions
            names = [name for name in dir(module) if not name.startswith("__")]
            
            for name in names:
                obj = getattr(module, name)
                if inspect.isfunction(obj):
                    print(f"  [Function]  {name}()")
                elif not inspect.ismodule(obj): # Skip imported libraries like 'cv2'
                    print(f"  [Variable]  {name}")
            print("\n")
            
        except Exception as e:
            print(f"  ❌ Skip/Error: {file_name}\n")

if __name__ == "__main__":
    list_src_folder_contents()