from pypdf import PdfWriter, PdfReader
from typing import List
from io import BytesIO

class PDFService:
    @staticmethod
    def merge_pdfs(pdf_files: List[BytesIO]) -> BytesIO:
        """Une una lista de archivos PDF en un solo archivo PDF, optimizado para grandes volúmenes de páginas.
        
        Args:
            pdf_files (List[BytesIO]): Lista de archivos PDF en BytesIO.
        
        Returns:
            BytesIO: Un solo archivo PDF resultante de la unión.
        """
        writer = PdfWriter()
        
        # Procesar cada archivo PDF individualmente para ahorrar memoria
        for pdf_file in pdf_files:
            pdf_file.seek(0)  # Asegurarse de que estamos al inicio del archivo
            reader = PdfReader(pdf_file)
            
            # Añadir páginas individualmente para optimizar el uso de memoria
            for page in reader.pages:
                writer.add_page(page)
            
            # Cerrar el archivo una vez procesado (buena práctica con archivos grandes)
            pdf_file.close()

        # Generar el archivo de salida
        output = BytesIO()
        writer.write(output)
        output.seek(0)  # Reiniciar el puntero al inicio del archivo

        return output
