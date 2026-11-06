# fuction of upload document 
# used to generate thumbnail of pdf
# create pdf name folder where we will extract images of pdf
# provide total number of pages

from db.repository import DocumentRepository



class DocumentService:
    def __init__(self):
        self.repo=DocumentRepository()
    def upload_document(self,upload_file,tags,description,lecture_date=None):
        # 1. save file
        # 2.generate thumbnail
        # 3. get total pages
        # 4. convert to image
        # 5. create required variable:upload date
        # 6. save to DB