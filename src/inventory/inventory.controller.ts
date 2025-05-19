import { Controller, Get, Post, Body, Delete, Param } from '@nestjs/common';
import { InventoryService } from './inventory.service';
import { Product } from './schemas/product.schema';

@Controller('inventory')
export class InventoryController {
  constructor(private readonly inventoryService: InventoryService) {}

  @Get()
  findAll() {
    return this.inventoryService.findAll();
  }

  @Post()
  create(@Body() product: Product) {
    return this.inventoryService.create(product);
  }

  @Delete(':id')
  delete(@Param('id') id: string) {
    return this.inventoryService.delete(id);
  }
}