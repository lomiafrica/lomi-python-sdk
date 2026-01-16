from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class BeneficiaryPayouts(BaseModel):
    """Beneficiary payouts - track individual payout transfers model"""
    account_id: str = Field(default=None)
    amount: float = Field(default=None)
    created_at: str = Field(default=None)
    created_by: Optional[str] = Field(default=None)
    currency_code: CurrencyCode = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    organization_id: str = Field(default=None)
    payout_id: str = Field(default=None)
    payout_method_id: Optional[str] = Field(default=None)
    provider_code: Optional[ProviderCode] = Field(default=None)
    spi_bulk_instruction_id: Optional[str] = Field(default=None)
    status: PayoutStatus = Field(default=None)
    updated_at: str = Field(default=None)

class BeneficiaryPayoutsCreate(BaseModel):
    account_id: str
    amount: float
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    currency_code: CurrencyCode
    metadata: Optional[Dict[str, Any]] = None
    organization_id: str
    payout_id: Optional[str] = None
    payout_method_id: Optional[str] = None
    provider_code: Optional[ProviderCode] = None
    spi_bulk_instruction_id: Optional[str] = None
    status: Optional[PayoutStatus] = None
    updated_at: Optional[str] = None

class BeneficiaryPayoutsUpdate(BaseModel):
    account_id: Optional[str] = None
    amount: Optional[float] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    currency_code: Optional[CurrencyCode] = None
    metadata: Optional[Dict[str, Any]] = None
    organization_id: Optional[str] = None
    payout_id: Optional[str] = None
    payout_method_id: Optional[str] = None
    provider_code: Optional[ProviderCode] = None
    spi_bulk_instruction_id: Optional[str] = None
    status: Optional[PayoutStatus] = None
    updated_at: Optional[str] = None

