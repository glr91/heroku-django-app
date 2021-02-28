import logo from './logo.svg';
import './App.css';
import Tree from '@naisutech/react-tree';
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

function App() {
  const nodes = [
    {
      label: 'Node',
      id: 1234,
      parentId: null,
      items: [
        {
          label: 'Child node 1',
          id: 1236,
          parentId: 1234,
        },
        {
          label: 'Child node 2',
          id: 5678,
          parentId: 1234
        }
      ]
    },
    {
      label: 'Node',
      id: 1235,
      parentId: null
    }
  ]
  return (
    <div style={{ display: 'flex', flexWrap: 'nowrap', flexGrow: 1 }}>
      <div style={{ width: '100%', display: 'flex', flexDirection: 'column' }}>
        <Tree nodes={nodes} size="full" theme={'light'} />
      </div>
    </div>
  )
}

export default App;
