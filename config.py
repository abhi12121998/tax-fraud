import os
class config:
    MONGODB_SETTINGS = {
        'db' : "Taxdata",
        #'host': 'mongodb+srv://abhishek:abhishek@taxdata.6vg7w.mongodb.net/Taxdata?retryWrites=true&w=majority'
        'host': os.environ["MONGODB_URI"]
    }
