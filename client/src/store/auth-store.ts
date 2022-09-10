import { legacy_createStore as createStore } from 'redux';

// eslint-disable-next-line @typescript-eslint/no-namespace
namespace Auth {
  export const enum AuthState {
    NotAuthorized,
    Authorized,
  }
  interface storeType {
    auth: AuthState
    token: string | null
    hash: string | null
  };

  const enum AuthActionType {
    login,
    logout
  }

  type AuthAction = {
    type: AuthActionType.logout
  } | {
    type: AuthActionType.login
    value: {
      token: string | null
      hash: string | null
    }
  };

  const reducer = (state: storeType | undefined, action: AuthAction): storeType => {
    switch (action?.type) {
      case AuthActionType.login:
        return {
          auth: AuthState.Authorized,
          token: action.value.token,
          hash: action.value.hash
        };
      case AuthActionType.logout: return {
        ...state,
        auth: AuthState.NotAuthorized,
        hash: null,
        token: null
      };
      default: return {
        auth: AuthState.NotAuthorized,
        hash: null,
        token: null
      };
    }
  };
  export const store = createStore<storeType, AuthAction, storeType, {}>(reducer, {
    auth: AuthState.NotAuthorized,
    token: null,
    hash: null
  });

  export const setState = <T extends AuthState>(authorized: T, ...args: T extends AuthState.Authorized ? [token: string, hash: string] : []): AuthAction => store.dispatch<AuthAction>((() => {
    if (authorized === AuthState.Authorized) {
      return {
        type: AuthActionType.login,
        value: {
          token: args[0] ?? '',
          hash: args[1] ?? ''
        }
      };
    }
    return {
      type: AuthActionType.logout,
      value: {
        token: null,
        hash: null
      }
    };
  })());
}

export default Auth;
