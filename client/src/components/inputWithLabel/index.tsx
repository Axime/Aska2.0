import React, { useState } from 'react';
export interface InputWithLabelProps {
  type?: React.HTMLInputTypeAttribute
  name: string
  init?: string
  id: string
  placeholder?: string
  text: string
  autocomplete?: string
}

const InputWithLabel: React.FC<InputWithLabelProps> = ({
  type = 'text',
  name,
  init = '',
  id,
  placeholder = '',
  text,
  autocomplete = 'off'
}) => {
  const [value, setValue] = useState(init);

  return (<>
    <label htmlFor={id}>{text}</label>
    <input
      type={type}
      name={name}
      onInput={e => setValue(e.currentTarget.value)}
      value={value}
      placeholder={placeholder}
      autoComplete={autocomplete}
    />
  </>);
};

export default InputWithLabel;
