import * as yup from "yup"

// export const addOrderSchema = yup.object().shape({
//     name: yup.string().required(),
//     email : yup.string().email(),
//     location : yup.string().required(),
//     purchase : yup.string().required()
// })

//Email validation
export const userSchema = yup.object().shape({
    email : yup.string().email().required(),
    password: yup.string().min(6).required(),
});


export const emailSchema = yup.object().shape({
    email : yup.string().email().required()
});

export const passwordSchema = yup.object().shape({
    password: yup.string().min(6).required()
});

// // Quantity Order
// export const QuantitySchema = yup.object().shape({
//     quantity: yup.number().positive().integer()
// })