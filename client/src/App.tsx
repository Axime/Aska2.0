import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
// import logo from './logo.svg';
import Auth from './store/auth-store';
import './App.css';
import RegistrationPage from './pages/registration';
import LoginPage from './pages/login/index';

const App: React.FC = () => {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          {Auth.store.getState().auth === Auth.AuthState.NotAuthorized
            ? (<>
              <Route caseSensitive path='/login' element={<LoginPage />} />
              <Route path='/register' element={<RegistrationPage />} />
              <Route path='*' element={<Navigate replace to="/" />} />
              <Route element={<h1>Hello world</h1>} index />
            </>)
            : (<>
              {/* <Route element={<h1>Авторизован</h1>} /> */}
            </>)
          }
        </Routes>
      </BrowserRouter>
    </div>
  );
};

export default App;
