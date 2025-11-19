from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..controllers import resources as resource_ctrl
from ..schemas.resources import Resource, ResourceCreate, ResourceUpdate
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/resources",
    tags=["resources"]
)

@router.post("/", response_model=Resource)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    return resource_ctrl.create(db, resource)

@router.get("/", response_model=List[Resource])
def read_resources(db: Session = Depends(get_db)):
    return resource_ctrl.read_all(db)

@router.get("/{resource_id}", response_model=Resource)
def read_resource(resource_id: int, db: Session = Depends(get_db)):
    return resource_ctrl.read_one(db, resource_id)

@router.put("/{resource_id}", response_model=Resource)
def update_resource(resource_id: int, resource: ResourceUpdate, db: Session = Depends(get_db)):
    return resource_ctrl.update(db, resource_id, resource)

@router.delete("/{resource_id}")
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return resource_ctrl.delete(db, resource_id)
