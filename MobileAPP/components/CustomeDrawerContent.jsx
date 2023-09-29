import { 
	DrawerContentScrollView,  
	DrawerItem 
} from '@react-navigation/drawer'
import { 
	Image, 
	View ,
} from 'react-native'
import * as Clipboard from 'expo-clipboard'
import Label from './Label'


const CustomDrawerContent = (props) => {
    const image = require('../assets/logo.png')


    return (
			<DrawerContentScrollView 
				{...props} 
				contentContainerStyle={{
					justifyContent:'space-between',
					flex:1,
				}}
				>
				<View >
					<DrawerItem
						label={() => {
							return (
								<View style={{flexDirection:'row'}}>
									<Image source={image} style={{height:200,width:200}} />
								</View>
							)
						}}
						/>
					<DrawerItem
						label={()=><Label name='camera' label='Scane'/>}
						onPress={()=>props.navigation.navigate('QR Code Reader')}
						/>
					<DrawerItem
						label={()=><Label name='qrcode' label='Generate'/>}
						onPress={()=>props.navigation.navigate('QR Code Generator')}
						/>
				</View>
				<DrawerItem
					label={()=> <Label	name='envelope' label='Bahrib665@gmail.com'/>}
					onPress={()=>{
						Clipboard.setStringAsync('Bahrib665@gmail.com')
						props.changeVisibility()
					}
				}
				/>
			</DrawerContentScrollView>

    );
}

export default CustomDrawerContent;
