from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any
from uuid import UUID
from enum import Enum

class ObjectType(str, Enum):
    SPHERE = "sphere"
    BOX = "box"
    CYLINDER = "cylinder"

class Geometry(BaseModel):
    model_config = {"extra":"forbid"}

class Cube(Geometry):
    type:str = "cube"
    center: List[float] = Field(..., ge=3, le=3)
    size: List[float] = Field(..., ge=3, le=3)
    forces: Optional[List[float]] = Field([0.0, 0.0, 0.0], ge=3, le=3)

class Sphere(Geometry):
    type:str = "sphere"
    center: List[float] = Field(..., ge=3, le=3)
    radius: float = Field(..., gt=0)
    forces: Optional[List[float]] = Field([0.0, 0.0, 0.0], ge=3, le=3)

class Cylinder(Geometry):
    type:str = "cylinder"
    center: List[float] = Field(..., ge=3, le=3)
    radius: float = Field(..., gt=0)
    height: float = Field(..., gt=0)
    axis: int = Field(..., ge=0, lt=3)
    forces: Optional[List[float]] = Field([0.0, 0.0, 0.0], ge=3, le=3)

class OptimizationParams(BaseModel):
    model_config = {"extra":"forbid"}
    nelx: int = Field(..., ge=5, le=200)
    nely: int = Field(..., ge=5, le=200)
    nelz: int = Field(..., ge=5, le=200)
    volfrac: float = Field(..., ge=0.0, le=1.0)
    penal: float = Field(..., ge=1.0, le=5.0)
    rmin: float = Field(..., ge=0.5, le=10.0)
    tolx: float = Field(..., ge=0.001, le=0.999)
    maxloop: int = Field(..., ge=1, le=2000)
    pitch: Optional[float] = Field(1.0, ge=0.01, le=1.0)
    invert_design_space: Optional[bool] = Field(False)
    design_space_stl_id: Optional[UUID] = None
    obstacles: Optional[List[Geometry]] = Field(None, max_items=10)
    supports: Optional[List[Geometry]] = Field(None, max_items=10)
    forces: Optional[List[Geometry]] = Field(None, max_items=10)