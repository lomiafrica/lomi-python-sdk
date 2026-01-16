from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class Subscriptions(BaseModel):
    """Subscription management - create and manage recurring billing model"""
    created_at: str = Field(default=None)
    created_by: Optional[str] = Field(default=None)
    customer_id: str = Field(default=None)
    end_date: Optional[str] = Field(default=None)
    environment: str = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    next_billing_date: Optional[str] = Field(default=None)
    organization_id: str = Field(default=None)
    price_id: Optional[str] = Field(default=None)
    product_id: str = Field(default=None)
    provider_payment_method_id: Optional[str] = Field(default=None)
    start_date: str = Field(default=None)
    status: SubscriptionStatus = Field(default=None)
    subscription_id: str = Field(default=None)
    updated_at: str = Field(default=None)

class SubscriptionsCreate(BaseModel):
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    customer_id: str
    end_date: Optional[str] = None
    environment: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    next_billing_date: Optional[str] = None
    organization_id: str
    price_id: Optional[str] = None
    product_id: str
    provider_payment_method_id: Optional[str] = None
    start_date: str
    status: Optional[SubscriptionStatus] = None
    subscription_id: Optional[str] = None
    updated_at: Optional[str] = None

class SubscriptionsUpdate(BaseModel):
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    customer_id: Optional[str] = None
    end_date: Optional[str] = None
    environment: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    next_billing_date: Optional[str] = None
    organization_id: Optional[str] = None
    price_id: Optional[str] = None
    product_id: Optional[str] = None
    provider_payment_method_id: Optional[str] = None
    start_date: Optional[str] = None
    status: Optional[SubscriptionStatus] = None
    subscription_id: Optional[str] = None
    updated_at: Optional[str] = None

