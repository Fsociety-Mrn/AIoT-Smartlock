import React, { useState } from 'react';
import './Account.css'; // Link to your CSS file
import { LogoutSession } from '../../Authentication/Authentication'


const Account = () => {
  const [name, setName] = useState('');
  const [contact, setContact] = useState('');
  const [communication, setCommunication] = useState('');
  const [isChangePasswordOpen, setIsChangePasswordOpen] = useState(false);
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');

  const handleFormSubmit = (e) => {
    e.preventDefault();
    console.log('Name:', name);
    console.log('Contact:', contact);
    console.log('Communication:', communication);
  };

  const handlePasswordChange = () => {
    setIsChangePasswordOpen(true);
  };

  const handleCloseChangePassword = () => {
    setIsChangePasswordOpen(false);
    setOldPassword('');
    setNewPassword('');
  };

  return (
    <div className="account-container">
      <div className="account-card">
        <h1>Profile Settings</h1>
        <form onSubmit={handleFormSubmit}>
          <label htmlFor="name">Name:</label>
          <input type="text" id="name" value={name} onChange={(e) => setName(e.target.value)} required />

          <label htmlFor="contact">Contact Details:</label>
          <input type="text" id="contact" value={contact} onChange={(e) => setContact(e.target.value)} required />

          <label htmlFor="communication">Preferred Communication:</label>
          <input type="text" id="communication" value={communication} onChange={(e) => setCommunication(e.target.value)} required />

          <button type="submit">Save Changes</button>
        </form>

        <div className="links">
          <button onClick={handlePasswordChange}>Change Password</button>
        </div>
        <div className="links">
        <button onClick={() => {LogoutSession();window.location.reload(); }}>Logout</button>
        </div>
      
      </div>


      {isChangePasswordOpen && (
        <div className="modal">
          <div className="card-modal">
            <h2>Change Password</h2>
            <label htmlFor="oldPassword">Old Password:</label>
            <input type="password" id="oldPassword" value={oldPassword} onChange={(e) => setOldPassword(e.target.value)} />

            <label htmlFor="newPassword">New Password:</label>
            <input type="password" id="newPassword" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} />
            <div className="button-group">
              <button className="cancel-button" onClick={handleCloseChangePassword}>Cancel</button>
              <button className="save-button" onClick={handleCloseChangePassword}>Save</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Account;
