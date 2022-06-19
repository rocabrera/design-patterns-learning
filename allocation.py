from datetime import date
from typing import List, Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    orderlineid: str
    sku: str  # stock-keep-unit
    quantity: int  # amount of 


class Batch:

    def __init__(self, reference: str, sku: str, available_quantity: int, eta:Optional[date]) -> None:
        self.sku = sku
        self.eta = eta
        self.reference = reference
        self.available_quantity = available_quantity
        
    def can_allocate(self, line: OrderLine):
        return self.available_quantity >= line.quantity


    def allocate(self, line: OrderLine):
        self.available_quantity -= line.quantity
    
    