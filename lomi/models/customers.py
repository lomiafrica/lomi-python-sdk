from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class Customers(BaseModel):
    """Customer management - create and manage customer profiles model"""
    address: Optional[str] = Field(default=None)
    city: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    created_at: str = Field(default=None)
    created_by: Optional[str] = Field(default=None)
    customer_id: str = Field(default=None)
    deleted_at: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    environment: str = Field(default=None)
    is_business: bool = Field(default=None)
    is_deleted: bool = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    name: str = Field(default=None)
    organization_id: str = Field(default=None)
    phone_number: Optional[str] = Field(default=None)
    postal_code: Optional[str] = Field(default=None)
    provider_customer_id: Optional[str] = Field(default=None)
    spi_alias_mbno: Optional[str] = Field(default=None)
    spi_alias_shid: Optional[str] = Field(default=None)
    spi_primary_alias: Optional[str] = Field(default=None)
    updated_at: str = Field(default=None)
    whatsapp_number: Optional[str] = Field(default=None)

class CustomersCreate(BaseModel):
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    customer_id: Optional[str] = None
    deleted_at: Optional[str] = None
    email: Optional[str] = None
    environment: Optional[str] = None
    is_business: Optional[bool] = None
    is_deleted: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None
    name: str
    organization_id: str
    phone_number: Optional[str] = None
    postal_code: Optional[str] = None
    provider_customer_id: Optional[str] = None
    spi_alias_mbno: Optional[str] = None
    spi_alias_shid: Optional[str] = None
    spi_primary_alias: Optional[str] = None
    updated_at: Optional[str] = None
    whatsapp_number: Optional[str] = None

class CustomersUpdate(BaseModel):
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    customer_id: Optional[str] = None
    deleted_at: Optional[str] = None
    email: Optional[str] = None
    environment: Optional[str] = None
    is_business: Optional[bool] = None
    is_deleted: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    organization_id: Optional[str] = None
    phone_number: Optional[str] = None
    postal_code: Optional[str] = None
    provider_customer_id: Optional[str] = None
    spi_alias_mbno: Optional[str] = None
    spi_alias_shid: Optional[str] = None
    spi_primary_alias: Optional[str] = None
    updated_at: Optional[str] = None
    whatsapp_number: Optional[str] = None

