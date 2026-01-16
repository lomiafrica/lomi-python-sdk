from typing import List, Optional
from ..models import DiscountCoupons, DiscountCouponsCreate, DiscountCouponsUpdate
from ..client_base import ClientBase

class DiscountCouponsService(ClientBase):
    """discount_coupons API service"""
    
    
    def list(self, **params) -> List[DiscountCoupons]:
        """List discount_coupons"""
        return self._request("GET", "/discount-coupons", model=DiscountCoupons, params=params)
    
    
    def get(self, id: str) -> DiscountCoupons:
        """Get a single discount_coupon"""
        return self._request("GET", f"/discount-coupons/{id}", model=DiscountCoupons)
    
    
    def create(self, data: DiscountCouponsCreate) -> DiscountCoupons:
        """Create a new discount_coupon"""
        return self._request("POST", "/discount-coupons", model=DiscountCoupons, data=data)
    
    
    
