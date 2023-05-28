from pydantic import BaseModel, validator


class UsernameValidator(BaseModel):
    username: str

    @validator('username')
    def username_alphanumeric(cls, v: str) -> str:
        if v.isdigit():
            raise ValueError('Must be alphanumeric')
        return v


