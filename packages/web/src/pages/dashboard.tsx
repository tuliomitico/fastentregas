import React from 'react';
import { GetServerSideProps } from 'next';
import { parseCookies } from 'nookies';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';

import Layout from '../components/Layout';
import { getAPIClient } from '../services/axios';
import { Typography } from '@mui/material';

type Props = {
  name: string;
  deliverys: Array<any>;
};

export default function Dashboard(props: Props) {
  return (
    <Layout>
      <Typography>Olá, {props.name}</Typography>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
          <TableHead>
            <TableRow>
              <TableCell>Entregas</TableCell>
              <TableCell align="right">Horário</TableCell>
              <TableCell align="right">Endereço</TableCell>
              <TableCell align="right">Telefone do cliente</TableCell>
              <TableCell align="right">Nome do cliente</TableCell>
              <TableCell align="right">Data</TableCell>
              <TableCell align="right">Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {props.deliverys.map(row => (
              <TableRow
                key={row.name}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell scope="row">{row.id}</TableCell>
                <TableCell align="right">{row.hour}</TableCell>
                <TableCell align="right">
                  {row.address.st_or_av}, {row.address.number} -{' '}
                  {row.address.district}
                </TableCell>
                <TableCell align="right">{row.telephone}</TableCell>
                <TableCell align="right">{row.name}</TableCell>
                <TableCell align="right">?</TableCell>
                <TableCell align="right">
                  {row.status === 'avaliable'
                    ? 'Aberto'
                    : row.status === 'closed'
                    ? 'Finalizado'
                    : 'Em rota'}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Layout>
  );
}

export const getServerSideProps: GetServerSideProps = async ctx => {
  const apiClient = getAPIClient(ctx);
  const { 'nextauth.token': token } = parseCookies(ctx);

  if (!token) {
    return {
      redirect: {
        destination: '/',
        permanent: false,
      },
    };
  }

  const {
    data: {
      user: { name },
    },
  } = await apiClient.get('/user');
  const {
    data: { deliverys },
  } = await apiClient.get('/deliver');
  console.log(name);

  return {
    props: { name, deliverys },
  };
};
