'use client';

import React, { useEffect } from 'react';

const BadgesError = ({ error, reset }: { error: Error; reset: () => void }) => {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <>
      <h1>Erro</h1>
      <pre>{error.stack}</pre>
      <button
        onClick={() => {
          reset();
        }}
      >
        Reset
      </button>
    </>
  );
};

export default BadgesError;
