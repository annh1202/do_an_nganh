// src/RouteConfig.js
import React from 'react';
import Home from '@/modules/Home';
import LyThuyetCSDL from '@/modules/LyThuyetCSDL/LyThuyetCSDL';

export const RouteConfig = [
  {
    path: '/',
    label: 'Trang chủ',
    element: <Home />,
    showInMenu: false,
  },
  {
    path: '/ly-thuyet-csdl',
    label: 'Lý thuyết CSDL',
    element: <LyThuyetCSDL />,
    showInMenu: true,
    isNested: true,
  }
];