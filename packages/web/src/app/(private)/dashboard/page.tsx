import React from 'react';
import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';
import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
} from '@mui/material';

import { getAPIClient } from '../../../services/axios';

export default async function Dashboard() {
  const apiClient = getAPIClient();
  const token = cookies().get('nextauth.token')?.value ?? null;
  if (!token) {
    return redirect('/');
  }

  const {
    data: {
      user: { name },
    },
  } = await apiClient.get('/user');

  const {
    data: { deliverys },
  } = await apiClient.get('/deliver');

  return (
    <>
      <Typography>Olá, {name}</Typography>
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
            {deliverys.map(row => (
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
    </>
  );
}
