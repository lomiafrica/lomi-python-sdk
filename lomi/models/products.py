from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class Products(BaseModel):
    """Products - manage one-time and recurring products model"""
    charge_day: Optional[float] = Field(default=None)
    continue_selling_when_out_of_stock: Optional[bool] = Field(default=None)
    created_at: str = Field(default=None)
    created_by: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    display_on_storefront: bool = Field(default=None)
    environment: str = Field(default=None)
    images: Optional[List[str]] = Field(default=None)
    inventory_quantity: Optional[float] = Field(default=None)
    is_active: bool = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    name: str = Field(default=None)
    organization_id: str = Field(default=None)
    product_id: str = Field(default=None)
    product_type: ProductType = Field(default=None)
    sku: Optional[str] = Field(default=None)
    track_inventory: Optional[bool] = Field(default=None)
    trial_enabled: bool = Field(default=None)
    trial_period_days: Optional[float] = Field(default=None)
    updated_at: str = Field(default=None)
    usage_unit: Optional[str] = Field(default=None)

class ProductsCreate(BaseModel):
    charge_day: Optional[float] = None
    continue_selling_when_out_of_stock: Optional[bool] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    description: Optional[str] = None
    display_on_storefront: Optional[bool] = None
    environment: Optional[str] = None
    images: Optional[List[str]] = None
    inventory_quantity: Optional[float] = None
    is_active: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None
    name: str
    organization_id: str
    product_id: Optional[str] = None
    product_type: Optional[ProductType] = None
    sku: Optional[str] = None
    track_inventory: Optional[bool] = None
    trial_enabled: Optional[bool] = None
    trial_period_days: Optional[float] = None
    updated_at: Optional[str] = None
    usage_unit: Optional[str] = None

class ProductsUpdate(BaseModel):
    charge_day: Optional[float] = None
    continue_selling_when_out_of_stock: Optional[bool] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    description: Optional[str] = None
    display_on_storefront: Optional[bool] = None
    environment: Optional[str] = None
    images: Optional[List[str]] = None
    inventory_quantity: Optional[float] = None
    is_active: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    organization_id: Optional[str] = None
    product_id: Optional[str] = None
    product_type: Optional[ProductType] = None
    sku: Optional[str] = None
    track_inventory: Optional[bool] = None
    trial_enabled: Optional[bool] = None
    trial_period_days: Optional[float] = None
    updated_at: Optional[str] = None
    usage_unit: Optional[str] = None

