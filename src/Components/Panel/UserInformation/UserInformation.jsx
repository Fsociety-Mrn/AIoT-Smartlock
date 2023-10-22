import React, { useState } from "react";
import FormInput from "../../Forms/FormInput/FormInput";
import Titles from "../../Titles/Titles";
import { Form, Row, Col, Button, Modal } from "react-bootstrap";
import { useFormik } from "formik";
import { object, string, date } from "yup";
import PropTypes from "prop-types";
import UserChangePassword from "../UserChangePassword/UserChangePassword";

// Sample data (replace this with your actual data)
const sampleData = [
  {
    username: "sampleUser1",
    firstName: "John",
    lastName: "Doe",
    email: "john@example.com",
    birthday: "1990-01-15"
  },
  {
    username: "sampleUser2",
    firstName: "Jane",
    lastName: "Smith",
    email: "jane@example.com",
    birthday: "1985-08-22"
  }
];

const UserInformation = ({
  username,
  firstName,
  lastName,
  email,
  birthday,
  onChangeInfo
}) => {
  const [submit, setSubmit] = useState(false);
  const [showPasswordModal, setShowPasswordModal] = useState(false);

  const isNotIterateEmail = (username, email) => {
    // Check if the email already exists in the sample data
    const isNotDuplicateEmail = !sampleData.some(
      (user) => user.username !== username && user.email === email
    );
    return isNotDuplicateEmail;
  };

  const formik = useFormik({
    initialValues: {
      firstName: firstName ? firstName : "",
      lastName: lastName ? lastName : "",
      email,
      birthday
    },
    validationSchema: object({
      firstName: string().max(
        10,
        "Your first name must be 10 characters or less"
      ),
      lastName: string().max(
        10,
        "Your last name must be 10 characters or less"
      ),
      email: string()
        .required("Please enter your email")
        .email("Invalid email"),
      birthday: date()
        .required("Please enter your birthday date")
        .min("1922-01-01", "Your birthday date must be on or after 1922-01-01")
        .max("2022-05-22", "Invalid birthday date")
    }),
    onSubmit: ({ firstName, lastName, email, birthday }, { setFieldError }) => {
      const isNotDuplicateEmail = isNotIterateEmail(username, email);

      if (isNotDuplicateEmail) {
        onChangeInfo(
          ["firstName", "lastName", "email", "birthday"],
          [firstName, lastName, email, birthday]
        );
      } else {
        setFieldError("email", "You can't choose this email");
      }
    }
  });

  const handleShowPasswordModal = () => {
    setShowPasswordModal(true);
  };

  const handleClosePasswordModal = () => {
    setShowPasswordModal(false);
  };

  return (
    <>
      <Titles
        title="Welcome to the Information"
        text="Check or change your information as you want"
      />
      <Form noValidate onSubmit={formik.handleSubmit}>
        <Row className="mt-5 px-3">
          <FormInput
            xs={12}
            lg
            as={Col}
            inpClass="py-2"
            className="p-0"
            name="firstName"
            controlId="first-name-input"
            text="First Name"
            placeholder="Arash"
            size="sm"
            invalid={
              formik.values.firstName === ""
                ? false
                : submit && formik.errors.firstName
                ? true
                : false
            }
            errMsg={formik.errors.firstName || ""}
            valid={
              formik.values.firstName === ""
                ? false
                : submit && !formik.errors.firstName
                ? true
                : false
            }
            successMsg="done"
            {...formik.getFieldProps("firstName")}
          />
          <FormInput
            xs={12}
            lg
            as={Col}
            inpClass="py-2"
            className="p-0 ms-lg-5 mt-3 mt-lg-0"
            name="lastName"
            controlId="last-name-input"
            text="Last Name"
            placeholder="Karimi"
            size="sm"
            invalid={
              formik.values.lastName === ""
                ? false
                : submit && formik.errors.lastName
                ? true
                : false
            }
            errMsg={formik.errors.lastName || ""}
            valid={
              formik.values.lastName === ""
                ? false
                : submit && !formik.errors.lastName
                ? true
                : false
            }
            successMsg="done"
            {...formik.getFieldProps("lastName")}
          />
        </Row>

        <Row className="mt-3 mt-lg-4 px-3">
          <FormInput
            xs={12}
            lg
            as={Col}
            inpClass="py-2"
            className="p-0"
            name="email"
            controlId="email-input"
            text="Email"
            placeholder="Enter your Email"
            size="sm"
            errMsg={formik.errors.email || ""}
            successMsg="done"
            invalid={submit && formik.errors.email ? true : false}
            valid={submit && !formik.errors.email ? true : false}
            {...formik.getFieldProps("email")}
          />
          <FormInput
            xs={12}
            lg
            as={Col}
            inpClass="py-2"
            className="p-0 ms-lg-5 mt-3 mt-lg-0"
            name="birthday"
            controlId="birthday-input"
            text="Birthday"
            size="sm"
            placeholder="Enter your birthday"
            type="date"
            invalid={submit && formik.errors.birthday ? true : false}
            errMsg={formik.errors.birthday || ""}
            valid={submit && !formik.errors.birthday ? true : false}
            successMsg="done"
            {...formik.getFieldProps("birthday")}
          />
        </Row>

        <div className="d-flex justify-content-center align-items-center">
          <Button
            onClick={() => setSubmit(true)}
            disabled={submit && !formik.isValid ? true : false}
            variant="primary"
            className="mt-5 py-2 px-4 mx-2"
            type="submit"
          >
            Update
          </Button>

          <Button
            variant="primary"
            className="mt-5 py-2 px-4 mx-2"
            onClick={handleShowPasswordModal}
          >
            Change Password
          </Button>
        </div>
      </Form>

      {/* Password Change Modal */}
      <Modal show={showPasswordModal} onHide={handleClosePasswordModal}>
        <Modal.Header closeButton>
          <Modal.Title>Change Password</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {/* Create a separate component for the password change form */}
          <UserChangePassword />
        </Modal.Body>
      </Modal>
    </>
  );
};

UserInformation.propTypes = {
  onChangeInfo: PropTypes.func.isRequired
};

export default UserInformation;
