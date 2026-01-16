from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class PaymentRequests(BaseModel):
    """Payment requests - create payment intents and track status model"""
    amount: float = Field(default=None)
    created_at: str = Field(default=None)
    created_by: Optional[str] = Field(default=None)
    currency_code: CurrencyCode = Field(default=None)
    customer_id: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    environment: str = Field(default=None)
    expiry_date: str = Field(default=None)
    organization_id: str = Field(default=None)
    payment_link: Optional[str] = Field(default=None)
    payment_reference: Optional[str] = Field(default=None)
    request_id: str = Field(default=None)
    spi_account_number: Optional[str] = Field(default=None)
    spi_bulk_instruction_id: Optional[str] = Field(default=None)
    spi_confirmation: bool = Field(default=None)
    spi_date_envoi: Optional[str] = Field(default=None)
    spi_date_irrevocabilite: Optional[str] = Field(default=None)
    spi_date_limite_paiement: Optional[str] = Field(default=None)
    spi_date_limite_reponse: Optional[str] = Field(default=None)
    spi_date_rejet: Optional[str] = Field(default=None)
    spi_debit_differe: bool = Field(default=None)
    spi_end2end_id: Optional[str] = Field(default=None)
    spi_payeur_alias: Optional[str] = Field(default=None)
    spi_payeur_nom: Optional[str] = Field(default=None)
    spi_payeur_pays: Optional[str] = Field(default=None)
    spi_ref_doc_numero: Optional[str] = Field(default=None)
    spi_remise_amount: Optional[float] = Field(default=None)
    spi_remise_rate: Optional[float] = Field(default=None)
    spi_tx_id: Optional[str] = Field(default=None)
    status: TransactionStatus = Field(default=None)
    updated_at: str = Field(default=None)

class PaymentRequestsCreate(BaseModel):
    amount: float
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    currency_code: CurrencyCode
    customer_id: Optional[str] = None
    description: Optional[str] = None
    environment: Optional[str] = None
    expiry_date: str
    organization_id: str
    payment_link: Optional[str] = None
    payment_reference: Optional[str] = None
    request_id: Optional[str] = None
    spi_account_number: Optional[str] = None
    spi_bulk_instruction_id: Optional[str] = None
    spi_confirmation: Optional[bool] = None
    spi_date_envoi: Optional[str] = None
    spi_date_irrevocabilite: Optional[str] = None
    spi_date_limite_paiement: Optional[str] = None
    spi_date_limite_reponse: Optional[str] = None
    spi_date_rejet: Optional[str] = None
    spi_debit_differe: Optional[bool] = None
    spi_end2end_id: Optional[str] = None
    spi_payeur_alias: Optional[str] = None
    spi_payeur_nom: Optional[str] = None
    spi_payeur_pays: Optional[str] = None
    spi_ref_doc_numero: Optional[str] = None
    spi_remise_amount: Optional[float] = None
    spi_remise_rate: Optional[float] = None
    spi_tx_id: Optional[str] = None
    status: Optional[TransactionStatus] = None
    updated_at: Optional[str] = None

class PaymentRequestsUpdate(BaseModel):
    amount: Optional[float] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    currency_code: Optional[CurrencyCode] = None
    customer_id: Optional[str] = None
    description: Optional[str] = None
    environment: Optional[str] = None
    expiry_date: Optional[str] = None
    organization_id: Optional[str] = None
    payment_link: Optional[str] = None
    payment_reference: Optional[str] = None
    request_id: Optional[str] = None
    spi_account_number: Optional[str] = None
    spi_bulk_instruction_id: Optional[str] = None
    spi_confirmation: Optional[bool] = None
    spi_date_envoi: Optional[str] = None
    spi_date_irrevocabilite: Optional[str] = None
    spi_date_limite_paiement: Optional[str] = None
    spi_date_limite_reponse: Optional[str] = None
    spi_date_rejet: Optional[str] = None
    spi_debit_differe: Optional[bool] = None
    spi_end2end_id: Optional[str] = None
    spi_payeur_alias: Optional[str] = None
    spi_payeur_nom: Optional[str] = None
    spi_payeur_pays: Optional[str] = None
    spi_ref_doc_numero: Optional[str] = None
    spi_remise_amount: Optional[float] = None
    spi_remise_rate: Optional[float] = None
    spi_tx_id: Optional[str] = None
    status: Optional[TransactionStatus] = None
    updated_at: Optional[str] = None

