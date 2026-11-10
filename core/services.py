# fuction of upload document 
# used to generate thumbnail of pdf
# create pdf name folder where we will extract images of pdf
# provide total number of pages
import os
from db.repository import DocumentRepository
from datetime import datetime

PDF_STORAGE=os.path.join("storage","pdfs")


class DocumentService:
    def __init__(self):
        self.repo=DocumentRepository()
    def upload_document(self,upload_file,tags,description,lecture_date=None):
        doc={}
        # 1. save file and change pdf file name a bit by adding time stamp with name
        timestamp=datetime.now().strftime("%Y%m%d%H%M%S")
        file_name=f"{timestamp}_{upload_file.name}"
       
        # created a folder to store name of storage/pdfs
        file_path=os.path.join(PDF_STORAGE,file_name)
        with open(file_path,"wb")as f: # opening file path in file in write binary(wb)format
            f.write(upload_file.read())
        # 2.generate thumbnail
        # 3. get total pages
        # 4. convert to image
        # 5. create required variable:upload date
        # 6. save to DB
        #self.repo.add_document(doc)
        