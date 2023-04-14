import {
  Body,
  Controller,
  Get,
  Post,
  UseInterceptors,
  CacheInterceptor,
  Query,
} from '@nestjs/common';
import { AppService } from './app.service';

@Controller('app')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get('/storedata/')
  async findOne(@Query('id') id: string) {
    return await this.appService.getCacheData(id);
  }

  @UseInterceptors(CacheInterceptor)
  @Post('/storedata/')
  async storeNewData(
    @Body() storeNewData: { dataId: string; maxSize: number },
  ) {
    const { dataId, maxSize } = storeNewData;
    return await this.appService.storeExternalData(dataId, maxSize);
  }
}
