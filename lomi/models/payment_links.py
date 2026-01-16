from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class PaymentLinks(BaseModel):
    """Payment links - shareable payment URLs model"""
    allow_coupon_code: bool = Field(default=None)
    allow_quantity: bool = Field(default=None)
    amount: Optional[float] = Field(default=None)
    cancel_url: Optional[str] = Field(default=None)
    created_at: str = Field(default=None)
    created_by: Optional[str] = Field(default=None)
    currency_code: CurrencyCode = Field(default=None)
    description: Optional[str] = Field(default=None)
    environment: str = Field(default=None)
    expires_at: Optional[str] = Field(default=None)
    is_active: bool = Field(default=None)
    link_id: str = Field(default=None)
    link_type: LinkType = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    organization_id: str = Field(default=None)
    price_id: Optional[str] = Field(default=None)
    product_id: Optional[str] = Field(default=None)
    quantity: float = Field(default=None)
    require_billing_address: bool = Field(default=None)
    success_url: Optional[str] = Field(default=None)
    title: str = Field(default=None)
    updated_at: str = Field(default=None)
    url: str = Field(default=None)

class PaymentLinksCreate(BaseModel):
    allow_coupon_code: Optional[bool] = None
    allow_quantity: Optional[bool] = None
    amount: Optional[float] = None
    cancel_url: Optional[str] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    currency_code: CurrencyCode
    description: Optional[str] = None
    environment: Optional[str] = None
    expires_at: Optional[str] = None
    is_active: Optional[bool] = None
    link_id: Optional[str] = None
    link_type: LinkType
    metadata: Optional[Dict[str, Any]] = None
    organization_id: str
    price_id: Optional[str] = None
    product_id: Optional[str] = None
    quantity: Optional[float] = None
    require_billing_address: Optional[bool] = None
    success_url: Optional[str] = None
    title: str
    updated_at: Optional[str] = None
    url: str

class PaymentLinksUpdate(BaseModel):
    allow_coupon_code: Optional[bool] = None
    allow_quantity: Optional[bool] = None
    amount: Optional[float] = None
    cancel_url: Optional[str] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    currency_code: Optional[CurrencyCode] = None
    description: Optional[str] = None
    environment: Optional[str] = None
    expires_at: Optional[str] = None
    is_active: Optional[bool] = None
    link_id: Optional[str] = None
    link_type: Optional[LinkType] = None
    metadata: Optional[Dict[str, Any]] = None
    organization_id: Optional[str] = None
    price_id: Optional[str] = None
    product_id: Optional[str] = None
    quantity: Optional[float] = None
    require_billing_address: Optional[bool] = None
    success_url: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None
    url: Optional[str] = None

