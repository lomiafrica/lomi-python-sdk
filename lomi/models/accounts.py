from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class Accounts(BaseModel):
    """Account balances - view organization account balances and SPI account information model"""
    account_id: str = Field(default=None)
    balance: float = Field(default=None)
    created_at: str = Field(default=None)
    currency_code: CurrencyCode = Field(default=None)
    is_spi_account: bool = Field(default=None)
    organization_id: str = Field(default=None)
    spi_account_balance: Optional[float] = Field(default=None)
    spi_account_balance_sync_error: Optional[str] = Field(default=None)
    spi_account_balance_synced_at: Optional[str] = Field(default=None)
    spi_account_number: Optional[str] = Field(default=None)
    updated_at: str = Field(default=None)

class AccountsCreate(BaseModel):
    account_id: Optional[str] = None
    balance: Optional[float] = None
    created_at: Optional[str] = None
    currency_code: Optional[CurrencyCode] = None
    is_spi_account: Optional[bool] = None
    organization_id: str
    spi_account_balance: Optional[float] = None
    spi_account_balance_sync_error: Optional[str] = None
    spi_account_balance_synced_at: Optional[str] = None
    spi_account_number: Optional[str] = None
    updated_at: Optional[str] = None

class AccountsUpdate(BaseModel):
    account_id: Optional[str] = None
    balance: Optional[float] = None
    created_at: Optional[str] = None
    currency_code: Optional[CurrencyCode] = None
    is_spi_account: Optional[bool] = None
    organization_id: Optional[str] = None
    spi_account_balance: Optional[float] = None
    spi_account_balance_sync_error: Optional[str] = None
    spi_account_balance_synced_at: Optional[str] = None
    spi_account_number: Optional[str] = None
    updated_at: Optional[str] = None

