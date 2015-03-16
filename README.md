# Image Uploads with Google App Engine

This experiment implements an image uploader on Google App Engine. Given a Post kind, a number of image files can be uploaded to the blobstore and references its respective Post entity.

### Models
``` python
class Post(ndb.Model):
  title = ndb.StringProperty()
  images = ndb.BlobKeyProperty(repeated=True)

class ImageInfo(ndb.Model):
  blob_key = ndb.BlobKeyProperty()
  post_key = ndb.KeyProperty()
```

### Workflow
The Post and ImageInfo entitie are created separately.

1. Create Post entity using `/new-post`.
2. We are redirected to `/post/<post_id>`, on which we will find the 'upload image' link (new-image/<post_id>).
3. On the image upload page (new-image.html), we print a file upload form which includes:
  - the blobstore generated upload_url
  - enctype="multipart/form-data"
  - hidden input with the value of the current post's id.
4. The upload_url is created using `upload_url = blobstore.create_upload_url('/image-upload/%s' % post_id)`. Thus, the uploaded file is handled by the /image-upload path (and ImageUploadHandler).
5. The ImageUploadHandler(blobstore_handlers.BlobstoreUploadHandler) takes the uploaded file's BlobInfo and uses this to create an ImageInfo entity.
6. Now we can query for ImageInfo entities that has its `post_key == post.key` to find all entities associated with a certain post.
7. Because we are returning ImageInfo entities in the above query, we need to call image.get_serving_url(image_info.blob_key) on each ImageInfo to return a list of image urls.
8. Finally, this list of urls is passed to the template, where we will loop them into the src of the <img> tag.