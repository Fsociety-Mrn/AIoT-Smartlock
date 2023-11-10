import React from 'react';

const MyLocker = () => {
  const cardStyle = {
    width: '300px',
    padding: '20px',
    backgroundColor: '#f9f9f9',
    borderRadius: '10px',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    textAlign: 'center',
  };

  const buttonStyle = {
    margin: '10px',
    padding: '10px 20px',
    backgroundColor: '#4CAF50',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
    transition: 'background-color 0.3s ease',
  };

  const containerStyle = {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    flexDirection: 'column',
    height: '100vh',
  };

  const buttonContainerStyle = {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    flexDirection: 'column',
    marginTop: '20px',
  };

  return (
    <div style={containerStyle}>
      <div style={cardStyle}>
        <h1 style={{ marginBottom: '20px' }}>My Locker</h1>
        <div style={buttonContainerStyle}>
          <button
            style={buttonStyle}
            onMouseOver={(e) => (e.target.style.backgroundColor = '#38597a')}
            onMouseOut={(e) => (e.target.style.backgroundColor = '#45a8a8')}
          >
            Button 1
          </button>
          <button
            style={buttonStyle}
            onMouseOver={(e) => (e.target.style.backgroundColor = '#38597a')}
            onMouseOut={(e) => (e.target.style.backgroundColor = '#45a8a8')}
          >
            Button 2
          </button>
          <button
            style={buttonStyle}
            onMouseOver={(e) => (e.target.style.backgroundColor = '#38597a')}
            onMouseOut={(e) => (e.target.style.backgroundColor = '#45a8a8')}
          >
            Button 3
          </button>
        </div>
      </div>
    </div>
  );
};

export default MyLocker;
