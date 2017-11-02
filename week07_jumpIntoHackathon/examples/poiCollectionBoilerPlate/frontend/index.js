import React from 'react';
import ReactDOM from 'react-dom';
import MapDemo from './mapdemo/mapdemo';

import './index.css';

function App() {
  return (
    <div style={{ width: '100%', height: '100%' }}>
      <MapDemo />
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
