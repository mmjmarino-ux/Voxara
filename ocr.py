try:
    import easyocr
    _reader = None

    def get_reader():
        global _reader
        if _reader is None:
            _reader = easyocr.Reader(['en'], gpu=False)
        return _reader

    def extract_text_from_image(image_path):
        try:
            reader = get_reader()
            results = reader.readtext(image_path, detail=0)
            return '\n'.join(results).strip() or 'No text detected in image.'
        except Exception as e:
            return f"OCR error: {str(e)}"

except ImportError:
    # Fallback: try pytesseract with auto-detected path
    try:
        import pytesseract
        from PIL import Image
        import shutil

        # Auto-detect tesseract — works on Linux/Mac/Windows
        tess = shutil.which('tesseract')
        if tess:
            pytesseract.pytesseract.tesseract_cmd = tess

        def extract_text_from_image(image_path):
            try:
                img = Image.open(image_path)
                text = pytesseract.image_to_string(img)
                return text.strip() or 'No text detected in image.'
            except Exception as e:
                return f"OCR error: {str(e)}"

    except ImportError:
        def extract_text_from_image(image_path):
            return ("OCR engine not installed. "
                    "Run: pip install easyocr\n"
                    "Or install Tesseract: https://github.com/tesseract-ocr/tesseract")