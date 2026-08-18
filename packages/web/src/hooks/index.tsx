'use client';
import React from 'react';
import { AuthProvider } from './AuthContext';

function AppProvider({ children }: { children: React.ReactNode }) {
  return <AuthProvider>{children}</AuthProvider>;
}

export default AppProvider;
