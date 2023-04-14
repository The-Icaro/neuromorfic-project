import { Inject, Injectable, CACHE_MANAGER } from '@nestjs/common';
import { HttpService } from '@nestjs/axios';
import { Cache } from 'cache-manager';

@Injectable()
export class AppService {
  constructor(
    private readonly httpService: HttpService,
    @Inject(CACHE_MANAGER) private cacheService: Cache,
  ) {}

  async storeExternalData(dataId: string, maxSize: number) {
    const cachedData = await this.getCacheData(dataId);

    if (cachedData) return cachedData;

    const { data } = await this.httpService.axiosRef.get(
      `https://api.thingspeak.com/channels/${dataId}/feeds.json?results=${maxSize}`,
    );

    return await this.setCacheData(dataId, data);
  }

  async getCacheData(key: string) {
    if (!key) return [];
    return await this.cacheService.get(key);
  }

  async setCacheData(key: string, data: any) {
    if (!key || !data) return [];

    await this.cacheService.set(key, data, 0);

    return await this.cacheService.get(key);
  }
}
