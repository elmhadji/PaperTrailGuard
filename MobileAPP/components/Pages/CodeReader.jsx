import { StyleSheet,Text,View,Pressable,	Alert,} from 'react-native'
import {Camera} from 'expo-camera'
import {BarCodeScanner} from 'expo-barcode-scanner' 
import ButtonIcon from '../ButtonIcon'
import decrypt from '../../functions/decryption'
import { useState } from 'react'
import * as Clipboard from 'expo-clipboard'
import * as ImagePicker from 'expo-image-picker'

const CodeReader = () => {
	const [status ,requestPermission] = Camera.useCameraPermissions()
	const [isShowing ,setIsShowing] = useState(false)
	
	const pickImage = async ()=>{
		const image = await ImagePicker.launchImageLibraryAsync({

				mediaTypes: ImagePicker.MediaTypeOptions.Images,
				allowsMultipleSelection:false,
				allowsEditing:true,
				quality:1,
				barCodeTypes: [BarCodeScanner.Constants.BarCodeType.qr],
			})

		if (! image.canceled){

			console.log('Image selected')
			console.log('the path of image is : ',image.assets[0].uri)
			//TODO: the problem is in he URI (not accepted by the barcode scanner) change to the rn-qr-generator
			const scannedResult = await BarCodeScanner.scanFromURLAsync(image.assets[0].uri , [BarCodeScanner.Constants.BarCodeType.qr])
			console.log('QRCode: ',scannedResult)
		}
	}

	const handelOnScanned=({type,data})=>{
		if (!isShowing){
			const result = decrypt(data)
			Alert.alert(
					'QR Code Scanned',
					`Result :${result} `,
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
		<View style={styles.center}>
			{status && !status.granted &&(
				<View>
					<Pressable onPress={requestPermission} style={{	backgroundColor:'blue',borderRadius:15,padding:20}}>
						<Text style={{color:'#fff',fontSize:15}}>
							We need your permission to show the camera
						</Text>
					</Pressable>
				</View>
			)}
			{ status && status.granted &&(
				<View style={{flex:1}}>
					<Camera
						barCodeScannerSettings={{
							barCodeTypes: [BarCodeScanner.Constants.BarCodeType.qr],
						}}
						onBarCodeScanned={handelOnScanned}
						style={styles.camera}
						/>
					<View style={styles.center}>
						<ButtonIcon
							onPress={pickImage}
							/>
					</View>
				</View>
			)}
		</View>
	)
}

export default CodeReader

const styles = StyleSheet.create({
	center:{
		flex:1,
		justifyContent:'center',
		alignItems:'center'
	},
	camera:{
		height:570,
		width:400,
	}
})