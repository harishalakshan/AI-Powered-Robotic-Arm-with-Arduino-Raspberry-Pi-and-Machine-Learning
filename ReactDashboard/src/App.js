import React, { useState } from 'react';

function App() {
  const [status, setStatus] = useState("Idle");

  const sendCommand = async (cmd) => {
    setStatus("Sending...");
    await fetch(`http://raspberrypi.local:5000/control?cmd=${cmd}`);
    setStatus("Done");
  }

  return (
    <div className="App">
      <h1>Robotic Arm Control Dashboard</h1>
      <button onClick={() => sendCommand('90,90')}>Activate</button>
      <button onClick={() => sendCommand('0,0')}>Deactivate</button>
      <p>Status: {status}</p>
    </div>
  );
}

export default App;