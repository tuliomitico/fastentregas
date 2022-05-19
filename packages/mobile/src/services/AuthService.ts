import api from '@fastentregas/axios-config';

interface ILoginDTO {
  telephone: string;
  password: string;
}

export default class AuthService {
  static signIn(data: ILoginDTO): Promise<any> {
    return api.post('/login', {
      telephone: data.telephone,
      password: data.password,
    });
  }

  static signUp(data: ILoginDTO): Promise<any> {
    return api.post('/delivery_boy/create_password', {
      telephone: data.telephone,
      password: data.password,
    });
  }
}
