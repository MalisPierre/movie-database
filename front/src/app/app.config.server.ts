import { mergeApplicationConfig, ApplicationConfig } from '@angular/core';
import { provideServerRendering, withRoutes } from '@angular/ssr';
import { appConfig } from './app.config';
import { serverRoutes } from './app.routes.server';
import {provideRouter} from '@angular/router';import routeConfig from './app.routes';
import { provideHttpClient } from '@angular/common/http';
const serverConfig: ApplicationConfig = {
  providers: [
    provideServerRendering(withRoutes(serverRoutes)),
    provideRouter(routeConfig),
    provideHttpClient(),
  ]
};
export const config = mergeApplicationConfig(appConfig, serverConfig);
