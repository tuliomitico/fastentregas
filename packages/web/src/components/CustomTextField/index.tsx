'use client';
import React, {
  forwardRef,
  useRef,
  useState,
  useImperativeHandle,
} from 'react';
import { Control, Controller, FieldErrors, FieldValues } from 'react-hook-form';
import TextField, { BaseTextFieldProps } from '@mui/material/TextField';
import InputMask, { BeforeMaskedStateChangeStates } from 'react-input-mask';

interface CustomInputProps extends BaseTextFieldProps {
  name: string;
  control: Control<FieldValues, any>;
  errors: FieldErrors;
  label: string;
  inputMask?: boolean;
  mask?: string;
  maskChar?: string | null;
  formatChars?: object;
  disabled?: boolean;
}

interface InputRef {
  focus(): void;
}

const CustomTextField: React.ForwardRefRenderFunction<
  InputRef,
  CustomInputProps
> = (
  {
    errors,
    name,
    control,
    label,
    mask,
    inputMask,
    maskChar,
    formatChars,
    disabled,
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
  const beforeMaskedStateChange = ({
    currentState,
    nextState,
    previousState,
  }: BeforeMaskedStateChangeStates) => {
    let { value } = currentState;

    const newValue = value.replace(/[^0-9]/g, '');
    if (newValue.length < 10) {
      return nextState;
    }

    if (newValue.length === 10) {
      value = newValue.replace(/^(\d{2})(\d{4})(\d{4})$/, '($1) $2-$3');
    } else if (newValue.length > 10) {
      value = newValue.replace(/^(\d{2})(\d{5})(\d{4})(\d*)$/, '($1) $2-$3');
    }

    return {
      value: value,
      selection: {
        start: value.length,
        end: value.length,
      },
    };
  };
  return (
    <Controller
      control={control}
      render={({ field: { onChange, onBlur, value } }) => (
        <>
          {inputMask ? (
            <InputMask
              ref={inputElementRef}
              mask={mask}
              beforeMaskedStateChange={beforeMaskedStateChange}
              maskPlaceholder={null}
              onBlur={onBlur}
              // value={value}
              onChange={onChange}
            >
              <TextField
                error={!!errors[name]}
                label={label}
                helperText={errors[name] ? errors[name].message : null}
                {...props}
              />
            </InputMask>
          ) : (
            <TextField
              error={!!errors[name]}
              onBlur={onBlur}
              onChange={onChange}
              label={label}
              value={value}
              disabled={disabled}
              helperText={errors[name] ? errors[name].message : null}
              {...props}
            />
          )}
        </>
      )}
      name={name}
      rules={{ required: true }}
      defaultValue=""
    />
  );
};

export default forwardRef(CustomTextField);
