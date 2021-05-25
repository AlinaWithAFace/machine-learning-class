# Group Problem (35pt)

In this homework you will implement k-means for image segmentation.

* **Step 1.** Take **three** photos. Do not use very large photos. You may use the PNG and JPEG
format. For each photo,
    * Load your photo into computer and get the pixels each of which is given by (R,G,B).
Use the libraries for processing image.
    * Apply K-means to the pixels, and rewrite the image where each pixel is replaced by
the mean of its cluster. Now you have a new photo.
    * Try different k from {1, 2, 5, 10, 20}. Now you have many new photos.
* **Step 2.** Questions:
    * What did you find concerning the relationship between k and the size of the new
image?
    * For each of your photos, which k is the best you think? Why?
* Step 3. Take a new photo of which you believe k=2 is the best, and verify it use your program in step 1.

### What to Turn in
Please upload.
* Your **code and a Readme file** for compiling the code.
* Your original **photos** and produced photos.
* A pdf **report** of (a) your results in step 1, (b) your answers to step 2, and (c) your findings
in step 3. You should also show your photos in your report.