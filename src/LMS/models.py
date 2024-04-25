from pydantic import BaseModel

# Pydantic models...
class LMSBaseModel(BaseModel):
    class Config:
        orm_mode = True
        # validate_assignment = True
        # arbitrary_types_allowed = True
        # anystr_strip_whitespace = True

        # json_encoders = {
        #     # custom output conversion for datetime
        #     datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%SZ") if v else None,
        #     SecretStr: lambda v: v.get_secret_value() if v else None,
        # }