from sqlmodel import SQLModel,Field,Relationship

class VehicleBase(SQLModel):
   plates: str | None = Field(description="Vehicles plates")


class DestinationBase(SQLModel):
