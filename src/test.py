from py_mongo_backup_restore import PyMongoBackupRestore


# Example Usage
config = {
    'scheme': 'mongodb',
    'host': '37.108.158.64:27017',
    'username': 'username',
    'password': 'password',
    'extra_options': '?authSource=admin', # Optional
    'database_name': 'testDatabase', # Optional
}
# config = {
#     'connection_string': 'mongodb+srv://username:password@host.gp2xb.mongodb.net/database?retryWrites=true&w=majority'
# }

# PyMongoBackupRestore(**config).check_mongodump_mongorestore()

mongo_handler = PyMongoBackupRestore(**config)
print('URI -> ', mongo_handler.get_uri())

# Backup Database
mongo_handler.backup(
    # database_name = "testDatabase",  # Optional
    backup_folder = "backup_folder/TestDatabase", 
    compression="gzip" # --gzip option for compression
)

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