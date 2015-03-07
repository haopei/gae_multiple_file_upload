# Uploading Multiple Images using Google App Engine

## Approach: create Post then images
- Let the user create the Post entity first (without images)
- Then, on the post/edit page, allow users to add images
- These images would contain the post_id as reference
- query for all images where their post_id == to the post being viewed
- output the images there

## todo
- each Post entity should contain a list of blob keys which reference the images of that post.

## Rubric
1. Must be able to select several images at once for uploading; instead of selecting and uploading one image at a time.
2. The completion of upload of each image must be seen
3. Can delete image, after an alert verification prompt.

## Steps / Method
- Define model to include blobstore property
- Create the stand alone upload widget specified by the doc
- Implement multi upload

## Setup requirements
- from google.appengine.ext import blobstore
- from google.appengine.ext.webapp import blobstore_handlers
- set encrypt="multipart/form-data"


## Clues
- Generates a new upload-url whenever a current image has been uploaded
- Uses ajax to upload each photo
- the upload_url must be generated and passed to the form's action parameter
- You must serve the form's page with a Content-Type of text/html; charset=utf-8, or any filenames with non-ASCII characters will be misinterpreted.


## Basic upload process
- When the user submits, the POST is handled by the Blobstore API, which creates the blob. The API also creates the blob's 'info record' to be stored in the datastore.
- Set up an upload handler. In this handler, you can store the blob key with the application's data model.
- The blob key is accessible from the info-record in the datastore
- When the Blobstore rewrites the user request, the MIME part of the uploaded files have their bodies emptied. The blob key is added as a MIME part header. All other form fields and parts are preserved.
- If a content-type is not specified, the Blobstore will infer this from the file extension. If no content type can be determined, the blob is assigned a content type of 'application/octet-stream'

## Serving blobs
- If serving images, use the get_serving_url instead of send_blob. The get_serving_url lets you serve the image directly instead of going through your app engine instances.

## The BlobInfo() object
- Every blobstore value has a corresponding read-only BlobInfo entity inside the datastore which contains information about the blob.
- You can retrieve BlobInfo objects using a Blobstore key.
- When a blob is uploaded, the blobstore automatically creates this BlobInfo entity

## Images Service
- The images service returns a transformed image to the app, and must be less than 32MB.
- Can resize, transform, rotate, flip and crop images.
- can convert image formats
- can composite multiple images into one image.
- can accept image data directly from the app, the blobstore or Google Cloud Storage
- can accept jpeg, png, webp gif, bmp, tiff and ico. Can return jpeg, webp and png. The image service converts the input format into the output format before transformation.

- use images.get_serving_url(blob_key) to retrieve the url of the image. You can pass in a BlobInfo object, a BlobKey object, or a string representation of the blob key

## Code

- blobstore.BlobInfo.get(blob_key) returns a BlobInfo object of the corresponding key
- use blob_info.key() to get the blob key from a BlobInfo object
- images.get_serving_url(<blob_info object or blob key string or blob key object)

