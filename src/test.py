from py_mongo_backup_restore import PyMongoBackupRestore


# Example Usage
config = {
    'protocol': 'mongodb',
    'host': '3.108.158.64:27017',
    'username': 'admin',
    'password': 'XXXXXXXXXXXXXXXX',
    'params': '?authSource=admin', # Optional
}

PyMongoBackupRestore(**config).check_mongodump_mongorestore()

# mongo_handler = PyMongoBackupRestore(**config)
# print('URI -> ', mongo_handler.get_uri())

# Backup Database
# mongo_handler.backup(
#     database_name = "location_database_test", 
#     backup_folder = "backup_folder/newzip", 
#     compression="gzip" # --gzip option for compression
# )

# mongo_handler.backup(
#     database_name = "location_database_new1", 
#     collection_name = "location_data", 
#     backup_folder = "backup_folder/sanjay", 
#     compression="gzip" # --gzip option for compression
# )

# Restore Database

# mongo_handler.restore(
#     database_name = "location_database_new1", # Target Database Name
#     backup_folder = "backup_folder/newzip/location_database_test/sanjay.bson", 
# )
# mongo_handler.restore_collection(
#     database_name = "location_database_new1", # Target Database Name
#     collection_source = "backup_folder/newzip/location_database_test/sanjay.bson", 
#     collection_name = "sanjay", 
# )