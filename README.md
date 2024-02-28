## Python MongoDB Backup & Restore
Python Library to Backup and Restore MongoDB

GitHub Repo: [https://github.com/sannjayy/py-mongo-backup-restore](https://github.com/sannjayy/py-mongo-backup-restore)
### Installaion
Do the following in your virtualenv:

`pip install py-mongo-backup-restore`

**Import:**
```
from py_mongo_backup_restore import PyMongoBackupRestore
```
---

### Configuration:
```python
from py_mongo_backup_restore import PyMongoBackupRestore

# Database Configuration:
config = {
    'protocol': 'mongodb',
    'host': '3.108.158.64:27017',
    'username': 'admin',
    'password': 'XXXXXXXXXXXXXXXX',
    'params': '?authSource=admin', # Optional
}

# (OR) Connection with URI
config = {
    'host_uri': '', # If MongoDB URI  (Optional)
    'params': '?authSource=admin', # Optional
}

# Creating Instance
mongo_handler = PyMongoBackupRestore(**config)
print('URI -> ', mongo_handler.get_uri()) # Returns the Mongo Host Uri
```


**To check if mongodump and mongorestore commands are working**

This script checks the version of mongodump and mongorestore commands using the --version flag. If the commands are working, it prints a success message; otherwise, it prints an error message.

```python
PyMongoBackupRestore(**config).check_mongodump_mongorestore()
```

---

### Backup Database:

```python
# Backup Full Database
mongo_handler.backup(
    database_name = "DATABASE_NAME", 
    backup_folder = "BACKUP_FOLDER", 
    compression="gzip" # (Optional)
)

# (OR) Backup a Collection
mongo_handler.backup(
    database_name = "DATABASE_NAME", 
    collection_name = "COLLECTION_NAME", 
    backup_folder = "BACKUP_FOLDER", 
    compression="gzip" # (Optional)
)
```

### Restore Database:

```python
# Restore Full Database
mongo_handler.restore(
    database_name = "DATABASE_NAME", # Target Database Name
    backup_folder = "BACKUP_FOLDER/BACKUP_NAME", 
)

# (OR) Restore a Collection
mongo_handler.restore_collection(
    database_name = "DATABASE_NAME", # Target Database Name
    collection_source = "BACKUP_FOLDER/BACKUP_NAME/file.bson", 
    collection_name = "COLLECTION_NAME", 
)
```

---

---

[![](https://img.shields.io/github/followers/sannjayy?style=social)](https://github.com/sannjayy)  
Developed by *Sanjay Sikdar*.   
- 📫 me@sanjaysikdar.dev



