import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as BsIcons from 'react-icons/bs';
import * as SiIcons from 'react-icons/si';

export const SidebarData = [
  {
    title: 'Manage Data Sources',
    path: '/data',
    icon: <BsIcons.BsFillDatabaseFill />,
    cName: 'nav-text'
  },
  {
    title: 'Customize',
    path: '/customize',
    icon: <IoIcons.IoIosPaper />,
    cName: 'nav-text'
  },

  {
    title: 'About',
    path: '/about',
    icon: <IoIcons.IoMdPeople />,
    cName: 'nav-text'
  },
  {
    title: 'Analytics',
    path: '/analytics',
    icon: <SiIcons.SiGoogleanalytics />,
    cName: 'nav-text'
  },
  {
    title: 'Support',
    path: '/support',
    icon: <IoIcons.IoMdHelpCircle />,
    cName: 'nav-text'
  }
];