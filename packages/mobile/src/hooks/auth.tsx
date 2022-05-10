import api from '@fastentregas/axios-config';
import AsyncStorage from '@react-native-async-storage/async-storage';
import React, {
  createContext,
  useContext,
  useEffect,
  useState,
  useCallback,
} from 'react';
import AuthService from '../services/AuthService';

export interface SignInCredentials {
  telephone: string;
  password: string;
}

interface AuthContextData {
  // user: string | Record<any, string>;
  token: string;
  signIn(credentials: SignInCredentials): Promise<void>;
  signOut(): void;
  loading: boolean;
}

const AuthContext = createContext<AuthContextData>({} as AuthContextData);

export const AuthProvider: React.FC = ({ children }) => {
  const [data, setData] = useState({ token: '' });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadStorageData() {
      const [token] = await AsyncStorage.multiGet(['@Fast:token']);
      if (token[1]) {
        api.defaults.headers.authorization = `Bearer ${token[1]}`;
        setData({ token: token[1] });
      }
      setLoading(false);
    }
    loadStorageData();
  }, []);

  const signIn = useCallback(async ({ telephone, password }) => {
    try {
      const { data } = await AuthService.signIn({ telephone, password });
      const { token } = data;
      await AsyncStorage.multiSet([['@Fast:token', token]]);
      api.defaults.headers.authorization = `Bearer ${token}`;
      setData({ token });
    } catch (err) {
      console.error(err);
      throw new Error(err);
    }
  }, []);
  const signOut = useCallback(async () => {
    await AsyncStorage.multiRemove(['@Fast:token']);
    setData({ token: '' });
  }, []);
  return (
    <AuthContext.Provider
      value={{ loading, signIn, token: data.token, signOut }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export function useAuth(): AuthContextData {
  const context = useContext(AuthContext);
  return context;
}
