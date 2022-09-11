import React from 'react';
import InputWithLabel from '../../components/inputWithLabel/index';
import useFetch from '../../hooks/useFetch';

const RegistrationPage: React.FC = () => {
  const {
    fetch: f
  } = useFetch();
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
    if (values.password !== values.password_repeat) {
      alert('Пароли не совпадают');
      return;
    }
    f('/api/auth/registration', {
      method: 'POST',
      body: JSON.stringify({
        ...values,
        __secure_key: '1bcd8735'
      }),
      headers: [[
        'Content-Type',
        'application/json'
      ]]
    }).then().catch(console.error);
  };
  return (
    <div className='registration-page'>
      <h1>Регистрация</h1>
      <form onSubmit={submitHandler}>
        {[{
          name: 'first_name',
          text: 'Имя',
          autocomplete: 'first-name',
          required: true
        }, {
          name: 'last_name',
          text: 'Фамилия',
          autocomplete: 'last-name',
          required: true
        }, {
          type: 'email',
          text: 'Email',
          autocomplete: 'email',
          name: 'email',
          required: true
        }, {
          name: 'password',
          type: 'password',
          text: 'Пароль',
          required: true
        }, {
          name: 'password_repeat',
          type: 'password-repeat',
          text: 'Повотрите пароль',
          required: true
        }].map(e => (<React.Fragment key={e.name} >
          <InputWithLabel
            id={`${e.name}__reg-input`}
            name={e.name} text={e.text}
            type={e.type ?? 'text'}
            required={e.required}
          />
          <br />
        </React.Fragment>))}
        {/* <input type="hidden" name="__secret_key" value="secret_key" /> */}
        <input type="submit" value="123" />
      </form>
    </div>
  );
};

export default RegistrationPage;
