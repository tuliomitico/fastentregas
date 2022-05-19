import React from 'react';
import { useNavigation } from '@react-navigation/native';
import { yupResolver } from '@hookform/resolvers/yup';
import * as Yup from 'yup';

import Input from '../../../components/Input';
import { Container, SignupButton } from './styles';
import { useForm } from 'react-hook-form';
import AuthService from '../../../services/AuthService';
import { MaskService } from 'react-native-masked-text';

interface SignUpCredentials {
  telephone: string;
  password: string;
}

export default function Register(): React.ReactElement {
  const navigation = useNavigation();
  const schema = Yup.object().shape({
    telephone: Yup.string().required('Telefone Obrigatório'),
    password: Yup.string()
      .required('Senha Obrigatória')
      .min(8, 'A senha tem que ser no mínio 8 dígitos'),
    confirmPassword: Yup.string()
      .when('password', {
        is: (val: any) => !!val.lentgh,
        then: Yup.string().required('Campo obrigatório'),
        otherwise: Yup.string(),
      })
      .oneOf([Yup.ref('password')], 'Confirmação incorreta'),
  });
  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),
    mode: 'onBlur',
    defaultValues: { password: '', telephone: '' },
  });

  const handleSignUp = async (data: SignUpCredentials) => {
    // console.log(data);

    const { telephone: maskedTelephone, password } = data;
    const telephone = MaskService.toRawValue('cel-phone', maskedTelephone);
    try {
      await AuthService.signUp({ telephone, password });
    } catch (error) {
      console.log(error.response.data.error);
    }
    navigation.navigate('Home');
  };
  return (
    <Container>
      <Input
        errors={errors}
        control={control}
        name="telephone"
        label="Telefone"
        inputMask
        type={'cel-phone'}
        options={{ dddMask: '(99) ', withDDD: true, maskType: 'BRL' }}
        keyboardType="phone-pad"
        returnKeyType="next"
        color="purple"
      />
      <Input
        errors={errors}
        control={control}
        name="password"
        label="Senha"
        secureTextEntry
        color="purple"
      />
      <Input
        errors={errors}
        control={control}
        name="confirmPassword"
        label="Confirmar senha"
        secureTextEntry
        color="purple"
      />
      <SignupButton
        title="Cadastrar"
        type="solid"
        onPress={handleSubmit(handleSignUp)}
      />
    </Container>
  );
}
