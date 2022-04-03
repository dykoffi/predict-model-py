from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    person_age: float
    person_income: float
    person_emp_length: float
    loan_amnt: float
    loan_int_rate: float
    loan_percent_income: float
    cb_person_cred_hist_length: float
    loan_status: float
    person_home_ownership_MORTGAGE: float
    person_home_ownership_OTHER: float
    person_home_ownership_OWN: float
    person_home_ownership_RENT: float
    loan_intent_DEBTCONSOLIDATION: float
    loan_intent_EDUCATION: float
    loan_intent_HOMEIMPROVEMENT: float
    loan_intent_MEDICAL: float
    loan_intent_PERSONAL: float
    loan_intent_VENTURE: float
    loan_grade_A: float
    loan_grade_B: float
    loan_grade_C: float
    loan_grade_D: float
    loan_grade_E: float
    loan_grade_F: float
    loan_grade_G: float

