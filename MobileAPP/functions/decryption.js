import 'react-native-get-random-values'
import CryptoJS from'crypto-js'

const decrypt =  (encryptedText)=> {
    const encryptedData = CryptoJS.enc.Base64.parse(encryptedText.slice(0,encryptedText.length-24));

    // assuming `key` is the key obtained securely from the Python script
    const key = CryptoJS.enc.Base64.parse( encryptedText.slice(encryptedText.length-24 ,encryptedText.length));
  
    // the IV is the first 16 bytes of the encrypted data
    const iv = CryptoJS.lib.WordArray.create(encryptedData.words.slice(0, 4));
    
    // the actual encrypted data is the remainder
    const encrypted = CryptoJS.lib.WordArray.create(encryptedData.words.slice(4));
    
    // decrypt the data
    const decryptedData = CryptoJS.AES.decrypt({ciphertext: encrypted}, key, {iv: iv});

    // console.log("Decrypted data:", decryptedData.toString(CryptoJS.enc.Utf8));
    return decryptedData.toString(CryptoJS.enc.Utf8);
}

export default decrypt

