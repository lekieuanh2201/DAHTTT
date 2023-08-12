import React from 'react';
import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import HotTopics from './pages/TrendingPosts';

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Layout />}>
            <Route index element={<Home />}/>
            <Route path='hot-topics' element={<HotTopics />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
