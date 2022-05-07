import React, {
  forwardRef,
  useImperativeHandle,
  useRef,
  useState,
} from 'react';
import { InputProps } from '@rneui/base';
import { Controller, FieldErrors } from 'react-hook-form';

import { BaseInput, Container, Error } from './styles';
import {
  TextInputMask,
  TextInputMaskOptionProp,
  TextInputMaskTypeProp,
} from 'react-native-masked-text';

interface CustomInputProps extends InputProps {
  name: string;
  control: any;
  errors: FieldErrors;
  label: string;
  color: string;
  styleContainer?: object;
  inputMask?: boolean;
  type?: TextInputMaskTypeProp;
  options?: TextInputMaskOptionProp;
  disabled?: boolean;
}

interface InputRef {
  focus(): void;
}

const Input: React.ForwardRefRenderFunction<InputRef, CustomInputProps> = (
  {
    errors,
    name,
    control,
    label,
    color,
    styleContainer,
    disabled,
    inputMask,
    type,
    options,
    ...props
  },
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
        <Container style={styleContainer}>
          {inputMask && type ? (
            <TextInputMask
              ref={inputElementRef}
              type={type}
              options={options}
              includeRawValueInChangeText
              onBlur={onBlur}
              value={value}
              testID="test-mask-input-id"
              onChangeText={(maskedValue, unmaskedValue) => {
                setRawValue(unmaskedValue);
                onChange(maskedValue);
              }}
              customTextInput={BaseInput}
              customTextInputProps={{
                rawValue,
                error: errors[name],
                label,
                ...props,
              }}
            />
          ) : (
            <BaseInput
              disabled={disabled}
              onChangeText={onChange}
              onBlur={onBlur}
              returnKeyType="next"
              selectionColor={'gray'}
              label={label}
              value={value}
              {...props}
            />
          )}
          {errors[name] ? <Error>{errors[name].message}</Error> : null}
        </Container>
      )}
      name={name}
      rules={{ required: true }}
      defaultValue=""
    />
  );
};

export default forwardRef(Input);
