import React from 'react';
import InputWithLabel, { InputWithLabelProps } from '../../components/inputWithLabel/index';
import useFetch from '../../hooks/useFetch';

const LoginPage: React.FC = () => {
  const { fetch: f } = useFetch();
  const submitHandler: React.FormEventHandler = (e): void => {
    // console.log(e.currentTarget);
    e.preventDefault();
    const form = e.currentTarget;
    const values = Object.fromEntries([
      ...form.querySelectorAll('input').entries()
    ].map(e => e[1])
      .filter(i => i.type !== 'submit')
      .map(i => [i.name, i.value])
    );
    f('/api/auth/login', {
      method: 'POST',
      body: JSON.stringify({
        ...values,
        __secure_key: document.cookie.split(';').map(c => c.split('=')).find(c => c[0] === '__secure_key')?.[1] ?? 'no_secure_key'
      }),
      headers: [[
        'Content-Type',
        'application/json'
      ]]
    }).then().catch(console.error);
  };
  return (
    <div className='login-page'>
      <h1>Вход</h1>
      <form onSubmit={submitHandler}>
        {(() => {
          const a: Array<Omit<InputWithLabelProps, 'id'>> = [{
            type: 'email',
            name: 'login',
            text: 'Логин',
            autocomplete: 'email',
            required: true
          }, {
            name: 'password',
            type: 'password',
            text: 'Пароль',
            autocomplete: 'password',
            required: true
          }];
          return a;
        })().map(e => (<React.Fragment key={e.name} >
          <InputWithLabel
            id={`${e.name}__login-input`}
            name={e.name}
            text={e.text}
            required={e.required}
          />
          <br />
        </React.Fragment>))}
        <input type="submit" value="Войти" />
      </form>
    </div>
  );
};

export default LoginPage;
