import axios from 'axios';
import { env } from '../config/env';

export const apiClient = axios.create({ baseURL: env.apiBaseUrl, timeout: 15000, headers: { 'Content-Type': 'application/json' } });

export function attachAccessToken(getToken) {
  apiClient.interceptors.request.use(async (config) => {
    const token = await getToken();
    if (token) config.headers.Authorization = 'Bearer ' + token;
    return config;
  });
}
