import subprocess
from urllib.parse import quote_plus, urlparse, parse_qs, urlencode

class PyMongoBackupRestore:
    
    def __init__(self, **kwargs) -> None:

        self.CONNECTION_STRING = kwargs.get('connection_string', None)
        if self.CONNECTION_STRING:
            # Parse the connection string
            parsed_url = urlparse(self.CONNECTION_STRING)
            self.SCHEME = parsed_url.scheme
            self.USERNAME = parsed_url.username
            self.PASSWORD = parsed_url.password
            self.HOST = parsed_url.hostname
            self.EXTRA_OPTIONS  = urlencode({key: val[0] for key, val in parse_qs(parsed_url.query).items()})
            self.DATABASE = parsed_url.path.strip('/') or None
        else:
            self.SCHEME = kwargs.get('scheme', 'mongodb')
            self.USERNAME = kwargs.get('username', '')
            self.PASSWORD = kwargs.get('password', '')
            self.HOST = kwargs.get('host')
            self.EXTRA_OPTIONS  = kwargs.get('extra_options', '')
            self.DATABASE = kwargs.get('database_name', None)
            
        self.MONGO_URI = f"{self.SCHEME}://{quote_plus(self.USERNAME)}:{quote_plus(self.PASSWORD)}@{self.HOST}/{self.EXTRA_OPTIONS}"
            
    def get_uri(self):
        if self.DATABASE:
            return f"{self.SCHEME}://{quote_plus(self.USERNAME)}:{quote_plus(self.PASSWORD)}@{self.HOST}/{self.DATABASE}?{self.EXTRA_OPTIONS}"
        return self.MONGO_URI
    
    
    def backup(self, *args, **kwargs):
        database_name = self.DATABASE or kwargs.get('database_name')
        backup_folder = kwargs.get('backup_folder')
        compression = kwargs.get('compression', 'default')
        collection_name = kwargs.get('collection_name', None)
        
        # Use mongodump command to backup the database
        backup_cmd = [
            "mongodump",
            "--uri", self.get_uri(),
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
            print(f"Backup of {database_name}.{backup_cmd} failed. Error: {e}")
        
    
    def backup_collection(self, *args, **kwargs):
        database_name = self.DATABASE or kwargs.get('database_name')
        backup_folder = kwargs.get('backup_folder')
        compression = kwargs.get('compression', 'default')
        collection_name = kwargs.get('collection_name', None)
        
        # Use mongodump command to backup the database
        backup_cmd = [
            "mongodump",
            "--uri", self.get_uri(),
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
    
    def restore(self, *args, **kwargs):
        database_name = self.DATABASE or kwargs.get('database_name')
        backup_folder = kwargs.get('backup_folder')
        
        restore_cmd = [
            "mongorestore",
            "--uri", self.get_uri(),
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
            
    def restore_collection(self, *args, **kwargs):
        database_name = self.DATABASE or kwargs.get('database_name')  
        collection_name = kwargs.get('collection_name', None)
        collection_source = kwargs.get('collection_source', None)
        
        restore_cmd = [
            "mongorestore",
            "--uri", self.get_uri(),
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
  