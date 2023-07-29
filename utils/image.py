from pydantic import BaseModel, Field, validator
from typing import Optional, Literal, List
from configs.app_config import allowed_camera_types, allowed_locs
from configs.app_config import min_dpi, mutually_exclusive_labels


class ImageData(BaseModel):

    url: str
    domain: Optional[str] = Field(None)
    camera_type: Optional[Literal[allowed_camera_types]] = Field(None)
    location: Optional[Literal[allowed_locs]] = Field(None)
    dpi: int = Field(ge=min_dpi, description="dpi cannot be lower than 50")
    label: Optional[List[str]] = Field(None)

    @validator("label")
    def check_label(cls, v, values, **kwargs):
        if v is not None:
            for exclusive_pair in mutually_exclusive_labels:
                if set(exclusive_pair).issubset(set(v)):
                    raise ValueError(f'Image cannot have these labels combination {exclusive_pair} ')
        return v
