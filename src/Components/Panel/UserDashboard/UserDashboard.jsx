import Titles from "../../Titles/Titles";
import { Form, Button, Modal, Alert } from "react-bootstrap"; // Import Alert from React Bootstrap

import PropTypes from "prop-types";
import React, { useState } from "react"; // Import React and useState

const UserDashboard = ({
  username,
  firstName,
  lastName,
  email,
  birthday,
  onChangeInfo
}) => {
  // State to manage the modal and alert
  const [showModal, setShowModal] = useState(false);
  const [showAlert, setShowAlert] = useState(false);

  // State to store the old PIN and new PIN
  const [oldPin, setOldPin] = useState("");
  const [newPin, setNewPin] = useState("");

  // Function to handle opening the modal
  const handleShowModal = () => {
    setShowModal(true);
    setShowAlert(false); // Hide any previous alerts when opening the modal
  };

  // Function to handle closing the modal
  const handleCloseModal = () => {
    setShowModal(false);
    setShowAlert(false); // Hide any previous alerts when closing the modal
  };

  // Function to handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    // Replace '1234' with the actual correct old PIN
    if (oldPin === "1234") {
      // Old PIN is correct
      // Add your logic for changing the PIN here
      // Once the PIN is changed, you can close the modal
      handleCloseModal();
    } else {
      // Old PIN is incorrect, show an alert
      setShowAlert(true);
    }
  };

  return (
    <>
      <Titles
        title="Welcome to the Dashboard! 🎉"
        text="Explore insights, take control, and make informed decisions with ease."
      />

      <Form>
        <div className="d-flex flex-column justify-content-center align-items-center">
          <Button
            variant="primary"
            className="my-2 px-4"
            type="submit"
            style={{ width: "70%" }}
          >
            Open Locker
          </Button>

          {/* Add the "Change Pin" button with modal */}
          <Button
            variant="primary"
            className="my-2 px-4"
            type="button"
            style={{ width: "70%" }}
            onClick={handleShowModal} // Show modal on button click
          >
            Change Pin
          </Button>
        </div>
      </Form>

      {/* Modal for changing PIN */}
      <Modal show={showModal} onHide={handleCloseModal}>
        <Modal.Header closeButton>
          <Modal.Title>Change PIN</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="oldPin">
              <Form.Label>Old PIN</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter old PIN"
                value={oldPin}
                onChange={(e) => setOldPin(e.target.value)}
              />
            </Form.Group>

            <Form.Group controlId="newPin">
              <Form.Label>New PIN</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter new PIN"
                value={newPin}
                onChange={(e) => setNewPin(e.target.value)}
              />
            </Form.Group>

            {/* Add an alert for incorrect old PIN */}
            {showAlert && (
              <Alert variant="danger">
                Incorrect old PIN. Please try again.
              </Alert>
            )}

            <Button variant="primary" type="submit">
              Save Changes
            </Button>
          </Form>
        </Modal.Body>
      </Modal>
    </>
  );
};

UserDashboard.propTypes = {
  onChangeInfo: PropTypes.func.isRequired
};

export default UserDashboard;
