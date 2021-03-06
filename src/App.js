import logo from './logo.svg';
import './App.css';
import Tree from '@naisutech/react-tree';
import axios from 'axios';
import React, { useState, useEffect } from "react";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

function App() {

  // //var nodes = [
  //   /*     {
  //         label: 'Node',
  //         id: 1234,
  //         parentId: null,
  //         items: [
  //           {
  //             label: 'Child node 1',
  //             id: 1236,
  //             parentId: 1234,
  //           },
  //           {
  //             label: 'Child node 2',
  //             id: 5678,
  //             parentId: 1234
  //           }
  //         ]
  //       },
  //       {
  //         label: 'Node',
  //         id: 1235,
  //         parentId: null
  //       } */
  //     //]
  

  const axios = require('axios');
  var bands = null;
  var albums = null;

  const [nodes, setNodes] = useState([]);

  useEffect(() => {
    axios.get('api/bands/')
    .then(function (response) {
      // handle success
      bands = response.data;
      axios.get('api/albums/')
      .then(function (response) {
        // handle success
        albums = response.data;
        let nodes = [];
        bands.map((band) => {
          nodes = nodes.concat({
            label: band.name,
            id: band.id,
            parentId: null
          });
        })
        setNodes(nodes);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
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
