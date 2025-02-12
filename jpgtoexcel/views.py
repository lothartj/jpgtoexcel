from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import easyocr
import pandas as pd
import io
import tempfile
import numpy as np

@csrf_exempt
def jpgtoexcel(request):
    if request.method == 'POST':
        try:
            # Get the uploaded image
            image_file = request.FILES['image']
            
            # Create a temporary file to save the image
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                for chunk in image_file.chunks():
                    tmp.write(chunk)
                tmp_path = tmp.name

            # Initialize the OCR reader
            reader = easyocr.Reader(['en'])
            
            # Read text from image with bounding boxes
            results = reader.readtext(tmp_path)
            
            # Sort results by vertical position (y-coordinate) first
            # Then by horizontal position (x-coordinate)
            sorted_results = sorted(results, key=lambda x: (x[0][0][1], x[0][0][0]))
            
            # Group results into rows based on similar y-coordinates
            rows = []
            current_row = []
            last_y = None
            y_threshold = 10  # Adjust this value based on your image

            for result in sorted_results:
                y_coord = result[0][0][1]  # Get y-coordinate of top-left corner
                
                if last_y is None:
                    current_row.append(result[1])
                elif abs(y_coord - last_y) > y_threshold:
                    # New row
                    if current_row:
                        rows.append(current_row)
                    current_row = [result[1]]
                else:
                    # Same row
                    current_row.append(result[1])
                
                last_y = y_coord
            
            # Add the last row
            if current_row:
                rows.append(current_row)
            
            # Create DataFrame
            df = pd.DataFrame(rows)
            
            # If first row contains headers, use it as column names
            if len(df) > 0:
                df.columns = [f'Column_{i+1}' for i in range(len(df.columns))]
            
            # Create Excel file in memory
            excel_file = io.BytesIO()
            df.to_excel(excel_file, index=False, engine='openpyxl')
            excel_file.seek(0)
            
            # Return the Excel file as response
            response = HttpResponse(excel_file.read(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = 'attachment; filename=extracted_text.xlsx'
            return response
            
        except Exception as e:
            return HttpResponse(str(e), status=500)
    
    return render(request, 'index.html')