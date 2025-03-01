# JPG to Excel Converter

A Django web application that converts JPG images containing tabular data into Excel spreadsheets using OCR (Optical Character Recognition).

## Features

- Drag and drop interface for image upload
- OCR processing using EasyOCR
- Automatic table structure detection
- Excel file generation
- Modern, responsive UI

## Installation

### Using Docker

1. Clone the repository:
```bash
git clone https://github.com/lothartj/jpgtoexcel.git
cd jpgtoexcel
```

2. Build and run with Docker:
```bash
docker build -t jpgtoexcel .
docker run -p 8000:8000 jpgtoexcel
```

3. Visit http://localhost:8000 in your browser

### Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/lothartj/jpgtoexcel.git
cd jpgtoexcel
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python manage.py runserver
```

4. Visit http://localhost:8000 in your browser

## Usage

1. Open the web interface
2. Drag and drop an image containing tabular data (or click to select)
3. Wait for the OCR processing to complete
4. Download the generated Excel file

## Requirements

- Python 3.9+
- Django 4.2+
- EasyOCR
- Pandas
- OpenPyXL
- PyTorch

## License

MIT License

## Author

Contributions are welcome! Please feel free to submit a Pull Request.
Contributions are welcome! Please feel free to submit a Pull Request.

lothartj