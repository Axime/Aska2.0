import React, { useState, useCallback } from 'react';

interface useFetchReturnType {
  isLoading: boolean
  setIsLoading: React.Dispatch<React.SetStateAction<boolean>>
  fetch: typeof fetch
}

const useFetch = (): useFetchReturnType => {
  const [isLoading, setIsLoading] = useState(false);
  return {
    isLoading,
    setIsLoading,
    fetch: useCallback(async (...args: Parameters<typeof fetch>) => {
      setIsLoading(true);
      return await fetch(...args).then(r => { setIsLoading(false); return r; });
    }, [fetch, setIsLoading])
  };
};

export default useFetch;
