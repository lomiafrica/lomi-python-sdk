from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class DiscountCoupons(BaseModel):
    """Discount coupons - create and manage promotional codes model"""
    code: str = Field(default=None)
    coupon_id: str = Field(default=None)
    created_at: str = Field(default=None)
    current_uses: float = Field(default=None)
    customer_type: CustomerType = Field(default=None)
    description: Optional[str] = Field(default=None)
    discount_fixed_amount: Optional[float] = Field(default=None)
    discount_percentage: Optional[float] = Field(default=None)
    discount_type: DiscountType = Field(default=None)
    environment: str = Field(default=None)
    expires_at: Optional[str] = Field(default=None)
    is_active: bool = Field(default=None)
    max_quantity_per_use: Optional[float] = Field(default=None)
    max_uses: Optional[float] = Field(default=None)
    organization_id: str = Field(default=None)
    scope_type: str = Field(default=None)
    updated_at: str = Field(default=None)
    usage_frequency_limit: UsageFrequency = Field(default=None)
    usage_limit_value: Optional[float] = Field(default=None)
    valid_from: Optional[str] = Field(default=None)

class DiscountCouponsCreate(BaseModel):
    code: str
    coupon_id: Optional[str] = None
    created_at: Optional[str] = None
    current_uses: Optional[float] = None
    customer_type: Optional[CustomerType] = None
    description: Optional[str] = None
    discount_fixed_amount: Optional[float] = None
    discount_percentage: Optional[float] = None
    discount_type: Optional[DiscountType] = None
    environment: Optional[str] = None
    expires_at: Optional[str] = None
    is_active: Optional[bool] = None
    max_quantity_per_use: Optional[float] = None
    max_uses: Optional[float] = None
    organization_id: str
    scope_type: Optional[str] = None
    updated_at: Optional[str] = None
    usage_frequency_limit: Optional[UsageFrequency] = None
    usage_limit_value: Optional[float] = None
    valid_from: Optional[str] = None

class DiscountCouponsUpdate(BaseModel):
    code: Optional[str] = None
    coupon_id: Optional[str] = None
    created_at: Optional[str] = None
    current_uses: Optional[float] = None
    customer_type: Optional[CustomerType] = None
    description: Optional[str] = None
    discount_fixed_amount: Optional[float] = None
    discount_percentage: Optional[float] = None
    discount_type: Optional[DiscountType] = None
    environment: Optional[str] = None
    expires_at: Optional[str] = None
    is_active: Optional[bool] = None
    max_quantity_per_use: Optional[float] = None
    max_uses: Optional[float] = None
    organization_id: Optional[str] = None
    scope_type: Optional[str] = None
    updated_at: Optional[str] = None
    usage_frequency_limit: Optional[UsageFrequency] = None
    usage_limit_value: Optional[float] = None
    valid_from: Optional[str] = None

