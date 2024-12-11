import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SearchPage from './pages/SearchPage';
import './styles.css'; 

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-[#120428] text-white ">
        <Routes>
          <Route path="/" element={<SearchPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
