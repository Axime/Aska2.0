import { legacy_createStore as createStore } from 'redux';

// eslint-disable-next-line @typescript-eslint/no-namespace
namespace Auth {
  export const enum AuthState {
    NotAuthorized,
    Authorized,
  }
  interface storeType {
    auth: AuthState
  };

  const enum AuthActionType {
    login,
    logout
  }

  interface AuthAction {
    type: AuthActionType
  };

  const reducer = (state: storeType | undefined, action: AuthAction): storeType => {
    switch (action?.type) {
      case AuthActionType.login:
        return {
          ...state,
          auth: AuthState.Authorized
        };
      case AuthActionType.logout: return {
        ...state,
        auth: AuthState.NotAuthorized
      };
      default: return {
        auth: AuthState.NotAuthorized
      };
    }
  };
  export const store = createStore<storeType, AuthAction, {}, {}>(reducer, {
    auth: AuthState.NotAuthorized
  });

  export const setState = (authorized: AuthState): AuthAction => store.dispatch({
    type: authorized === AuthState.Authorized ? AuthActionType.login : AuthActionType.logout
  });
}

export default Auth;
