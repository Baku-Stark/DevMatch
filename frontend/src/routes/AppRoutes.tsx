import { Routes, Route } from 'react-router-dom';
import About from '../pages/About';

export default function AppRoutes() {
  return (
    <>
      <Routes>
        <Route path="/about" element={<About />} />
      </Routes>
    </>
  );
}
