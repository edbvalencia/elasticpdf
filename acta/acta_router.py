import os

from fastapi import APIRouter, File, HTTPException, UploadFile, status
from fastapi.responses import FileResponse

from acta.acta_model import Acta
from acta.acta_repository import save

router = APIRouter(
    prefix="/actas",
    tags=["Actas"],
    responses={404: {"detail": "No encontrado"}},
)


@router.get("/query/{query}", status_code=status.HTTP_200_OK, response_model=Acta)
async def get_related(query: str):
    try:
        print(query)
        return Acta(id=1, name="aula.pdf", autor="eduardo")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La query es maala",
        ) from e


pdf_directory = "pdf_files"

# Crear directorio si no existe
os.makedirs(pdf_directory, exist_ok=True)


@router.post("/uploadpdf/")
async def create_upload_file(file: UploadFile = File(...)):
    # Guardar el archivo en el directorio
    file_path = os.path.join(pdf_directory, file.filename)
    with open(file_path, "wb") as pdf_file:
        pdf_file.write(file.file.read())
    return {"filename": file.filename}


@router.get("/downloadpdf/{filename}")
async def download_pdf(filename: str):
    # Verificar si el archivo existe
    file_path = os.path.join(pdf_directory, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    # Devolver el archivo como respuesta
    return FileResponse(file_path, filename=filename)


@router.get("/gege")
async def gege():
    save()
    return "good"
