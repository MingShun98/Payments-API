from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_transactions():
    return {"message": "Transactions endpoint placeholder"}
