from typing import List, Optional
from ..models import BeneficiaryPayouts, BeneficiaryPayoutsCreate, BeneficiaryPayoutsUpdate
from ..client_base import ClientBase

class BeneficiaryPayoutsService(ClientBase):
    """beneficiary_payouts API service"""
    
    
    def list(self, **params) -> List[BeneficiaryPayouts]:
        """List beneficiary_payouts"""
        return self._request("GET", "/beneficiary-payouts", model=BeneficiaryPayouts, params=params)
    
    
    def get(self, id: str) -> BeneficiaryPayouts:
        """Get a single beneficiary_payout"""
        return self._request("GET", f"/beneficiary-payouts/{id}", model=BeneficiaryPayouts)
    
    
    def create(self, data: BeneficiaryPayoutsCreate) -> BeneficiaryPayouts:
        """Create a new beneficiary_payout"""
        return self._request("POST", "/beneficiary-payouts", model=BeneficiaryPayouts, data=data)
    
    
    
