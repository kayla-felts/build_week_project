"""Machine learning functions"""

import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    property_type: str = Field(..., example='Apartment')
    room_type: str = Field(..., example='Entire home/apt')
    bed_type: str = Field(..., example='Real Bed')
    cancellation_policy: str = Field(..., example='Strict')
    city: str = Field(..., example='NYC')
    host_identity_verified: bool = Field(..., example='True')
    instant_bookable: bool = Field(..., example='True')
    neighbourhood: str = Field(..., example='Brooklyn Heights')
    zipcode: int = Field(..., example=11201)
    amenities: int = Field(..., example=8)
    accommodates: int = Field(..., example=5)
    bathrooms: float = Field(..., example=1.5)
    bedrooms: int = Field(..., example=2)
    beds: int = Field(..., example=1)
    host_since_days: int = Field(..., example=365)


    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('x1')
    def x1_must_be_positive(cls, value):
        """Validate that amenities is a positive number."""
        assert value > 0, f'amenities == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(item: Item):
    """
    Make random baseline predictions for classification problem
    """
    X_new = item.to_df()
    log.info(X_new)
    y_pred = random.choice([True, False])
    y_pred_proba = random.random() / 2 + 0.5
    return {
        'prediction': y_pred,
        'probability': y_pred_proba
    }