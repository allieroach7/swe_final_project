from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import resources as model
from sqlalchemy.exc import SQLAlchemyError