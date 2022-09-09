import React from 'react';
import InputWithLabel from '../../components/inputWithLabel/index';

const RegistrationPage: React.FC = () => {
  const submitHandler: React.FormEventHandler = (e): void => {
    console.log(e.currentTarget);
    e.preventDefault();
  };
  return (
    <div className='registration-page'>
      <h1>Регистрация</h1>
      <form onSubmit={submitHandler}>
        {[{
          name: 'firstName',
          text: 'Имя',
          autocomplete: 'first-name'
        }, {
          name: 'lastName',
          text: 'Фамилия',
          autocomplete: 'last-name'
        }, {
          type: 'email',
          text: 'Email',
          autocomplete: 'email',
          name: 'email'
        }, {
          name: 'password',
          type: 'password',
          text: 'Пароль'
        }, {
          name: 'paswordRepeat',
          type: 'password-repeat',
          text: 'Повотрите пароль'
        }].map(e => (<React.Fragment key={e.name} >
          <InputWithLabel
            id={`${e.name}__reg-input`}
            name={e.name} text={e.text}
            type={e.type ?? 'text'}
          />
          <br />
        </React.Fragment>))}
        <input type="submit" value="123" />
      </form>
    </div>
  );
};

export default RegistrationPage;
