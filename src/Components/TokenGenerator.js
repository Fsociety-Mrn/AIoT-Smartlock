
const TokenGenerator = () => {
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    var otp = '';
    for (var i = 0; i < 6; i++) {
        var index = Math.floor(Math.random() * characters.length);
        otp += characters.charAt(index);
    }
    return otp;
}

export default TokenGenerator