import { Routes, Route } from 'react-router-dom';
import About from '../pages/About';
import Home from '../pages/Home';

export default function AppRoutes() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </>
  );
}