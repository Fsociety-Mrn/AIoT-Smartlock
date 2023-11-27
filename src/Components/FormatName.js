const FormatName = (Text) => {
    const wordsArray = Text.split(',');
    const reversedText = wordsArray.reverse().join(' ').toUpperCase();
    return reversedText;
}

export default FormatName;