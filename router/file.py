from fastapi import APIRouter, File, UploadFile
import shutil

from fastapi.responses import FileResponse

router = APIRouter(
    prefix='/file',
    tags=['files']
)


@router.post('/file')
def get_file(files: bytes = File(...)):
    content = files.decode('utf-8')
    lines = content.split('\n')
    return {'lines': lines}


@router.post('/upload_file')
def get_upload_file(up_file: UploadFile = File(...)):
    path = f"files/{up_file.filename}"
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(up_file.file, buffer)

    return {
        'filename': up_file.filename,
        'type': up_file.content_type
    }

@router.get('/downloads/{name}', response_class = FileResponse)

def download_file(name: str):
    path = f'files/{name}'
    return path