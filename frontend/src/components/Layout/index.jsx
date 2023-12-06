import './index.css';
import Sidebar from '../Sidebar';
import {Outlet} from 'react-router-dom';

const Layout = () => {
  return <div className='my-app'>
		<Sidebar />
		<Outlet />
	</div>
}

export default Layout
