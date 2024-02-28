import subprocess
from urllib.parse import quote_plus

class PyMongoBackupRestore:
    
    def __init__(self, **kwargs) -> None:
        self.MONGO_USERNAME = quote_plus(kwargs.get('username'))
        self.MONGO_PASSWORD = quote_plus(kwargs.get('password'))
        self.HOST = kwargs.get('host')
        self.PARAMS = kwargs.get('params', '')
        _host_uri = kwargs.get('host_uri', None)
        self.MONGO_HOST_URI = _host_uri or f"{kwargs.get('protocol', 'mongodb')}://{self.MONGO_USERNAME}:{self.MONGO_PASSWORD}@{self.HOST}/{self.PARAMS}"
            
    def get_uri(self):
        return self.MONGO_HOST_URI
    
    
    def backup(self, *args, **kwargs):
        database_name = kwargs.get('database_name')
        backup_folder = kwargs.get('backup_folder')
        compression = kwargs.get('compression', 'default')
        collection_name = kwargs.get('collection_name', None)
        
        # Use mongodump command to backup the database
        backup_cmd = [
            "mongodump",
            "--uri", self.MONGO_HOST_URI,
            "--db", database_name,
            # "--gzip",  # Add --gzip option for compression
            "--out", backup_folder
        ]
        
        if compression == 'gzip':
            backup_cmd.append("--gzip")
        
        if collection_name:
            backup_cmd.append("--collection")
            backup_cmd.append(collection_name)
        
        try:
            result = subprocess.run(backup_cmd, check=True, capture_output=True, text=True)
            print(f"Backup completed successfully. Check {backup_folder} for the {database_name} backup files.")
            print(result.stdout)
            
        except subprocess.CalledProcessError as e:
            print(f"Restore of {database_name}.{backup_cmd} failed. Error: {e}")
            print("Output:")
            print(e.output)
        
    
    def backup_collection(self, *args, **kwargs):
        database_name = kwargs.get('database_name')
        backup_folder = kwargs.get('backup_folder')
        compression = kwargs.get('compression', 'default')
        collection_name = kwargs.get('collection_name', None)
        
        # Use mongodump command to backup the database
        backup_cmd = [
            "mongodump",
            "--uri", self.MONGO_HOST_URI,
            "--db", database_name,
            "--collection", collection_name,
            # "--gzip",  # Add --gzip option for compression
            "--out", backup_folder
        ]
        
        if compression == 'gzip':
            backup_cmd.append("--gzip")
        
        try:
            result = subprocess.run(backup_cmd, check=True, capture_output=True, text=True)
            print(f"Backup completed successfully. Check {backup_folder} for the {database_name} backup files.")
            print(result.stdout)
            
        except subprocess.CalledProcessError as e:
            print(f"Restore of {database_name}.{backup_cmd} failed. Error: {e}")
            print("Output:")
            print(e.output)
    
    def restore(self, *args, **kwargs):
        database_name = kwargs.get('database_name')
        backup_folder = kwargs.get('backup_folder')
        
        restore_cmd = [
            "mongorestore",
            "--uri", self.MONGO_HOST_URI,
            "--db", database_name,
            backup_folder
        ]
            
        # subprocess.run(restore_cmd, check=True)
        try:
            result = subprocess.run(restore_cmd, check=True, capture_output=True, text=True)
            print(f"Restore of {database_name} completed successfully.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Restore of {database_name} failed. Error: {e}")
            print("Output:")
            print(e.output)
            
    def restore_collection(self, *args, **kwargs):
        database_name = kwargs.get('database_name')       
        collection_name = kwargs.get('collection_name', None)
        collection_source = kwargs.get('collection_source', None)
        
        restore_cmd = [
            "mongorestore",
            "--uri", self.MONGO_HOST_URI,
            "--db", database_name,
            "--collection", collection_name,
            collection_source
        ]
            
        # subprocess.run(restore_cmd, check=True)
        try:
            result = subprocess.run(restore_cmd, check=True, capture_output=True, text=True)
            print(f"Restore of {database_name}.{collection_name} completed successfully.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Restore of {database_name}.{collection_name} failed. Error: {e}")
            print("Output:")
            print(e.output)
        
    def check_mongodump_mongorestore(self, info=False):
        try:
            # Check mongodump command
            print("------------------------------------------")
            subprocess.run(["mongodump", "--version"], check=True)
            print("------------------------------------------")
            # Check mongorestore command
            subprocess.run(["mongorestore", "--version"], check=True)
            print("------------------------------------------")
            print("mongodump and mongorestore commands are working.")
            print("------------------------------------------")

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            print("------------------------------------------")
            print("mongodump and/or mongorestore commands encountered an error.")
  