from google.appengine.ext import ndb

# Data model
class Post(ndb.Model):
  title = ndb.StringProperty()
  images = ndb.BlobKeyProperty(repeated=True)

class ImageInfo(ndb.Model):
  blob_key = ndb.BlobKeyProperty()
  post_key = ndb.KeyProperty()
