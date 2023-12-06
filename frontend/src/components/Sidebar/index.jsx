import './index.css';
import {NavLink} from 'react-router-dom';

const Sidebar = () => (
  <div className='nav-bar'>
    <nav>
      <NavLink exact="true" activeclassname='active' to='/'>
        Home
      </NavLink>
      <NavLink exact="true" activeclassname='active' to='/grids'>
        Grids
      </NavLink>
      <NavLink exact="true" activeclassname='active' to='/components'>
        Components
      </NavLink>
    </nav>
  </div>
)

export default Sidebar
