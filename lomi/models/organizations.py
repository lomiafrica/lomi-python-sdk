from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class Organizations(BaseModel):
    """Organization metrics - view MRR, ARR, total revenue, merchant lifetime value, and other organization metrics model"""
    arr: float = Field(default=None)
    created_at: str = Field(default=None)
    default_currency: CurrencyCode = Field(default=None)
    deleted_at: Optional[str] = Field(default=None)
    email: str = Field(default=None)
    employee_number: Optional[str] = Field(default=None)
    industry: Optional[str] = Field(default=None)
    is_deleted: bool = Field(default=None)
    is_starter_business: bool = Field(default=None)
    logo_url: Optional[str] = Field(default=None)
    merchant_lifetime_value: float = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    mrr: float = Field(default=None)
    name: str = Field(default=None)
    organization_id: str = Field(default=None)
    phone_number: str = Field(default=None)
    pin_code: Optional[str] = Field(default=None)
    slug: Optional[str] = Field(default=None)
    status: OrganizationStatus = Field(default=None)
    storefront_enabled: bool = Field(default=None)
    total_customers: Optional[float] = Field(default=None)
    total_merchants: Optional[float] = Field(default=None)
    total_revenue: Optional[float] = Field(default=None)
    total_transactions: Optional[float] = Field(default=None)
    updated_at: str = Field(default=None)
    verification_status: OrganizationVerificationStatus = Field(default=None)
    website_url: Optional[str] = Field(default=None)

class OrganizationsCreate(BaseModel):
    arr: Optional[float] = None
    created_at: Optional[str] = None
    default_currency: Optional[CurrencyCode] = None
    deleted_at: Optional[str] = None
    email: str
    employee_number: Optional[str] = None
    industry: Optional[str] = None
    is_deleted: Optional[bool] = None
    is_starter_business: Optional[bool] = None
    logo_url: Optional[str] = None
    merchant_lifetime_value: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None
    mrr: Optional[float] = None
    name: str
    organization_id: Optional[str] = None
    phone_number: str
    pin_code: Optional[str] = None
    slug: Optional[str] = None
    status: Optional[OrganizationStatus] = None
    storefront_enabled: Optional[bool] = None
    total_customers: Optional[float] = None
    total_merchants: Optional[float] = None
    total_revenue: Optional[float] = None
    total_transactions: Optional[float] = None
    updated_at: Optional[str] = None
    verification_status: Optional[OrganizationVerificationStatus] = None
    website_url: Optional[str] = None

class OrganizationsUpdate(BaseModel):
    arr: Optional[float] = None
    created_at: Optional[str] = None
    default_currency: Optional[CurrencyCode] = None
    deleted_at: Optional[str] = None
    email: Optional[str] = None
    employee_number: Optional[str] = None
    industry: Optional[str] = None
    is_deleted: Optional[bool] = None
    is_starter_business: Optional[bool] = None
    logo_url: Optional[str] = None
    merchant_lifetime_value: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None
    mrr: Optional[float] = None
    name: Optional[str] = None
    organization_id: Optional[str] = None
    phone_number: Optional[str] = None
    pin_code: Optional[str] = None
    slug: Optional[str] = None
    status: Optional[OrganizationStatus] = None
    storefront_enabled: Optional[bool] = None
    total_customers: Optional[float] = None
    total_merchants: Optional[float] = None
    total_revenue: Optional[float] = None
    total_transactions: Optional[float] = None
    updated_at: Optional[str] = None
    verification_status: Optional[OrganizationVerificationStatus] = None
    website_url: Optional[str] = None

