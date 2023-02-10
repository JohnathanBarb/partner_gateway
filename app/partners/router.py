from fastapi import APIRouter

from .schemas import PartnerSchema

partner_router = APIRouter(
    prefix="/partners",
    tags=["partners"],
)


@partner_router.post("/")
def create_partner(partner: PartnerSchema):
    return {"partner": partner}
