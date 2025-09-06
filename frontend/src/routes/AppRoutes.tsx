import { Routes, Route } from 'react-router-dom';
import { ROUTES } from './routes';

import About from '../pages/About';
import Home from '../pages/Home';

export default function AppRoutes() {
  return (
    <>
      <Routes>
        <Route path={ROUTES.HOME} element={<Home />} />
        <Route path={ROUTES.ABOUT} element={<About />} />
      </Routes>
    </>
  );
}