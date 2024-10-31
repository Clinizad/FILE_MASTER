# app/routers/pdf.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from typing import List
from services.pdf_services import PDFService
from io import BytesIO

router = APIRouter()

@router.post("/merge", response_class=StreamingResponse)
async def merge_pdfs(files: List[UploadFile] = File(...)):
    """ Recibe múltiples archivos PDF y los une en uno solo.
    
    Args:
        files (List[UploadFile]): Lista de archivos PDF cargados.
    
    Returns:
        StreamingResponse: Archivo PDF unido.
    """
    pdf_files = []
    
    for file in files:
        if file.content_type != "application/pdf":
            raise HTTPException(status_code=400, detail="Todos los archivos deben ser PDFs")
        
        # Leer archivo como BytesIO
        pdf_files.append(BytesIO(await file.read()))
    
    # Llamar al servicio para unir los PDFs
    merged_pdf = PDFService.merge_pdfs(pdf_files)
    
    return StreamingResponse(merged_pdf, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=merged.pdf"})
