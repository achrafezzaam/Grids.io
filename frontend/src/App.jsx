import './App.css';
import {Routes, Route} from 'react-router-dom';
import Layout from './components/Layout';
import Home from './components/Home';
import Grids from './components/Grids';
import Components from './components/Components';

function App() {

  return (
    <>
      <Routes>
	<Route path='/' element={<Layout />}>
        <Route index element={<Home />} />
        <Route path='/grids' element={<Grids />} />
        <Route path='/components' element={<Components />} />
	</Route>
      </Routes>
    </>
  )
};

export default App
