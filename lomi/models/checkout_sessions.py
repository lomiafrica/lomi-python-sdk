from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class CheckoutSessions(BaseModel):
    """Checkout sessions - create hosted payment pages model"""
    allow_coupon_code: bool = Field(default=None)
    allow_quantity: bool = Field(default=None)
    amount: float = Field(default=None)
    cancel_url: Optional[str] = Field(default=None)
    checkout_session_id: str = Field(default=None)
    created_at: str = Field(default=None)
    created_by: Optional[str] = Field(default=None)
    currency_code: CurrencyCode = Field(default=None)
    customer_email: Optional[str] = Field(default=None)
    customer_id: Optional[str] = Field(default=None)
    customer_name: Optional[str] = Field(default=None)
    customer_phone: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    environment: str = Field(default=None)
    expires_at: str = Field(default=None)
    installment_plan_id: Optional[str] = Field(default=None)
    integration_source: IntegrationSource = Field(default=None)
    is_pos: bool = Field(default=None)
    is_spi: bool = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    organization_id: str = Field(default=None)
    payment_link_id: Optional[str] = Field(default=None)
    payment_request_id: Optional[str] = Field(default=None)
    price_id: Optional[str] = Field(default=None)
    product_id: Optional[str] = Field(default=None)
    qr_code_data: Optional[Dict[str, Any]] = Field(default=None)
    qr_code_type: Optional[QrCodeType] = Field(default=None)
    quantity: float = Field(default=None)
    require_billing_address: bool = Field(default=None)
    spi_account_number: Optional[str] = Field(default=None)
    spi_qr_code_id: Optional[str] = Field(default=None)
    status: CheckoutSessionStatus = Field(default=None)
    subscription_id: Optional[str] = Field(default=None)
    success_url: Optional[str] = Field(default=None)
    title: Optional[str] = Field(default=None)
    updated_at: str = Field(default=None)

class CheckoutSessionsCreate(BaseModel):
    allow_coupon_code: Optional[bool] = None
    allow_quantity: Optional[bool] = None
    amount: float
    cancel_url: Optional[str] = None
    checkout_session_id: Optional[str] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    currency_code: CurrencyCode
    customer_email: Optional[str] = None
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None
    description: Optional[str] = None
    environment: Optional[str] = None
    expires_at: str
    installment_plan_id: Optional[str] = None
    integration_source: Optional[IntegrationSource] = None
    is_pos: Optional[bool] = None
    is_spi: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None
    organization_id: str
    payment_link_id: Optional[str] = None
    payment_request_id: Optional[str] = None
    price_id: Optional[str] = None
    product_id: Optional[str] = None
    qr_code_data: Optional[Dict[str, Any]] = None
    qr_code_type: Optional[QrCodeType] = None
    quantity: Optional[float] = None
    require_billing_address: Optional[bool] = None
    spi_account_number: Optional[str] = None
    spi_qr_code_id: Optional[str] = None
    status: Optional[CheckoutSessionStatus] = None
    subscription_id: Optional[str] = None
    success_url: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None

class CheckoutSessionsUpdate(BaseModel):
    allow_coupon_code: Optional[bool] = None
    allow_quantity: Optional[bool] = None
    amount: Optional[float] = None
    cancel_url: Optional[str] = None
    checkout_session_id: Optional[str] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    currency_code: Optional[CurrencyCode] = None
    customer_email: Optional[str] = None
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None
    description: Optional[str] = None
    environment: Optional[str] = None
    expires_at: Optional[str] = None
    installment_plan_id: Optional[str] = None
    integration_source: Optional[IntegrationSource] = None
    is_pos: Optional[bool] = None
    is_spi: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None
    organization_id: Optional[str] = None
    payment_link_id: Optional[str] = None
    payment_request_id: Optional[str] = None
    price_id: Optional[str] = None
    product_id: Optional[str] = None
    qr_code_data: Optional[Dict[str, Any]] = None
    qr_code_type: Optional[QrCodeType] = None
    quantity: Optional[float] = None
    require_billing_address: Optional[bool] = None
    spi_account_number: Optional[str] = None
    spi_qr_code_id: Optional[str] = None
    status: Optional[CheckoutSessionStatus] = None
    subscription_id: Optional[str] = None
    success_url: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None

