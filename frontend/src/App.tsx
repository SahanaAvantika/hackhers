import { useCallback, useEffect, useState } from '@lynx-js/react';

import './App.css';
import arrow from './assets/arrow.png';
import lynxLogo from './assets/lynx-logo.png';
import reactLynxLogo from './assets/react-logo.png';
import Login from './pages/Login.js'; 
import Home from './pages/Home.js';

export function App(props: {
  onRender?: () => void
}) {
  const [alterLogo, setAlterLogo] = useState(false);

  useEffect(() => {
    console.info('Hello, ReactLynx');
  }, []);

  props.onRender?.();

  const onTap = useCallback(() => {
    'background only';
    setAlterLogo(prev => !prev);
  }, []);

  return (
    <view>
      <view style={{ padding: 20 }}>
        <Login />
      </view>
    </view>
  );
}
