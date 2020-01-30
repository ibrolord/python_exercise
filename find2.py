def findrc(rcn=".examplerc"):
     var_n = "EXAMPLERC_DIR"
     if var_n in os.environ:
         var_p = os.path.join(f"${var_name}", rcn)
         configp = os.path.expandvars(var_p)
         print(f"Checking {configp}")
         if os.path.exists(configp):
             return configp
 # Check the current Working Directory
     configp = os.path.join(os.getcwd(), )


     print(f"Checking {configp}")
     if os.path.exists(configp):
         return configp
 # Check Dir of this File
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
