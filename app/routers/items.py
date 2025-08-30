from fastapi import FastAPI

router = APIRouter()

@router.get("/items")
def list_items():
    
    return {"Showing a list of items": "Accounts endpoint placeholder"}

@router.post('/items')
def create_items(): 
    return {"Added list to items": "201"}

@router.put('/items/{id}')
def update_items():
    return {"Update Items": '201'}

@router.delete('/items/{id}')
def delete_items(): 
    return