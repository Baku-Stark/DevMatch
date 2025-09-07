import { Routes, Route } from 'react-router-dom';
import { ROUTES } from './routes';

import About from '../pages/About';
import Home from '../pages/Home';
import SignIn from '../pages/SignIn';
import SignUp from '../pages/SignUp';

export default function AppRoutes() {
  return (
    <>
      <Routes>
        <Route path={ROUTES.HOME} element={<Home />} />

        {/* AUTH */}
        <Route path={ROUTES.SIGN_IN} element={<SignIn/>}/>
        <Route path={ROUTES.SIGN_UP} element={<SignUp/>}/>
        {/* AUTH */}

        <Route path={ROUTES.ABOUT} element={<About />} />
      </Routes>
    </>
  );
}