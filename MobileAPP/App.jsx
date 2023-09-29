import { 
	StatusBar 
} from 'expo-status-bar'
import {
	NavigationContainer ,
} from '@react-navigation/native'
import Drawer from './components/Drawer'
import { Snackbar } from "@react-native-material/core"
import { useState } from 'react'

export default function App() {
	const [isShowed ,setIsShowed] = useState(false)

	const changeVisibility =()=>{
		setIsShowed(previousState =>!previousState)
		setTimeout(()=>{
			setIsShowed(previousState =>!previousState)
		},1000)
	}

	return (
		<NavigationContainer>			
			<Drawer changeVisibility={changeVisibility} />
			<StatusBar style='auto'/>
			{ isShowed &&
				(<Snackbar
					message="The Email has been copied to your Clipboard."
					style={{ position: "absolute", start: 16, end: 16, bottom: 16 }}
					/>)
			}
		</NavigationContainer>
		
	)
}


