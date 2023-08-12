import React from 'react';
import { createRoot } from 'react-dom/client';
import 'mdb-react-ui-kit/dist/css/mdb.min.css';
import "@fortawesome/fontawesome-free/css/all.min.css";
import 'react-datepicker/dist/react-datepicker.css';
import App from './App';


const container = document.getElementById('root');
const root = createRoot(container);

root.render(<App />);

