from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class Transactions(BaseModel):
    """Transaction history - view completed and pending transactions model"""
    checkout_session_id: Optional[str] = Field(default=None)
    created_at: str = Field(default=None)
    currency_code: CurrencyCode = Field(default=None)
    customer_id: str = Field(default=None)
    description: Optional[str] = Field(default=None)
    discount_amount: float = Field(default=None)
    environment: str = Field(default=None)
    fee_amount: float = Field(default=None)
    fee_structure_id: Optional[str] = Field(default=None)
    gross_amount: float = Field(default=None)
    integration_source: IntegrationSource = Field(default=None)
    is_bnpl: bool = Field(default=None)
    is_pos: bool = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    net_amount: float = Field(default=None)
    organization_id: str = Field(default=None)
    payment_method_code: PaymentMethodCode = Field(default=None)
    price_id: Optional[str] = Field(default=None)
    product_id: Optional[str] = Field(default=None)
    provider_code: ProviderCode = Field(default=None)
    quantity: float = Field(default=None)
    spi_account_number: Optional[str] = Field(default=None)
    spi_bulk_instruction_id: Optional[str] = Field(default=None)
    spi_date_envoi: Optional[str] = Field(default=None)
    spi_date_irrevocabilite: Optional[str] = Field(default=None)
    spi_discount_amount: Optional[float] = Field(default=None)
    spi_discount_rate: Optional[float] = Field(default=None)
    spi_end2end_id: Optional[str] = Field(default=None)
    spi_tx_id: Optional[str] = Field(default=None)
    status: TransactionStatus = Field(default=None)
    stripe_payment_intent_id: Optional[str] = Field(default=None)
    subscription_id: Optional[str] = Field(default=None)
    transaction_id: str = Field(default=None)
    transaction_type: TransactionType = Field(default=None)
    updated_at: str = Field(default=None)

class TransactionsCreate(BaseModel):
    checkout_session_id: Optional[str] = None
    created_at: Optional[str] = None
    currency_code: Optional[CurrencyCode] = None
    customer_id: str
    description: Optional[str] = None
    discount_amount: Optional[float] = None
    environment: Optional[str] = None
    fee_amount: float
    fee_structure_id: Optional[str] = None
    gross_amount: float
    integration_source: Optional[IntegrationSource] = None
    is_bnpl: Optional[bool] = None
    is_pos: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None
    net_amount: float
    organization_id: str
    payment_method_code: PaymentMethodCode
    price_id: Optional[str] = None
    product_id: Optional[str] = None
    provider_code: ProviderCode
    quantity: Optional[float] = None
    spi_account_number: Optional[str] = None
    spi_bulk_instruction_id: Optional[str] = None
    spi_date_envoi: Optional[str] = None
    spi_date_irrevocabilite: Optional[str] = None
    spi_discount_amount: Optional[float] = None
    spi_discount_rate: Optional[float] = None
    spi_end2end_id: Optional[str] = None
    spi_tx_id: Optional[str] = None
    status: Optional[TransactionStatus] = None
    stripe_payment_intent_id: Optional[str] = None
    subscription_id: Optional[str] = None
    transaction_id: Optional[str] = None
    transaction_type: TransactionType
    updated_at: Optional[str] = None

class TransactionsUpdate(BaseModel):
    checkout_session_id: Optional[str] = None
    created_at: Optional[str] = None
    currency_code: Optional[CurrencyCode] = None
    customer_id: Optional[str] = None
    description: Optional[str] = None
    discount_amount: Optional[float] = None
    environment: Optional[str] = None
    fee_amount: Optional[float] = None
    fee_structure_id: Optional[str] = None
    gross_amount: Optional[float] = None
    integration_source: Optional[IntegrationSource] = None
    is_bnpl: Optional[bool] = None
    is_pos: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None
    net_amount: Optional[float] = None
    organization_id: Optional[str] = None
    payment_method_code: Optional[PaymentMethodCode] = None
    price_id: Optional[str] = None
    product_id: Optional[str] = None
    provider_code: Optional[ProviderCode] = None
    quantity: Optional[float] = None
    spi_account_number: Optional[str] = None
    spi_bulk_instruction_id: Optional[str] = None
    spi_date_envoi: Optional[str] = None
    spi_date_irrevocabilite: Optional[str] = None
    spi_discount_amount: Optional[float] = None
    spi_discount_rate: Optional[float] = None
    spi_end2end_id: Optional[str] = None
    spi_tx_id: Optional[str] = None
    status: Optional[TransactionStatus] = None
    stripe_payment_intent_id: Optional[str] = None
    subscription_id: Optional[str] = None
    transaction_id: Optional[str] = None
    transaction_type: Optional[TransactionType] = None
    updated_at: Optional[str] = None

