import React from 'react';
import Copyright from '../Copyright';
import NavBar from '../NavBar';

export default function Layout({ children }) {
  return (
    <>
      <NavBar />
      <main>{children}</main>
      <Copyright mt={5} />
    </>
  );
}
