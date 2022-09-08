import React from 'react';
import InputWithLabel, { InputWithLabelProps } from '../../components/inputWithLabel/index';

const LoginPage: React.FC = () => {
  const submitHandler: React.FormEventHandler = (e): void => {
    console.log(e.currentTarget);
    e.preventDefault();
  };
  return (
    <div className='login-page'>
      <h1>Вход</h1>
      <form onSubmit={submitHandler}>
        {(() => {
          const a: Array<Omit<InputWithLabelProps, 'id'>> = [{
            type: 'email',
            name: 'email',
            text: 'Логин',
            autocomplete: 'email'
          }, {
            name: 'password',
            type: 'password',
            text: 'Пароль',
            autocomplete: 'password'
          }];
          return a;
        })().map(e => (<React.Fragment key={e.name} >
          <InputWithLabel id={`${e.name}__login-input`} name={e.name} text={e.text} />
          <br />
        </React.Fragment>))}
        <input type="submit" value="Войти" />
      </form>
    </div>
  );
};

export default LoginPage;
