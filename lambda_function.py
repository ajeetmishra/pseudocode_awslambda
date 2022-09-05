def handler_cv():
    """Psuedo code for opencv"""

    import cv2
    img0 = cv2.imread("sample_img.jpg")
    return {"image_shape" : img0.shape}


def handler_pdf():
    """Psuedo code for poppler"""

    import pdf2image
    pages = pdf2image.convert_from_path('sample_pdf.pdf')

    # Decide a temporary filename
    import tempfile
    img_fname = tempfile.NamedTemporaryFile().name
    
    # Split pdf and save as images
    pdfPages = []
    for k, page in enumerate(pages):
        jpeg_file = f"{img_fname}---{k:0>4}.jpg"

        # Save each page to disk
        page.save(jpeg_file,'JPEG')
        pdfPages.append(jpeg_file)
    
    return {"count_pages" : len(pages)}


def main(event, lambda_context):
    """Combined code"""
    res1 = handler_cv()
    res2 = handler_pdf()
    return {**res1, **res2}


def main2(event, lambda_context):
    """Test code"""
    return {"hello":"world"}


if __name__ == '__main__':
    output = main(None, None)
    print(output)