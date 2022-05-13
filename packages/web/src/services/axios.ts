import api from '@fastentregas/axios-config';
import { parseCookies } from 'nookies';

export function getAPIClient(ctx?: any) {
  const { 'nextauth.token': token } = parseCookies(ctx);

  api.interceptors.request.use(config => {
    return config;
  });

  if (token) {
    api.defaults.headers.authorization = `Bearer ${token}`;
  }

  return api;
}
