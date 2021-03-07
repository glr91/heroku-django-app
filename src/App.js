import logo from './logo.svg';
import './App.css';
import Tree from '@naisutech/react-tree';
import axios from 'axios';
import React, { useState, useEffect } from "react";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

function App() {

  const axios = require('axios');
  var bands = null;
  var albums = null;

  const [nodes, setNodes] = useState([]);

  useEffect(() => {
    axios.get('api/albums-band-tree/')
    .then(function (response) {
      // handle success
      let nodes = response.data;
        setNodes(nodes);
    })
    .catch(function (error) {
      // handle error
      console.log(error);
    })
  });

  return (
    <div style={{ display: 'flex', flexWrap: 'nowrap', flexGrow: 1 }}>
      <div style={{ width: '100%', display: 'flex', flexDirection: 'column' }}>
        <Tree nodes={nodes} size="full" theme={'light'} />
      </div>
    </div>
  );
}

export default App;
