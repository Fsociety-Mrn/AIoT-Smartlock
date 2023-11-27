import * as yup from "yup"

// export const addOrderSchema = yup.object().shape({
//     name: yup.string().required(),
//     email : yup.string().email(),
//     location : yup.string().required(),
//     purchase : yup.string().required()
// })


// const passwordRules = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{5,}$/;
// min 5 characters, 1 upper case letter, 1 lower case letter, 1 numeric digit.

//Email and password validation
export const userSchema = yup.object().shape({
    email : yup.string()
            .email("Incorrect email format")
            .required("Please fill out the email field"),

    password: yup.string()
            // .matches(passwordRules, { message: "Please create a stronger password" })
            .required("Please enter a password")
            .min(6,"Password should be 6 char long")
});


//Email and password validation
export const SignUp_userSchema = yup.object().shape({
        email : yup.string()
                .email("Incorrect email format")
                .required("Please fill out the email field"),
    
        password: yup.string()
                // .matches(passwordRules, { message: "Please create a stronger password" })
                .required("Please enter a password")
                .min(6,"Password should be 6 char long"),

        confirmPassword: yup.string()
                // .matches(passwordRules, { message: "Please create a stronger password" })
                .required("Please enter a password")
                .min(6,"Password should be 6 char long")
                .oneOf([yup.ref('password'), null], 'Passwords must match')
    });

// Name Validation
export const Name_Schema = yup.object().shape({
        firstName: yup.string()
            .matches(/^[a-zA-Z\s]+$/, "Letters and spaces only")
            .required("First name required"),
        lastName: yup.string()
            .matches(/^[a-zA-Z\s]+$/, "Letters and spaces only")
            .required("Last name required"),
    });

// Password Validation
export const Change_password = yup.object().shape({
        CurrentPassword: yup.string()
                // .matches(passwordRules, { message: "Please create a stronger password" })
                .required("Please enter your current password")
                .min(6,"Password should be 6 char long"),

        NewPassword: yup.string()
                // .matches(passwordRules, { message: "Please create a stronger password" })
                .required("Please enter your new password")
                .min(6,"Password should be 6 char long"),

        ConfirmPassword: yup.string()
                // .matches(passwordRules, { message: "Please create a stronger password" })
                .required("Please enter your new password")
                .min(6,"Password should be 6 char long")
                .oneOf([yup.ref('NewPassword'), null], 'Passwords must match')
    });

// Password Validation
export const Email_validation = yup.object().shape({
        email : yup.string()
                .email("Incorrect email format")
                .required("Please fill out the email field"),
    });
    
// PIN schema
export const pinSchema = yup.object().shape({
        PIN : yup.string()
                .required("Please enter your pin code")
                .min(4,"Password should be 4 char long")
                .max(4,"Password should be 4 char long"),
    
        PIN2: yup.string()
                // .matches(passwordRules, { message: "Please create a stronger password" })
                .required("Please enter your pin code")
                .min(4,"Password should be 4 char long")
                .max(4,"Password should be 4 char long")
                .oneOf([yup.ref('PIN'), null], 'PIN code must be match')
    });