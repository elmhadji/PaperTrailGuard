import { 
	StyleSheet, 
	Text, 
	View,
	Pressable
} from 'react-native'
import {Camera} from 'expo-camera'
import {BarCodeScanner} from 'expo-barcode-scanner' 
import IonIcons from '@expo/vector-icons/FontAwesome'

const CodeReader = () => {
	const [status ,requestPermission] = Camera.useCameraPermissions()
	
	const handelOnScanned=({type,data})=>{
		alert(`Bar code with type ${type} and data ${data} has been scanned!`);
	}

	return (
		<View
			style={{
				justifyContent:'center',
				alignItems:'center',
				flex:1				
			}}
			>
				{status && !status.granted &&(
					<View>
							<Pressable 
								onPress={requestPermission}
								style={{
									backgroundColor:'blue',
									borderRadius:15,
									padding:20
								}}
								>
								<Text
									style={{
										color:'#fff',
										fontSize:15
									}}
									>
									We need your permission to show the camera
								</Text>
							</Pressable>
					</View>
				)}
				{ status && status.granted &&(
				<View 
					style={{
						flex:1,
					
					}}
					>
					<Camera
						barCodeScannerSettings={{
							barCodeTypes: [BarCodeScanner.Constants.BarCodeType.qr],
						}}
						onBarCodeScanned={handelOnScanned}
						style={{
							height:570,
							width:400,
						}}
						/>
					<View
						style={{
							flex:1,
							justifyContent:'center',
							alignItems:'center'

						}}
						>
						<Pressable
							style={{
								justifyContent:'center',
								alignItems:'center',
								paddingHorizontal:50,
								paddingVertical:10,
								backgroundColor:'#D9D9D9',
								borderRadius:17,
								width:165,
								height:65,
							}}
							>
							<IonIcons 
								name='image'
								size={30}
								/>
						</Pressable>
					</View>
				</View>
			)
		}
		
		</View>
	)
}

export default CodeReader
