import { StyleSheet,Pressable } from 'react-native'
import IonIcons from '@expo/vector-icons/FontAwesome'

const ButtonIcon = (props) => {
	return (
		<Pressable style={styles.pressable}	onPress={props.onPress}>
			<IonIcons 
				name='image'
				size={30}
				/>
		</Pressable>
	)
}

export default ButtonIcon

const styles = StyleSheet.create({
	pressable:{
		justifyContent:'center',
		alignItems:'center',
		paddingHorizontal:50,
		paddingVertical:10,
		backgroundColor:'#D9D9D9',
		borderRadius:17,
		width:165,
		height:65,
	},
	
})