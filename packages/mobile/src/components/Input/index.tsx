import React, {
  forwardRef,
  useImperativeHandle,
  useRef,
  useState,
} from 'react';
import { InputProps } from '@rneui/base';
import { Controller, FieldErrors } from 'react-hook-form';

import { BaseInput, Container } from './styles';

interface CustomInputProps extends InputProps {
  name: string;
  control: any;
  errors: FieldErrors;
  label: string;
  color: string;
  styleContainer?: object;
  inputMask?: boolean;
  type:
}

interface InputRef {
  focus(): void;
}

const Input: React.ForwardRefRenderFunction<InputRef, CustomInputProps> = (
  { errors, name, control, inputMask, ...props },
  ref,
) => {
  const inputElementRef = useRef<any>(null);
  useImperativeHandle(ref, () => ({
    focus() {
      if (inputMask) {
        inputElementRef.current.getElement().focus();
      } else {
        inputElementRef.current.focus();
      }
    },
  }));
  const [rawValue, setRawValue] = useState<string | undefined>('');
  return (
    <Controller
      control={control}
      render={({ field: { onChange, onBlur, value } }) => (
        <Container>
          <BaseInput />
        </Container>
      )}
    />
  );
};

export default forwardRef(Input);
