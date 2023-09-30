import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as BsIcons from 'react-icons/bs';
import * as SiIcons from 'react-icons/si';
import * as BiIcons from 'react-icons/bi';

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
    icon: <IoIcons.IoMdHelpCircle />,
    cName: 'nav-text'
  },
  {
    title: 'Pricing',
    path: '/pricing',
    icon: <BiIcons.BiSolidDollarCircle />,
    cName: 'nav-text'
  }
];