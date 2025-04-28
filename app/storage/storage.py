from google.cloud import storage

class gcp_st:
    def __init__(self, destination, source_file):
        self.destination = destination
        self.source_file = source_file 
    
    def uploadtoGcs(self):
        storage_client = storage.Client()
        bucket = storage_client.bucket("image21241")
        blob = bucket.blob(self.destination)
        
        self.source_file.file.seek(0)
    
        blob.upload_from_file(self.source_file.file)
        
        return f'{self.source_file.filename} uploaded to {self.destination}'
        
    


