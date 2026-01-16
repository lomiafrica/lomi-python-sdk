from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class Refunds(BaseModel):
    """Refund management - process and track refunds model"""
    amount: float = Field(default=None)
    created_at: str = Field(default=None)
    environment: str = Field(default=None)
    fee_amount: float = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    reason: Optional[str] = Field(default=None)
    refund_id: str = Field(default=None)
    refunded_amount: float = Field(default=None)
    spi_account_number: Optional[str] = Field(default=None)
    spi_end2end_id: Optional[str] = Field(default=None)
    spi_retour_date_demande: Optional[str] = Field(default=None)
    spi_retour_date_irrevocabilite: Optional[str] = Field(default=None)
    spi_tx_id: Optional[str] = Field(default=None)
    status: RefundStatus = Field(default=None)
    transaction_id: str = Field(default=None)
    updated_at: str = Field(default=None)

class RefundsCreate(BaseModel):
    amount: float
    created_at: Optional[str] = None
    environment: Optional[str] = None
    fee_amount: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None
    reason: Optional[str] = None
    refund_id: Optional[str] = None
    refunded_amount: float
    spi_account_number: Optional[str] = None
    spi_end2end_id: Optional[str] = None
    spi_retour_date_demande: Optional[str] = None
    spi_retour_date_irrevocabilite: Optional[str] = None
    spi_tx_id: Optional[str] = None
    status: Optional[RefundStatus] = None
    transaction_id: str
    updated_at: Optional[str] = None

class RefundsUpdate(BaseModel):
    amount: Optional[float] = None
    created_at: Optional[str] = None
    environment: Optional[str] = None
    fee_amount: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None
    reason: Optional[str] = None
    refund_id: Optional[str] = None
    refunded_amount: Optional[float] = None
    spi_account_number: Optional[str] = None
    spi_end2end_id: Optional[str] = None
    spi_retour_date_demande: Optional[str] = None
    spi_retour_date_irrevocabilite: Optional[str] = None
    spi_tx_id: Optional[str] = None
    status: Optional[RefundStatus] = None
    transaction_id: Optional[str] = None
    updated_at: Optional[str] = None

