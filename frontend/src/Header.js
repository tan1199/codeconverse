import { Sidebar, Menu, MenuItem } from 'react-pro-sidebar';

import React, { useState } from 'react';
import { Link } from 'react-router-dom';


const Header = () => {

    //create initial menuCollapse state using useState hook
    const [menuCollapse, setMenuCollapse] = useState(false)

    //create a custom function that will change menucollapse state from false to true and true to false
  const menuIconClick = () => {
    //condition checking to change state from true to false and vice versa
    menuCollapse ? setMenuCollapse(false) : setMenuCollapse(true);
  };

  return (
    <>

    </>
  );
};

export default Header;