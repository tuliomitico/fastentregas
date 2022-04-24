import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from '@mui/material';
import React from 'react';

const DATA = [
  {
    deliver: '543251',
    hour: '20:30',
    address: 'Rua dos Bobos, 0, São Nunca',
    telephone: '34 1234-5678',
    name: 'João Ninguém',
    date: '20/02/2022',
  },
];

export default function Dashboard() {
  return (
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
          </TableRow>
        </TableHead>
        <TableBody>
          {DATA.map(row => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell scope="row">{row.deliver}</TableCell>
              <TableCell align="right">{row.hour}</TableCell>
              <TableCell align="right">{row.address}</TableCell>
              <TableCell align="right">{row.telephone}</TableCell>
              <TableCell align="right">{row.name}</TableCell>
              <TableCell align="right">{row.date}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
