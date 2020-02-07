def findrc(rcn=".examplerc"):
     var_n = "EXAMPLERC_DIR"
     example_dir = os.environ.get(var_n)
     if example_dir:
        dir_path = pathlib.Path(example_dir)
        configp = dir_path / rcn
        print(f"Checking {configp}")
        if configp.exists():
             return configp.as_posix()

 # Check the current Working Directory
     configp = pathlib.Path.cwd() / rcn
     print(f"Checking {configp}")
     if configp.exists():
         return configp.as_posix()

 # Check User Home Dir
     file_path = os.path.abspath(__file__)
     parent_path = os.path.dirname(file_path)
     configp = os.path.join(parent_path, rcn)
     print(f"Checking {configp}")
     if os.path.exists(configp):
         return configp


         return configp
 # Check Dir of this File
     file_path = os.path.abspath(__file__)
     parent_path = os.path.dirname(file_path)
     configp = os.path.join(parent_path, rcn)
     print(f"Checking {configp}")
     if os.path.exists(configp):
         return configp

     print(f"File {rcn} has not been found")
