import { CameraView, useCameraPermissions } from 'expo-camera';
import { useState } from 'react';
import { Button, StyleSheet, Text, Alert, View } from 'react-native';
import * as Clipboard from'expo-clipboard';
import CryptoJS from'crypto-js';

export default function App() {
  const [isShowing, setIsShowing] = useState(false);
  const [permission, requestPermission] = useCameraPermissions();

  if (!permission) {
    // Camera permissions are still loading.
    return <View />;
  }

  if (!permission.granted) {
    // Camera permissions are not granted yet.
    return (
      <View style={styles.container}>
        <Text style={{ textAlign: 'center' }}>We need your permission to show the camera</Text>
        <Button onPress={requestPermission} title="grant permission" />
      </View>
    );
  }
  function decryption (encryptedText:string):string {
      const encryptedData = CryptoJS.enc.Base64.parse(encryptedText.slice(0,encryptedText.length-24));
      // assuming `key` is the key obtained securely from the Python script
      const key = CryptoJS.enc.Base64.parse( encryptedText.slice(encryptedText.length-24 ,encryptedText.length));
      // the IV is the first 16 bytes of the encrypted data
      const iv = CryptoJS.lib.WordArray.create(encryptedData.words.slice(0, 4));
      // the actual encrypted data is the remainder
      const encrypted = CryptoJS.lib.WordArray.create(encryptedData.words.slice(4));
      // Convert the WordArray to a base64 string
      const encryptedBase64 = encrypted.toString(CryptoJS.enc.Base64);
      // decrypt the data
      const decryptedData = CryptoJS.AES.decrypt(encryptedBase64, key, {iv: iv});
      // console.log("Decrypted data:", decryptedData.toString(CryptoJS.enc.Utf8));
      return decryptedData.toString(CryptoJS.enc.Utf8);
    }
  function handelOnScanned (_:string,data:string){
      if (!isShowing){
        const result:string = decryption(data)
        Alert.alert('QR Code Scanned',`Result :${result}`,
            [
              {
                text:'Copy Text',
                onPress: ()=>{
                  Clipboard.setStringAsync(result)
                  setIsShowing(previousStat =>!previousStat)
                } 
              },
              {
                text:'OK',
                onPress:()=>setIsShowing(previousStat =>!previousStat)
              },
            ]
          )
        setIsShowing(previousStat =>!previousStat)
      }
		}

  return (
    <View style={styles.container}>
      <CameraView 
        style={styles.camera}
        focusable={true}
        barcodeScannerSettings={{barcodeTypes:["qr"]}}
        onBarcodeScanned={({type ,data})=>{handelOnScanned(type ,data)}}
        />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
  },
  camera: {
    flex: 1,
  },
  buttonContainer: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: 'transparent',
    margin: 64,
  },
  button: {
    flex: 1,
    alignSelf: 'flex-end',
    alignItems: 'center',
  },
  text: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
  },
});