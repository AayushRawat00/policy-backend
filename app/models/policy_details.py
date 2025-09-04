from enum import IntEnum
from pydantic import BaseModel


class Gender(IntEnum):
    M = 1
    F = 2
    O = 3


class PremiumFrequency(IntEnum):
    YEARLY = 1
    HALF_YEARLY = 2
    MONTHLY = 3


class PolicyDetails(BaseModel):
    date_of_birth: str
    gender: Gender = Gender.M
    sum_assured: int
    model_premium: int
    premium_frequency: PremiumFrequency = PremiumFrequency.YEARLY
    policy_term: int
    premium_policy_term: int
